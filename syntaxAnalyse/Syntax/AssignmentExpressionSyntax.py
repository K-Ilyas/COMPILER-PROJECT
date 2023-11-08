
from ExpressionSyntax import ExpressionSyntax
from Tokens import Tokens

# The BinaryExpressionSyntax class represents a binary expression in Python, with a left expression, a
# token, and a right expression.

class AssignmentExpressionSyntax(ExpressionSyntax):

        def __init__(self,identifierToken,equalsToken,expression) -> None:
            
            self.identifierToken = identifierToken
            self.equalsToken = equalsToken
            self.expression = expression
          #   self.data = {identifierToken : self.identifierToken,equalsToken :self.equalsToken,expression :self.expression }
        
        
        def getIdentifierToken(self):
            return self.identifierToken
          
        def getEqualsToken(self):
             return self.equalsToken
        
        def getExpression(self):
             return self.expression
        
        def getType(self):
             return Tokens.AssignmentExpression
        
 
             

        