
from ExpressionSyntax import ExpressionSyntax
from Tokens import Tokens

# The BinaryExpressionSyntax class represents a binary expression in Python, with a left expression, a
# token, and a right expression.


class BinaryExpressionSyntax(ExpressionSyntax):

        def __init__(self,left,operatorToken,right) -> None:
            self.left = left
            self.operatorToken = operatorToken 
            self.right = right
        
        def getLeft(self):
            return self.left
                   
        def getOperatorToken(self):
            return self.operatorToken 
          
        def getRight(self):
            return self.right

        
        def getType(self):
             return Tokens.BinaryExpression
     
        # def getChildrens(self):
        #    yield self.left 
        #    yield self.operatorToken
        #    yield self.right
