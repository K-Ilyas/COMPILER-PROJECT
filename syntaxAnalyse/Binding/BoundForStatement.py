

from Binding.BoundNodeType import BoundNodeType
from Binding.BoundStatement import BoundStatement


class BoundForStatement(BoundStatement) :

    def __init__(self,variable,lowerBound,upperBound,body) -> None:
        self.variable = variable
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.body = body

    def getVariable(self):
        return self.variable
    
    def getLowerBound(self):
        return self.lowerBound
    
    def getUpperBound(self):
        return self.upperBound
    
    def getBody(self):
        return self.body
    
    def getType(self):
        return BoundNodeType.ForStatement