

from Binding.BoundExpression import BoundExpression
from Binding.BoundNodeType import BoundNodeType


class BoundUnrayExpression(BoundExpression):
    def __init__(self,op,operand) -> None:
         self.op = op
         self.operand = operand

    
    def getType(self):
         return BoundNodeType.UnrayExpression   

    def getOp(self):
         return self.op
    
    def getOperand(self):
         return self.operand
    
    def type(self):
         return self.op.getOperandType()