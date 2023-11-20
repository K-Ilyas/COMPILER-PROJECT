
from ExpressionSyntax import ExpressionSyntax
from Tokens import Tokens

# The BinaryExpressionSyntax class represents a binary expression in Python, with a left expression, a
# token, and a right expression.


class NameExpressionSyntax(ExpressionSyntax):

        def __init__(self,identifierToken) -> None:
            self.identifierToken = identifierToken
        
        def getIdentifierToken(self):
            return self.identifierToken
        
        def getType(self):
             return Tokens.NameExpression
        
  