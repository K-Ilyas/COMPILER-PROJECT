

from ExpressionSyntax import ExpressionSyntax
from Tokens import Tokens


# The `NumberExpressionSyntax` class represents a syntax node for a number expression in a programming
# language.


class LiteralExpressionSyntax(ExpressionSyntax):

    def __init__(self, literalToken, value=None) -> None:
        self.literalToken = literalToken
        self.value = value if value is not None else literalToken.getValue()



    def getLiteralToken(self):
        return self.literalToken

    # def getValue(self):
    #     return self.literalToken.getValue()

    def getValue(self):
        return self.value
    
    def getType(self):
        return Tokens.LiteralExpression
    # def getChildrens(self):
    #     yield self.literalToken


