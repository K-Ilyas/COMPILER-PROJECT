
from ExpressionSyntax import ExpressionSyntax
from Tokens import Tokens

# The BinaryExpressionSyntax class represents a binary expression in Python, with a left expression, a
# token, and a right expression.


class UnrayExpressionSyntax(ExpressionSyntax):

        def __init__(self,operatorToken,operand) -> None:
            self.operatorToken = operatorToken
            self.operand = operand 

        def getOperatorToken(self):
            return self.operatorToken
        
        def getOperand(self):
            return self.operand
      
        
        def getType(self):
            return Tokens.UnrayExpression
        
        # def getChildrens(self):
        #    yield self.operatorToken 
        #    yield self.operand
