


from Binding.BoundNodeType import BoundNodeType
from Binding.BoundStatement import BoundStatement


class BoundIfStatement(BoundStatement) :
    def __init__(self,condition,statement,elseStatement) -> None:
        self.condition = condition
        self.statement = statement
        self.elseStatement = elseStatement

    
    def getCondition(self):
        return self.condition
    
    def getStatement(self):
        return self.statement
    
    def getElseStatement(self):
        return self.elseStatement
    
    def getType(self):
        return BoundNodeType.IfStatement