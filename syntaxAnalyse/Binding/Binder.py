
from Binding.BoundAssignmentExpression import BoundAssignmentExpression
from Binding.BoundBinaryExpression import BoundBinaryExpression
from Binding.BoundBinaryOperator import BoundBinaryOperator
from Binding.BoundBinaryOperatorType import BoundBinaryOperatorType
from Binding.BoundLiteralExpression import BoundLiteralExpression
from Binding.BoundUnrayExpression import BoundUnrayExpression
from Binding.BoundUnrayOperator import BoundUnrayOperator
from Binding.BoundUnrayOperatorType import BoundUnrayOperatorType
import sys
from Binding.BoundVariableExpression import BoundVariableExpression

sys.path.insert(0, 'C:/Users/ilyas/Documents/compiler/syntaxAnalyse')

from DiagnosticBag import DiagnosticBag

from VariableSymbol import VariableSymbole

sys.path.insert(0, 'C:/Users/ilyas/Documents/compiler/syntaxAnalyse/Syntax')
from BinaryExpressionSyntax import BinaryExpressionSyntax
from Tokens import Tokens
from LiteralExpressionSyntax import LiteralExpressionSyntax
from UnrayExpressionSyntax import UnrayExpressionSyntax
from ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from NameExpressionSyntax import NameExpressionSyntax
from AssignmentExpressionSyntax import AssignmentExpressionSyntax


class Binder():

    _diagnostics = DiagnosticBag()
    _variables =dict()

    def __init__(self,variables) -> None:
        self._variables = variables
    def BindExpression(self, syntax):

        match(syntax.getType()):  
            case Tokens.ParenthesizedExpressionSyntax :
                syntax.__class__ = ParenthesizedExpressionSyntax
                return self.BindParenthesizedExpression(syntax)
            case Tokens.LiteralExpression:
                syntax.__class__= LiteralExpressionSyntax
                return self.BindLiteralExpression(syntax) 
            case Tokens.NameExpression : 
                syntax.__class__ = NameExpressionSyntax
                return self.BindNameExpression(syntax)   
            case Tokens.AssignmentExpression :
                syntax.__class__ = AssignmentExpressionSyntax
                return self.BindAssignmentExpression(syntax)
            case Tokens.UnrayExpression:
                syntax.__class__ = UnrayExpressionSyntax
                return self.BindUnaryExpression(syntax)
            case Tokens.BinaryExpression:
                syntax.__class__ = BinaryExpressionSyntax
                return self.BindBinaryExpression(syntax)
         
         
            case _:
                raise Exception(
                    "Unexpected syntax {}".format(syntax.getType()))
            

   
    def BindLiteralExpression(self, syntax):

        value = False if syntax.getValue() is None else syntax.getValue()
        return BoundLiteralExpression(value)
    
    def BindNameExpression(self,syntax):
        
        name =  syntax.getIdentifierToken().getText()
        variable = list(filter(lambda v : v.getName() == name,self._variables.keys()))
        
        if len(variable) == 0:
            self._diagnostics.ReportUndefinedName(syntax.getIdentifierToken().getSpan(),name)
            return BoundLiteralExpression(0)
        # self._variables[name].getType() if self._variables[name].getType() == None else object
        return BoundVariableExpression(variable[0])


    def BindAssignmentExpression(self,syntax):
       name =  syntax.getIdentifierToken().getText()
       boundExpression = self.BindExpression(syntax.getExpression())
       existingVariable = self._variables.get(name,None)
       if existingVariable != None :
           del self._variables[variable]
       
        
       variable = VariableSymbole(name,boundExpression.type())
       self._variables[variable] = None
    #    defaultValue = 0 if boundExpression.type() == int else (False if boundExpression.type() == bool else None)

    #    if defaultValue == None :
    #        raise Exception("Unsupported variable type {}".format(boundExpression.getType()))
       
       return BoundAssignmentExpression(variable,boundExpression) 

    def BindUnaryExpression(self, syntax):

        boundOperand = self.BindExpression(syntax.getOperand())
        #     boundOperator = BoundBinaryOperatorType.Bind(syntax.getOperatorToken().getType(), boundOperand.type())
        boundOperator = BoundUnrayOperator.bind(
            syntax.getOperatorToken().getType(), boundOperand.type())
        
        if boundOperator == None:

            self._diagnostics.ReportUndefinedUnrayOperator(syntax.getOperatorToken().getSpan(),syntax.getOperatorToken().getText(),boundOperand.type())
            # self._diagnostics.append(
            #     "Unary operator '{op}' is not defined for type {type}.".format(op=syntax.getOperatorToken().getText(), type=boundOperand.type()))
            return boundOperand

        return BoundUnrayExpression(boundOperator, boundOperand)

    def BindBinaryExpression(self, syntax):


        boundLeft = self.BindExpression(syntax.getLeft())
        boundRight = self.BindExpression(syntax.getRight())

        boundOperator = BoundBinaryOperator.bind(
            syntax.getOperatorToken().getType(), boundLeft.type(), boundRight.type())
        
        # print(boundLeft.getName(),boundRight.getName())

        if boundOperator == None:
            self._diagnostics.ReportUndefinedBinaryOperator(syntax.getOperatorToken().getSpan(),syntax.getOperatorToken().getText(),boundLeft.type(),boundRight.type())

            # self._diagnostics.append("Binary operator {} is not defined for types {} and {}.".format(syntax.getOperatorToken().getType(),
            #                                                                                          boundLeft.type(), boundRight.type()))
            return boundLeft
        

        return BoundBinaryExpression(boundLeft, boundOperator, boundRight)
    

    def BindParenthesizedExpression(self,syntax) :
        return self.BindExpression(syntax.getExpression())
    
  
    # def BindUnrayOperatarType(self, type, operandType):

    #     if operandType == int:
    #         match(type):
    #             case Tokens.PlusToken:
    #                 return BoundUnrayOperatorType.Identity
    #             case Tokens.MinusToken:
    #                 return BoundUnrayOperatorType.Negation
    #             case _:
    #                 raise Exception(
    #                     "Unexpected Unray operator {}".format(type))
        
    #     if operandType == bool :
    #         match(type):
    #             case Tokens.BangToken:
    #                 return BoundUnrayOperatorType.LogicalNegation

    #     return None

    # def BindBinaryOperatorType(self, type, leftType, rightType):
    #     if leftType == int and rightType == int:
    #         match(type):
    #             case Tokens.PlusToken:
    #                 return BoundBinaryOperatorType.Addition
    #             case Tokens.MinusToken:
    #                 return BoundBinaryOperatorType.Substraction
    #             case Tokens.SlashToken:
    #                 return BoundBinaryOperatorType.Division
    #             case Tokens.StarToken:
    #                 return BoundBinaryOperatorType.Multiplication
    #             case _:
    #                 raise Exception(
    #                     "Unexpected Binray operator {}".format(type))
                
    #     if leftType == bool and rightType == bool:
    #         match(type):
    #             case Tokens.AmperSandToken:
    #                 return BoundBinaryOperatorType.LogicalAnd
    #             case Tokens.PipeToken:
    #                 return BoundBinaryOperatorType.LogicalOr
               
    def getDignostics(self):
        return self._diagnostics
    
    def getVariables(self):
        return self._variables