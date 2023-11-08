


class Diagnostic:

    def __init__(self,span,message) -> None:
        self.span = span
        self.message =message


    def getSpan(self):
        return self.span
    
    def getMessage(self):
        return self.message
    
    def __str__(self) -> str:
        return self.message