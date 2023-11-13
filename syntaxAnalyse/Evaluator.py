
from Binding.BoundAssignmentExpression import BoundAssignmentExpression
from Binding.BoundBlockStatement import BoundBlockStatement
from Binding.BoundExpressionStatement import BoundExpressionStatement
from Binding.BoundNodeType import BoundNodeType
from Binding.BoundVariableDeclaration import BoundVariableDeclaration
from Binding.BoundVariableExpression import BoundVariableExpression
from UnrayExpressionSyntax import UnrayExpressionSyntax
from Tokens import Tokens
from ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from LiteralExpressionSyntax import LiteralExpressionSyntax
from BinaryExpressionSyntax import BinaryExpressionSyntax
import sys
from Binding.BoundBinaryExpression import BoundBinaryExpression
from Binding.BoundBinaryOperatorType import BoundBinaryOperatorType

from Binding.BoundLiteralExpression import BoundLiteralExpression
from Binding.BoundUnrayExpression import BoundUnrayExpression
from Binding.BoundUnrayOperatorType import BoundUnrayOperatorType
sys.path.insert(0, 'C:/Users/ilyas/Documents/compiler/syntaxAnalyse/Syntax')


# The `Evaluator` class is used to evaluate mathematical expressions represented by a syntax tree.


class Evaluator:
    __root = 0
    _variables = dict()
    _lastValue = None

    def __init__(self, root,variables) -> None:
        self.__root = root
        self._variables = variables

    def getRoot(self):
        return self.__root
    
    def geTvariables(self):
        return self._variables

    def result(self):
        self.EvaluateStatement(self.__root)
        return self._lastValue
    

    def EvaluateStatement(self, node):
     match node.getType():
        case BoundNodeType.BlockStatement:
            node.__class__ = BoundBlockStatement
            self.EvaluteBlockStatement(node)
        case BoundNodeType.VariableDeclaration:
            node.__class__ = BoundVariableDeclaration
            self.EvaluteDeclaration(node)
        case BoundNodeType.ExpressionStatement:
            node.__class__ = BoundExpressionStatement
            self.EvaluteExpressionStatement(node)
        case _:        
          raise Exception("Unexpected node {node}".format(node=node.getType()))
    
    def EvaluteBlockStatement(self,node):
        for statement in node.getStatements():
            self.EvaluateStatement(statement)

    def EvaluteDeclaration(self,node):
        value = self.ExpressionResult(node.getIntializer())
        self._variables[node.getVariable()] = value
        self._lastValue = value
    def EvaluteExpressionStatement(self,node):
        self._lastValue = self.ExpressionResult(node.getExpression())
    def ExpressionResult(self, r):
        
     match r.getType():
        case BoundNodeType.LiteralExpression:
            r.__class__ = BoundLiteralExpression
            return self.EvaluateLiteralExpression(r)
        
        case BoundNodeType.VariableExpression :
            r.__class__ = BoundVariableExpression
            return self.EvaluateVariableExpression(r)
        
            
        case BoundNodeType.AssignmentExpression:
            r.__class__ = BoundAssignmentExpression
            return self.EvaluateAssignmentExpression(r)

        case BoundNodeType.UnrayExpression:
            r.__class__ = BoundUnrayExpression
            return self.EvaluateUnaryExpression(r)

        case BoundNodeType.BinaryExpression:
            r.__class__ = BoundBinaryExpression
            return self.EvaluateBinaryExpression(r)
        case _:        
          raise Exception("Unexpected node {node}".format(node=r.getType()))



    def EvaluateLiteralExpression(self,a):
            return a.getValue()
        
    def EvaluateVariableExpression(self,v):
            return self._variables[v.getVariable()]
        
    def EvaluateAssignmentExpression(self,a) :
            value = self.ExpressionResult(a.getExpression())
            self._variables[a.getVariable()] = value
            return value
    def EvaluateUnaryExpression(self,u):
            operand = self.ExpressionResult(u.getOperand())
            if u.getOp().getType() == BoundUnrayOperatorType.Identity:
                return int(operand)
            elif u.getOp().getType() == BoundUnrayOperatorType.Negation:
                return - int(operand)
            elif u.getOp().getType() == BoundUnrayOperatorType.LogicalNegation:
                return not bool(operand)
            else:
                raise Exception(
                    "Unexpected Binary operator {op}".format(op=u.getOp()))
            
    def EvaluateBinaryExpression(self,b):

            left = self.ExpressionResult(b.getLeft())
            right = self.ExpressionResult(b.getRight())
            
            match b.getOp().getType():
                case BoundBinaryOperatorType.Addition:
                    return int(left) + int(right)
                case BoundBinaryOperatorType.Substraction:
                    return int(left) - int(right)
                case BoundBinaryOperatorType.Multiplication:
                    return int(left) * int(right)
                case BoundBinaryOperatorType.Division:
                    if int(right) == 0 or int(left) == 0:
                        raise Exception("Cannot devide by 0")
                    return int(left) / int(right)
                case BoundBinaryOperatorType.LogicalAnd:                 
                    return bool(left) and bool(right)
                case BoundBinaryOperatorType.LogicalOr:
                    return bool(left) or bool(right)
                case BoundBinaryOperatorType.Equals:
                    return left == right
                case  BoundBinaryOperatorType.NotEquals:
                    return left != right
                case _:
                    raise Exception(
                        "Unexpected Binary operator {token}".format(token=b.getOp()))


