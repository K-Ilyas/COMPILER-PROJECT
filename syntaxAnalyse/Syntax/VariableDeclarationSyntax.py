

from StatementSyntax import StatementSyntax
from Tokens import Tokens


class VariableDeclarationSyntax(StatementSyntax):

    def __init__(self,keyword,identifier,equalsToken,intializer) -> None:
        self.keyword = keyword
        self.identifier = identifier
        self.equalsToken = equalsToken 
        self.intializer = intializer

    def getKeyword(self):
        return self.keyword
    
    def getIdentifier(self):
        return self.identifier
    
    def getEqualsToken(self):
        return self.equalsToken
    def getIntializer(self):
        return self.intializer

    def getType(self):
        return Tokens.VariableDeclaration

    