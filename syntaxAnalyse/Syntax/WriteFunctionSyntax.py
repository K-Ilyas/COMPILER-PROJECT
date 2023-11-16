






from StatementSyntax import StatementSyntax
from Tokens import Tokens


class WriteFunctionSyntax(StatementSyntax):

    def __init__(self,writekeyword,openParenthesisToken,primaryExpressions,closeParenthesisToken,semiColonToken) -> None:
        self.writekeyword =writekeyword
        self.openParenthesisToken = openParenthesisToken
        self.primaryExpressions = primaryExpressions
        self.closeParenthesisToken = closeParenthesisToken
        self.semiColonToken = semiColonToken
    
    def getWritekeyword(self):
        return self.writekeyword
    
    def getOpenParenthesisToken(self):
        return self.openParenthesisToken
    
    def getPrimaryExpressions(self):
        return self.primaryExpressions
    
    def getCloseParenthesisToken(self):
        return self.closeParenthesisToken
    
    def getPrimaryExpressions(self):
        return self.primaryExpressions
    
    def getSemiColonToken(self):
        return self.semiColonToken
    
    def getType(self):
        return Tokens.WriteFunction
    