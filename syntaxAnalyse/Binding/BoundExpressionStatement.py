






from Binding.BoundNodeType import BoundNodeType
from Binding.BoundStatement import BoundStatement

class BoundExpressionStatement(BoundStatement):

    def __init__(self,expression) -> None:
        self.expression = expression

    def getExpression(self):
        return self.expression
    

    def getType(self):
        return BoundNodeType.ExpressionStatement