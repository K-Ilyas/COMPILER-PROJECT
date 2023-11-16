

from Binding.BoundNodeType import BoundNodeType
from Binding.BoundStatement import BoundStatement


class BoundWriteFunction(BoundStatement) :

    def __init__(self,primaryExpressions) -> None:
        self.primaryExpressions = primaryExpressions

    def getPrimaryExpressions(self):
        return self.primaryExpressions
    

    def getType(self):
        return BoundNodeType.WriteFunction