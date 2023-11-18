

from Binding.BoundNodeType import BoundNodeType
from Binding.BoundStatement import BoundStatement


class BoundReadFunction(BoundStatement) :

    def __init__(self,assignmentExpressions) -> None:
        self.assignmentExpressions = assignmentExpressions

    def getAssignmentExpressions(self):
        return self.assignmentExpressions
    

    def getType(self):
        return BoundNodeType.ReadFunction