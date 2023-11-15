

from SyntaxNode import SyntaxNode
from Tokens import Tokens


class ElseClauseSyntax(SyntaxNode):
    
    def __init__(self,elseKeyword,elseStatement)-> None:
        self.elseKeyword = elseKeyword
        self.elseStatement = elseStatement
    
    
    def getElseKeyword(self):
        return self.elseKeyword
    
    def getElseStatement(self):
        return self.elseStatement
    

    def getType(self):
        return Tokens.ElseClause