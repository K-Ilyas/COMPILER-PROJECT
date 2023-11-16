

from Binding.BoundExpression import BoundExpression
from Binding.BoundNodeType import BoundNodeType


class BoundLiteralExpression(BoundExpression):


    def __init__(self,value) -> None:
        self.value = value

    
    def getValue(self):
        return self.value
    
    def type(self):
        return  self.value.type() if type(self.value) != int and type(self.value) != bool and type(self.value) != str else type(self.value) 
    
    def getType(self):
        return BoundNodeType.LiteralExpression