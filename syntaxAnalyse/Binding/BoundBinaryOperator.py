
from Binding.BoundBinaryOperatorType import BoundBinaryOperatorType
import sys

import os
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(0, ROOT_DIR+'/syntaxAnalyse/Syntax')
from Tokens import Tokens


class BoundBinaryOperator():

    def __init__(self, syntaxType, type, ty, leftType=None, rightType=None, resultType=None) -> None:
        self.syntaxType = syntaxType
        self.type = type
        self.ty = ty
        self.leftType = leftType if leftType is not None else ty
        self.rightType = rightType if rightType is not None else ty
        self.resultType = resultType if resultType is not None else ty

    def getSyntaxType(self):
        return self.syntaxType

    def getType(self):
        return self.type

    def getLeftType(self):
        return self.leftType

    def getRightType(self):
        return self.rightType

    def getTy(self):
        return self.ty

    def getResultType(self):
        return self.resultType

    @staticmethod
    def getBinaryOperators():

        return [
            BoundBinaryOperator(
                Tokens.PlusToken, BoundBinaryOperatorType.Addition, int),
            BoundBinaryOperator(
                Tokens.PlusToken, BoundBinaryOperatorType.StringConcatenation, str),
            BoundBinaryOperator(
                Tokens.MinusToken, BoundBinaryOperatorType.Substraction, int),
            BoundBinaryOperator(
                Tokens.SlashToken, BoundBinaryOperatorType.Division, int),
            BoundBinaryOperator(
                Tokens.StarToken, BoundBinaryOperatorType.Multiplication, int),
            
            BoundBinaryOperator(
                Tokens.EqualsEqualsToken, BoundBinaryOperatorType.Equals, int, int, int, bool),
            BoundBinaryOperator(
                Tokens.LessToken, BoundBinaryOperatorType.Less, int, int, int, bool),
            BoundBinaryOperator(
                Tokens.GreatToken, BoundBinaryOperatorType.Greater, int, int, int, bool),
            BoundBinaryOperator(
                Tokens.GreatOrEqualsToken, BoundBinaryOperatorType.GreaterOrEquals, int, int, int, bool),
            BoundBinaryOperator(
                Tokens.LessOrEqualsToken, BoundBinaryOperatorType.LessOrEquals, int, int, int, bool),
            BoundBinaryOperator(
                Tokens.BangEqualsToken, BoundBinaryOperatorType.NotEquals, int, int, int, bool),
            BoundBinaryOperator(
                Tokens.AmpersandAmpersandToken, BoundBinaryOperatorType.LogicalAnd, bool),
            BoundBinaryOperator(
                Tokens.PipePipeToken, BoundBinaryOperatorType.LogicalOr, bool),
             BoundBinaryOperator(
                Tokens.AmpersandAmpersandToken, BoundBinaryOperatorType.LogicalAnd, int),
            BoundBinaryOperator(
                Tokens.PipePipeToken, BoundBinaryOperatorType.LogicalOr, int),

            BoundBinaryOperator(
                Tokens.EqualsEqualsToken, BoundBinaryOperatorType.Equals, bool),
            BoundBinaryOperator(
                Tokens.BangEqualsToken, BoundBinaryOperatorType.NotEquals, bool),
        ]

    @staticmethod
    def bind(syntaxType, leftType, rightType):
        for op in BoundBinaryOperator.getBinaryOperators():
            if op.getSyntaxType() == syntaxType and op.getLeftType() == leftType and op.getRightType() == rightType:
                return op

        return None
