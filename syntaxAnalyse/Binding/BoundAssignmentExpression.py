



from Binding.BoundExpression import BoundExpression
from Binding.BoundNodeType import BoundNodeType


class BoundAssignmentExpression(BoundExpression):


    def __init__(self,variable,expression) -> None:
        self.variable = variable 
        self.expression = expression 

    
    def getVariable(self):
        return self.variable
    
    
    def getExpression(self):
        return self.expression
    
    def type(self):
        return self.expression.type()

    def getType(self):
        return BoundNodeType.AssignmentExpression