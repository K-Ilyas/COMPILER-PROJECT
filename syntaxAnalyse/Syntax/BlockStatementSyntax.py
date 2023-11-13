


from StatementSyntax import StatementSyntax
from Tokens import Tokens


class BlockStatementSyntax(StatementSyntax):
    def __init__(self,openBraceToken,statments,closeBraceToken) -> None:
        self.openBraceToken = openBraceToken
        self.statments = statments
        self.closeBraceToken = closeBraceToken

    
    def getOpenBraceToken(self):
        return self.openBraceToken
    
    def getStatments(self):
        return self.statments
    
    def getCloseBraceToken(self):
        return self.closeBraceToken
    
    def getType(self):
        return Tokens.BlockStatement