import sys,gc
from colorama import Fore, Back, Style


import os, subprocess
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(0, ROOT_DIR+'/syntaxAnalyse')
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
        out.write("#include <stdlib.h>\n")
        out.write("int main(){\n")

def endCompiler(output_file):
    with open(output_file,"a") as out:
        out.write("return 0;\n}\n")

def getSibling(nodeParent: SyntaxToken):
    return [(e.getType(), e) for e in nodeParent.getChildrens()] if nodeParent != None else None


def getAllChildren(node):
    if isinstance(node, SyntaxToken):
        return [node]

    result = []
    for nodeChild in node.getChildrens():
        result.extend(getAllChildren(nodeChild))

    return result
variables = {
    "int" : [],
    "char*": []
}
def compile(child, output_file, parent=None, grandparent=None):
    global variables
    if isinstance(child, SyntaxToken):
        with open(output_file, "a") as out:
            match child.getType():
                case Tokens.BlockStatement:
                    out.write("\n")
                case Tokens.SemiColonToken:
                    out.write(";\n")
                case Tokens.OpenBraceToken:
                    out.write("{\n")
                case Tokens.VarKeyword:
                    variable = [e[1] for e in getSibling(parent) if e[0] == Tokens.IdentifierToken][0]
                    if Tokens.NumberToken in [a.getType() for a in getAllChildren(parent)]:
                        out.write("int "+str(variable.getText())+"=")
                        variables['int'].append(variable.getText()) 
                    else : 
                        out.write("char* "+str(variable.getText())+"=")
                        variables['char*'].append(variable.getText())
                # case Tokens.IdentifierToken:
                #     if grandparent.getType() not in {Tokens.WriteFunction, Tokens.ReadFunction, Tokens.VariableDeclaration}:
                #         out.write(str(child.getText()))
                case Tokens.EqualsToken:
                    if parent.getType() != Tokens.VariableDeclaration:
                        out.write("=")
                case Tokens.NumberToken:
                    if grandparent.getType() not in {Tokens.WriteFunction, Tokens.ReadFunction}:
                        out.write(str(child.getValue()))
                case Tokens.TrueKeyword:
                    out.write("1")
                case Tokens.FalseKeyword:
                    out.write("0")
                case Tokens.CloseBraceToken:
                    out.write("}\n")
                case Tokens.IfKeyword:
                    out.write("if(")
                case Tokens.WhileKeyword:
                    out.write("while(")
                case Tokens.DoKeyword:
                    out.write(")")
                case Tokens.ElseKeyword:
                    out.write("else")
                case Tokens.ThenKeyword:
                    out.write(")")
                case Tokens.GreatToken:
                    out.write(">")
                case Tokens.LessToken:
                    out.write("<")
                case Tokens.LessOrEqualsToken:
                    out.write("<=")
                case Tokens.GreatOrEqualsToken:
                    out.write(">=")
                case Tokens.PlusToken:
                    out.write("+")
                case Tokens.MinusToken:
                    out.write("-")
                case Tokens.DoubleQuteToken:
                    out.write('"')
                case Tokens.SlashToken:
                    out.write("/")
                case Tokens.AmpersandAmpersandToken:
                    out.write("&&")
                case Tokens.BadToken:
                    out.write("!")
                case Tokens.PipePipeToken:
                    out.write("||")
                case Tokens.EqualsEqualsToken:
                    out.write("==")
                case Tokens.BangEqualsToken:
                    out.write("<>")
                case Tokens.StarToken:
                    out.write("*")
                case Tokens.OpenParenthesisToken:
                    if grandparent.getType() in {Tokens.WriteFunction, Tokens.ReadFunction}:                        out.write("(")
                case Tokens.CloseParenthesisToken:
                    if grandparent.getType() in {Tokens.WriteFunction, Tokens.ReadFunction}:                        out.write(")")
                case Tokens.WriteKeyword:
                    AllChildren = getAllChildren(parent)
                    # print([a.getText() for a in AllChildren if a.getType() == Tokens.IdentifierToken])
                    pattern = ""
                    varName = []
                    for node in AllChildren:
                        if node.getType() == Tokens.WriteKeyword:
                            out.write("printf(")
                        elif node.getType() == Tokens.NumberToken:
                            varName.append((str(node.getValue())))
                            pattern += "%d"
                        elif node.getType() == Tokens.StringToken:
                            varName.append('"'+str(node.getValue().replace("\n", "\\n"))+'"')
                            pattern += "%s"
                        elif node.getType() == Tokens.IdentifierToken:
                            varName.append(str(node.getText()))
                            if node.getText() in variables['int']: pattern += "%d"
                            else: pattern += "%s"
                        
                    out.write('"'+pattern+'",')
                    out.write(','.join(map(str,varName)))
                    out.write(")")

                case Tokens.ReadKeyword:
                    AllChildren = getAllChildren(parent)
                    # print([a.getText() for a in AllChildren if a.getType() == Tokens.IdentifierToken])
                    pattern = ""
                    varName = []
                    for node in AllChildren:
                        if node.getType() == Tokens.ReadKeyword:
                            out.write("scanf(")
                        elif node.getType() == Tokens.IdentifierToken:
                            varName.append(str(node.getText()))
                            if node.getText() in variables['int']: pattern += "%d"
                            else: pattern += "%s"
                        
                    out.write('"'+pattern+'",&')
                    out.write(',&'.join(map(str,varName)))
                    out.write(")")
                      
                case Tokens.StringToken:
                    if grandparent.getType() not in {Tokens.WriteFunction, Tokens.ReadFunction}:
                        out.write('"' + str(child.getValue().replace("\n", "\\n")) + '"')
                    
                    

    for child2 in child.getChildrens():
        compile(child2, output_file, child, parent)

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




# previous = None
def Final(file_path, output, flag):

    # with open(file_path, "r") as f:
    text_file = open(file_path, "r")
    textBuilder = text_file.read()
    text_file.close()

    syntaxTree = SyntaxTree.Parse(textBuilder)

    # printResultAsTree(syntaxTree.getRoot(),"")
    # compiltaion =  Compiltaion(syntaxTree) if previous is None else previous.ContinueWith(syntaxTree)
    compiltaion =  Compiltaion(syntaxTree)
    
    result = None
    if flag == '-s':
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
       

        
    if flag == '-c':
            initCompiler(output)               
            compile(syntaxTree.getRoot(),output)
            endCompiler(output)


def usage(program_name):
    print(f"Usage: {program_name} <FLAG> <ARGS>")
    print("FLAGS : ")
    print("    -s    Simulate the program")
    print("    -c    Compile the program")

def call_cmd(cmd):
    print(" ".join(cmd))
    subprocess.call(cmd)

def uncons(xs):
    return (xs[0], xs[1:])

if __name__ == "__main__":
    argv = sys.argv
    assert len(argv) >= 1
    (program_name, argv) = uncons(argv)
    if len(argv) < 1:
        usage(program_name)
        print("Error flag must be set")
        exit(1)
    
    (flag, argv) = uncons(argv)
    # argv = argv[1:]


    if flag == '-s':
        if len(argv) < 1:
            usage(program_name)
            print("Error: no input file provided for the simulation")
            exit(1)
        (input_file_path, argv) = uncons(argv)
        Final(input_file_path, "output.c", '-s')
        # simulate(program, input_file_path)
 
    if flag == '-c':
        (input_file_path, argv) = uncons(argv)
        print(input_file_path)
        Final(input_file_path, "output.c", '-c')
        print("Generate the C program ")
        call_cmd(["gcc", "output.c"])
        # call_cmd(["rm", "output.c"])
        print("Execute the programe")
        call_cmd(["./a.out"])
        # call_cmd(["ld","-o", "output", "output.o"])
        # subprocess.call(["chmod","+x", "output"])
        
    else:
        usage()
        print(f"Unkown flag {flag}")
        exit(1)