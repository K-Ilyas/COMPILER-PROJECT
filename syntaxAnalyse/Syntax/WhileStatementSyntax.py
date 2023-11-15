



from StatementSyntax import StatementSyntax
from Tokens import Tokens


class WhileStatementSyntax(StatementSyntax):

    def __init__(self,keyword,condition,doKeyword,body) -> None:
        self.keyword = keyword
        self.condition = condition
        self.doKeyword = doKeyword
        self.body = body


    def getKeyword(self):
        return self.keyword
    
    def getCondition(self):
        return self.condition
    
    def getDoKeyword(self):
        return self.doKeyword
    
    def getBody(self):
        return self.body
    
    def getType(self):
        return Tokens.WhileStatement
    