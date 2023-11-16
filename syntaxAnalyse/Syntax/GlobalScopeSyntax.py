


from StatementSyntax import StatementSyntax
from Tokens import Tokens


class GlobalScopeSyntax(StatementSyntax):
    def __init__(self,statments) -> None:
        self.statments = statments

    def getStatements(self):
        return self.statments

    def getType(self):
        return Tokens.BlockStatement