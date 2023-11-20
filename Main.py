#!/usr/bin/env python3

import sys, os

from colorama import Fore, Back, Style

ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(0, ROOT_DIR+'/syntaxAnalyse')
from Compilation import Compiltaion
from Tokens import Tokens
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

# textBuilder = ""
# while True :
#     line = input(" : ")

#     if line.strip() == "#":
#             break
#     else :
#             textBuilder += line + '\n'

     
syntaxTree = SyntaxTree.Parse(open("L3Code.txt").read())

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
        if input("\ndo you want to see the parsing Tree ? [yes/no]  : ").strip().lower() == "yes" :
            
            syntaxTree.getRoot().WriteTo(print)
        result.getValue()
        previous = compiltaion

    