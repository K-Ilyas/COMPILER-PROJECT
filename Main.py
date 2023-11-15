

# This is just for a test purposes : 

# lex = Lex("1233+2-3/3")

# while True :

#     next = lex.NextToken()

#     if next.getType() == Tokens.EndOfFileToken : break

#     print(next.getType(),next.getPos(),next.getText(),next.getValue())

import sys,gc

from colorama import Fore, Back, Style


sys.path.insert(0, 'C:/Users/ilyas/Documents/compiler/syntaxAnalyse')
from Compilation import Compiltaion
from Tokens import Tokens
from VariableSymbol import VariableSymbole
from TextSpan import TextSpan

from SyntaxToken import SyntaxToken
from  SyntaxTree import SyntaxTree

pyCode = ""
variables = dict()


def initCompiler(output_file):
    with open(output_file,"w") as out:
        out.write("#include <stdio.h>\n")
        out.write("#include <stlib.h>\n")
        out.write("int main(){\n")

def endCompiler(output_file):
    with open(output_file,"a") as out:
        out.write("}\n")

def compile(child, output_file):
    global pyCode
    if isinstance(child,SyntaxToken) :
        with open(output_file,"a") as out:
            match child.getType() :
                case Tokens.BlockStatement:
                    out.write("\n")
                case Tokens.OpenBraceToken :
                    out.write("{")
                case Tokens.VarKeyword :
                    out.write("int ")
                case Tokens.IdentifierToken:
                    out.write(str(child.getText()))
                case Tokens.EqualsToken:
                    out.write("=")
                case Tokens.NumberToken:
                    out.write(str(child.getValue()))
                case Tokens.TrueKeyword:
                    out.write("1")
                case Tokens.FalseKeyword:
                    out.write("0")
                case Tokens.CloseBraceToken :
                    out.write("}")
                # case :
                #     pyCode+=" "+child.getText() + " "

    for child2 in child.getChildrens():
        compile(child2, output_file)

def printCode(child):

    global pyCode
    if isinstance(child,SyntaxToken) :

        match child.getType() :
            case Tokens.AmpersandAmpersandToken :
                pyCode +=" and "
            case Tokens.PipePipeToken :
                pyCode +=" or "
            case Tokens.TrueKeyword:
                pyCode +="True"
            case Tokens.FalseKeyword:
                pyCode +="False"
            case Tokens.IdentifierToken :
                  pyCode+= child.getText() 
            case Tokens.NumberToken :
                  pyCode += str(child.getText())
            case _:
                pyCode+=" "+child.getText() + " "

    for child2 in child.getChildrens():
        printCode(child2)

def printResultAsTree(child,sep,isLast = True):

    marker =   "└──" if isLast else "├──"
    print(sep,end="")
    print(marker,end="")
    print(child.getType(),end="")
    if isinstance(child,SyntaxToken) and child.getValue() != None :
        print("  ",end="")
        print(child.getValue(),end="")
        
    print("")

    sep += "    " if isLast else "│   "

    lst =  list(child.getChildrens())

    last = lst[-1] if len(lst) != 0 else child

    for child2 in child.getChildrens():
        printResultAsTree(child2,sep, last == child2)
    
previous = None

while True :
       textBuilder = ""
       while True :
            line = input(" : ")

            if line.strip() == "#":
                 break
            else :
                 textBuilder += line + '\n'

     
       syntaxTree = SyntaxTree.Parse(textBuilder)

       # printResultAsTree(syntaxTree.getRoot(),"")
       compiltaion =  Compiltaion(syntaxTree) if previous is None else previous.ContinueWith(syntaxTree)
       result = None
       result = compiltaion.evaluate(variables)


       if result.getDiagnostics() != [] :
           text = syntaxTree.getText()

           for diagnostic in result.getDiagnostics() :
                        
                               lineIndex = text.getLineIndex(int(diagnostic.getSpan().getStart()))
                               lineIndex = syntaxTree.getText().getLineIndex(diagnostic.getSpan().getStart())
                               line = syntaxTree.getText().getLines()[lineIndex]
                               lineNumber = lineIndex + 1
                               character = diagnostic.getSpan().getStart() - line.getStart() + 1

                               print(Fore.RED,end="")
                               print(f"({lineNumber}, {character}): ",end="")
                               print(diagnostic)
                               print(Style.RESET_ALL,end="")

                               prefixSpan = TextSpan.fromBounds(line.getStart(), diagnostic.getSpan().getStart())
                               suffixSpan = TextSpan.fromBounds(diagnostic.getSpan().getEnd(), line.end())


                               prefix = syntaxTree.getText().ToString_span(prefixSpan)
                               error = syntaxTree.getText().ToString_span(diagnostic.getSpan())
                               suffix = syntaxTree.getText().ToString_span(suffixSpan)

                               print("    ",end="")
                               print(prefix,end="")

                               print(Fore.RED,end="")
                               print(error,end="")
                               print(Style.RESET_ALL,end="")

                               print(suffix,end="")

                               print("")

       else :     
           syntaxTree.getRoot().WriteTo(print)
           print(result.getValue())
           previous = compiltaion

    
       if result.getDiagnostics() == [] :
               initCompiler("cCode.c")               
               compile(syntaxTree.getRoot(),"cCode.c")
               endCompiler("cCode.c")

   # variableDeclaration.append(self.MatchToken(Tokens.IdentifierToken))
        # while True :
        #     if self.current().getType() == Tokens.CommaToken:
        #         self.MatchToken(Tokens.CommaToken)
        #         variableDeclaration.append(self.MatchToken(Tokens.IdentifierToken))
        #         print(self.current().getType())
        #     else :
        #         break

        # for item in variableDeclaration :
        #     print(item.getText())