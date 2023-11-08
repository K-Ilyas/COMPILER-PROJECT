



from Binding.BoundExpression import BoundExpression
from Binding.BoundNodeType import BoundNodeType


class BoundVariableExpression(BoundExpression):


    def __init__(self,variable) -> None:
        self.variable = variable 

    
    def getVariable(self):
        return self.variable
    
    def type(self):
        return self.variable.type()
    

    def getType(self):
        return BoundNodeType.VariableExpression