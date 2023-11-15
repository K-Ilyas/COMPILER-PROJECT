

from Binding.BoundNodeType import BoundNodeType
from Binding.BoundStatement import BoundStatement


class BoundWhileStatement(BoundStatement) :

    def __init__(self,condition,body) -> None:
        self.condition = condition
        self.body = body 

    def getCondition(self):
        return self.condition
    
    def getBody(self):
        return self.body
    
    def getType(self):
        return BoundNodeType.WhileStatement