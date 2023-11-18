






from StatementSyntax import StatementSyntax
from Tokens import Tokens


class ReadFunctionSyntax(StatementSyntax):

    def __init__(self,readKeyword,openParenthesisToken,assignmentExpressions,closeParenthesisToken,semiColonToken) -> None:
        self.readKeyword =readKeyword
        self.openParenthesisToken = openParenthesisToken
        self.assignmentExpressions = assignmentExpressions
        self.closeParenthesisToken = closeParenthesisToken
        self.semiColonToken = semiColonToken
    
    def getReadKeyword(self):
        return self.readKeyword
    
    def getOpenParenthesisToken(self):
        return self.openParenthesisToken

    def getAssignmentExpressions(self):
        return self.assignmentExpressions
    
    def getCloseParenthesisToken(self):
        return self.closeParenthesisToken
    
    
    def getSemiColonToken(self):
        return self.semiColonToken
    
    def getType(self):
        return Tokens.ReadFunction
    