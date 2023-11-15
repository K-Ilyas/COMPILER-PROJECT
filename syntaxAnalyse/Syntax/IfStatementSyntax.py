


from StatementSyntax import StatementSyntax
from Tokens import Tokens


class IfStatementSyntax(StatementSyntax):
    
    def __init__(self,ifKeyword,condition,thenKeyword,thenStatement,elseClauseSyntax) -> None:
        self.ifKeyword =ifKeyword
        self.condition = condition
        self.thenKeyword = thenKeyword
        self.thenStatement = thenStatement
        self.elseClauseSyntax = elseClauseSyntax
      

    
    def getIfKeyword(self):
        return self.ifKeyword
    
    def getCondition(self):
        return self.condition
    def getThenStatement(self):
        return self.thenStatement
    def getThenKeyword(self):
        return self.thenKeyword
    def getElseClauseSyntax(self):
        return self.elseClauseSyntax
    
    def getType(self) :
        return Tokens.IfStatement
    
   
    

    
