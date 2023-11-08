


from VariableSymbol import VariableSymbole


class BoundScope:

    _variables = dict<str,VariableSymbole>()

    def __init__(self,parent) -> None:
        self.parent = parent

    
    def getParent(self):
        return self.parent

    def tryDeclare(self,variable):
        if variable.getName() in self._variables.keys() :
            return False
        
        self._variables[variable.getName()] = variable
        return True


    def tryLookUp(self,name,variable):
        if name in self._variables.Keys():
           return True

        if self.parent is None:
           return False

        return self.parent.tryLookUp(name, variable)

    def getDeclaredVariables(self):
        return self._variables.values()

