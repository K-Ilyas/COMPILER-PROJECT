

from StatementSyntax import StatementSyntax
from Tokens import Tokens


class ExpressionStatementSyntax(StatementSyntax):

    def __init__(self,expression) -> None:
        self.expression = expression
    
    def getExpression(self):
        return self.expression

    def getType(self):
        return Tokens.ExpressionStatement
    