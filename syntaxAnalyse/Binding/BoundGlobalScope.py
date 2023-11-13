



class BoundGlobalScope:
    def __init__(self,previous,diagnostics,variables,statement) -> None:
        self.previous = previous
        self.diagnostics= diagnostics
        self.variables = variables 
        self.statement = statement


    def getPrevious(self):
        return self.previous
    
    def getDiagnostics(self):
        return self.diagnostics
    
    def getVariables(self):
        return self.variables
    
    def getStatement(self):
        return self.statement
