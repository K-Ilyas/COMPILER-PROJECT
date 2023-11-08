


from Diagnostic import Diagnostic
from copy import deepcopy
import sys
sys.path.insert(0, 'C:/Users/ilyas/Documents/compiler/syntaxAnalyse/Text')

from TextSpan import TextSpan


class DiagnosticBag:

    _diagnostics = []

    def __init__(self) -> None:
        self._diagnostics = []
    
    def Report(self,span,message):
        self._diagnostics.append(Diagnostic(span,message))

    def ReportInvalidInt32(self,span,text,type):
        message = "The number {} isn't a valid {}".format(text,type)
        self.Report(span,message)

    def ReportBadCharacter(self,position,character):
        message = "Error : bad character input : {}".format(character)
        self.Report(TextSpan(position,1),message)
    

    def AddErrors(self,otherDiagnostics):
        self._diagnostics = deepcopy(otherDiagnostics.getDiagnostics())


    
    def ReportUndefinedUnrayOperator(self,span,operatorText,operandType):
            message = "Unary operator '{}' is not defined for type {}.".format(operatorText,operandType)

            self.Report(span,message)

    def ReportUndefinedBinaryOperator(self,span,operatorText,leftType,rightType):
          message = "Binary operator {} is not defined for types {} and {}.".format(operatorText,leftType,rightType)
          self.Report(span,message)
    

    def ReportUndefinedName(self,span,name):
         
         message = "Variable {} dosen't exist".format(name)
         self.Report(span,message)
         
    def ReportUnexpectedToken(self,span,actuelType,expectedType):
        message = "Error : Unexptected Token {} expected {}".format(actuelType,expectedType)
        self.Report(span,message)
    def getDiagnostics(self):
        return self._diagnostics
    
    