from ExpressionSyntax import ExpressionSyntax
from Tokens import Tokens

# The BinaryExpressionSyntax class represents a binary expression in Python, with a left expression, a
# token, and a right expression.


class CompilationUnitSyntax(ExpressionSyntax):

        def __init__(self,expression,endFileToken) -> None:
            self.expression =expression
            self.endFileToken = endFileToken
      
        def getExpression(self):
         return self.expression
    
        def getEndFileToken(self):
         return self.__endFileToken
    

        
        def getType(self):
             return Tokens.CompilationUnit