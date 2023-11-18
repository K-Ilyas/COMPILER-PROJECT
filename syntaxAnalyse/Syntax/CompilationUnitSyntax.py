from ExpressionSyntax import ExpressionSyntax
from Tokens import Tokens

# The BinaryExpressionSyntax class represents a binary expression in Python, with a left expression, a
# token, and a right expression.


class CompilationUnitSyntax(ExpressionSyntax):

        def __init__(self,programToken,NameProgramToken,semiColonToken,statement,endFileToken) -> None:
            self.programToken = programToken
            self.NameProgramToken = NameProgramToken
            self.semiColonToken = semiColonToken
            self.statement =statement
            self.endFileToken = endFileToken
      
        def getStatement(self):
         return self.statement
        
        def getProgramToken(self):
            return self.programToken
        def getEndFileToken(self):
         return self.__endFileToken

        def getType(self):
             return Tokens.CompilationUnit