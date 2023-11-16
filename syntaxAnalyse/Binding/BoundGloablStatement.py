



from Binding.BoundNodeType import BoundNodeType
from Binding.BoundStatement import BoundStatement

class BoundGloablStatement(BoundStatement):

    def __init__(self,statements) -> None:
        self.statements = statements

    def getStatements(self):
        return self.statements

    def getType(self):
        return BoundNodeType.GlobalScope