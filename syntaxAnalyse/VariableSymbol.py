


class VariableSymbole:

    def __init__(self,name,isReadOnly,typ,firstAssign=True) -> None:
        self.name = name 
        self.typ = typ
        self.isReadOnly = isReadOnly
        self.firstAssign = firstAssign

    def getName(self):
        return self.name 
    def getIsReadOnly(self):
        return self.isReadOnly
    def getFirstAssign(self):
        return self.firstAssign
    def type(self):
        return self.typ