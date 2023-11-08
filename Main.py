

# This is just for a test purposes : 

# lex = Lex("1233+2-3/3")

# while True :

#     next = lex.NextToken()

#     if next.getType() == Tokens.EndOfFileToken : break

#     print(next.getType(),next.getPos(),next.getText(),next.getValue())

import sys

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
variables[VariableSymbole("a",int)] =12
variables[VariableSymbole("b",bool)] = True

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

syntaxTree = None
textBuilder = ""
syntaxTree = None
while True :
     line = input(" : ")

     if line.strip() == "#":
          break
     else :
          textBuilder += line + '\n'
          
    
     
syntaxTree = SyntaxTree.Parse(textBuilder)

 # printResultAsTree(syntaxTree.getRoot(),"")
compiltaion = None
compiltaion = Compiltaion(syntaxTree)

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


                        # print("")

                        # print(Fore.RED,end="")
                        # print(diagnostic)
                        # print(Style.RESET_ALL,end="")

                        
                        # prefix = line[0:diagnostic.getSpan().getStart()]
                        # error = line[diagnostic.getSpan().getStart():diagnostic.getSpan().getStart()+diagnostic.getSpan().getLength()]
                        # suffix = line[diagnostic.getSpan().getEnd():]

                        # print("    ",end="")
                        # print(prefix,end="")
                        # print(Fore.RED + error,end="")
                        # print(Style.RESET_ALL,end="")

                        # print(suffix,end="")

                        # print("")

else :
    print(result.getValue())
    syntaxTree.getRoot().WriteTo(print)


if result.getDiagnostics() == [] :
        printCode(syntaxTree.getRoot())
        pyFile = open("pyCode.py","w")
        pyFile.write("print("+pyCode+")")

#  print(pyCode)
