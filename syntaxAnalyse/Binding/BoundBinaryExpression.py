


from Binding.BoundExpression import BoundExpression
from Binding.BoundNodeType import BoundNodeType


class BoundBinaryExpression(BoundExpression):


    def __init__(self,left,op,right) -> None:
        self.left = left
        self.right = right
        self.op = op

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getOp(self):
        return self.op
    
    def type(self):
        return self.op.getResultType()
    
    def getType(self):
        return BoundNodeType.BinaryExpression

    