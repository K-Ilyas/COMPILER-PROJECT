


class VariableSymbole:

    def __init__(self,name,isReadOnly,typ) -> None:
        self.name = name 
        self.typ = typ
        self.isReadOnly = isReadOnly

    def getName(self):
        return self.name 
    def getIsReadOnly(self):
        return self.isReadOnly
    def type(self):
        return self.typ