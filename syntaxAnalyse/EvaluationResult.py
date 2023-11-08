

class EvaluationResult:


    def __init__(self,diagnostics,value) -> None:
        self.diagnostics =diagnostics
        self.value = value

    
    def getValue(self):
        return self.value
    
    def getDiagnostics(self):
        return self.diagnostics