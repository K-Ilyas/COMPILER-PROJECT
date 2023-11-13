
from abc import ABC
from copy import deepcopy
from Lex import Lex
import Parse
from SourceText import SourceText
from Tokens import Tokens

# The SyntaxTree class represents a syntax tree and provides methods for accessing its root, errors,
# and end file token, as well as a static method for parsing a given text.

class SyntaxTree(ABC):
    __root = 0
    __errors = None

    def __init__(self,text) :
        parser = Parse.Parse(text)
        root = parser.ParseCompilationUnit()
        errors = parser.getErrors()
        self.__text = text
        self.__root = root

        if self.__errors is None :
            self.__errors = []

        self.__errors = deepcopy(errors)

    def getErrors(self):
        return self.__errors
    def getText(self):
        return self.__text
    def getRoot(self):
        return self.__root
    
    @staticmethod
    def Parse(text:str):
        sourceText = SourceText.From(text)
        return SyntaxTree.Parse_(sourceText)
    
    @staticmethod
    def Parse_(text:SourceText):
        return SyntaxTree(text)
    
    @staticmethod
    def ParseTokens(text:str):
       sourceText = SourceText.From(text)
       return SyntaxTree.ParseTokens_(sourceText)
    
    @staticmethod
    def ParseTokens_(text:SourceText):
        lex = Lex(text)
        while True :
            token = lex.NextToken()

            if token.getType() == Tokens.EndOfFileToken:
                break
            
            yield token 
