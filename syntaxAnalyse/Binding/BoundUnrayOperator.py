
from Binding.BoundUnrayOperatorType import BoundUnrayOperatorType
import sys, os

ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(0, ROOT_DIR+'/syntaxAnalyse/Syntax')

from Tokens import Tokens


class BoundUnrayOperator():

    def __init__(self, syntaxType, type, operandType, resultType=None) -> None:
        self.syntaxType = syntaxType
        self.type = type
        self.operandType = operandType
        self.resultType = resultType if resultType is not None else None

    def getSyntaxType(self):
        return self.syntaxType

    def getType(self):
        return self.type

    def getOperandType(self):
        return self.operandType

    def getResultType(self):
        return self.resultType

    @staticmethod
    def getUnrayOperators():

        return [
            BoundUnrayOperator(
                Tokens.BangToken, BoundUnrayOperatorType.LogicalNegation, bool),
            BoundUnrayOperator(
                Tokens.PlusToken, BoundUnrayOperatorType.Identity, int),
            BoundUnrayOperator(
                Tokens.MinusToken, BoundUnrayOperatorType.Negation, int),
            
        ]
    
    @staticmethod
    def bind(syntaxType,operandType):
        for op in BoundUnrayOperator.getUnrayOperators():
            if op.getSyntaxType() == syntaxType and op.getOperandType() == operandType :
                return op
            
        return None

