



from Binding.BoundNodeType import BoundNodeType
from Binding.BoundStatement import BoundStatement


class BoundVariableDeclaration(BoundStatement):

    def __init__(self,variable,intializer) -> None:
       self.variable = variable
       self.intializer = intializer

    
    def getVariable(self):
        return self.variable
    
    def getIntializer(self):
        return self.intializer
    
    def getType(self):
        return BoundNodeType.VariableDeclaration
