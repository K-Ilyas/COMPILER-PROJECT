



from StatementSyntax import StatementSyntax
from Tokens import Tokens


class ForStatementSyntax(StatementSyntax):

    def __init__(self,forKeyword,identifier,equalsToken,lowerBound,toKeyword,upperBound,body) -> None:
        self.forKeyword = forKeyword
        self.identifier = identifier
        self.equalsToken = equalsToken
        self.lowerBound = lowerBound
        self.toKeyword = toKeyword
        self.upperBound = upperBound
        self.body = body

    def getForKeyword(self):
        return self.forKeyword
    
    def getIdentifier(self):
        return self.identifier
    
    def getEqualsToken(self):
        return self.equalsToken 
    
    def getLowerBound(self):
        return self.lowerBound
    
    def getToKeyword(self):
        return self.toKeyword
    
    def getUpperBound(self):
        return self.upperBound
    
    
    def getBody(self):
        return self.body
    
    def getType(self):
        return Tokens.ForStatement
    