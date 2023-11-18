


from VariableSymbol import VariableSymbole


class BoundScope:

    _variables = None

    def __init__(self,parent) -> None:
        self._variables = dict()
        self.parent = parent

    
    def getParent(self):
        return self.parent

    def tryDeclare(self,variable):

        if variable.getName() in self._variables.keys() :
            return False
        
        self._variables[variable.getName()] = variable
        return True
    


    def tryLookUp(self,name):
        if name in self._variables.keys():
           return (True,self._variables[name])

        if self.parent is None:
           return (False,None)
        return self.parent.tryLookUp(name)

    def getDeclaredVariables(self):
        return self._variables.values()

