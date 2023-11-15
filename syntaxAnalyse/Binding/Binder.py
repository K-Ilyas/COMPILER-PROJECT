
from Binding.BoundAssignmentExpression import BoundAssignmentExpression
from Binding.BoundBinaryExpression import BoundBinaryExpression
from Binding.BoundBinaryOperator import BoundBinaryOperator
from Binding.BoundBinaryOperatorType import BoundBinaryOperatorType
from Binding.BoundBlockStatement import BoundBlockStatement
from Binding.BoundExpressionStatement import BoundExpressionStatement
from Binding.BoundForStatement import BoundForStatement
from Binding.BoundGlobalScope import BoundGlobalScope
from Binding.BoundIfStatement import BoundIfStatement
from Binding.BoundLiteralExpression import BoundLiteralExpression
from Binding.BoundScope import BoundScope
from Binding.BoundUnrayExpression import BoundUnrayExpression
from Binding.BoundUnrayOperator import BoundUnrayOperator
from Binding.BoundUnrayOperatorType import BoundUnrayOperatorType
import sys
from Binding.BoundVariableDeclaration import BoundVariableDeclaration
from Binding.BoundVariableExpression import BoundVariableExpression
from Binding.BoundWhileStatement import BoundWhileStatement

import types



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
from BlockStatementSyntax import BlockStatementSyntax
from ExpressionStatementSyntax import ExpressionStatementSyntax
from VariableDeclarationSyntax import VariableDeclarationSyntax
from IfStatementSyntax import IfStatementSyntax
from WhileStatementSyntax import WhileStatementSyntax
from ForStatementSyntax import ForStatementSyntax

class Binder():

    _diagnostics = None
    _variables =dict()
    _scope = None

    def __init__(self,parent) -> None:
        self._diagnostics = DiagnosticBag()
        self._scope = BoundScope(parent)
        

    def getScope(self):
        return self._scope
    @staticmethod
    def bindGlobalScope(previous,syntax):
        parentScope = Binder.createParentScope(previous)
        binder = Binder(parentScope)
        expression = binder.BindStatement(syntax.getStatement())
        variables = binder.getScope().getDeclaredVariables()
        diagnostics = binder.getDignostics()
        if previous != None:
            diagnostics.InsertRange(0,previous.getDiagnostics())
        return BoundGlobalScope(previous,diagnostics,variables,expression)
    
    @staticmethod    
    def createParentScope(previous):
        stack = []
        while previous != None :
            stack.append(previous)
            previous = previous.getPrevious()
        
        parent = None 

        while len(stack) > 0:
            previous = stack.pop()
            scope = BoundScope(parent)

            for v in previous.getVariables():
                scope.tryDeclare(v)

            parent = scope
        return parent
    

    def BindStatement(self, syntax):

        if  isinstance(syntax, types.GeneratorType) :
            for item in syntax :
                item.__class__ = VariableDeclarationSyntax
                print(item.getType())
                self.BindStatement(item)
        else :

         match(syntax.getType()):  
            case Tokens.BlockStatement :
                syntax.__class__ = BlockStatementSyntax
                return self.BindBlockStatement(syntax)
            case Tokens.VariableDeclaration :
                syntax.__class__ = VariableDeclarationSyntax
                return self.BindVariableDeclaration(syntax)
            case Tokens.IfStatement :
                syntax.__class__ = IfStatementSyntax
                return self.BindIfStatement(syntax)
            case Tokens.WhileStatement :
                syntax.__class__ = WhileStatementSyntax
                return self.BindWhileStatement(syntax)
            case Tokens.ForStatement :
                syntax.__class__ = ForStatementSyntax
                return self.BindForStatement(syntax)
            case Tokens.ExpressionStatement :
                syntax.__class__ = ExpressionStatementSyntax
                return self.BindExpressionStatement(syntax)
            case _:
                raise Exception(
                    "Unexpected syntax {}".format(syntax.getType()))
            
    def BindBlockStatement(self,syntax):
        statements = [] 
        self._scope = BoundScope(self._scope)

        for statementSyntax in syntax.getStatments() :
            statement = self.BindStatement(statementSyntax)
            statements.append(statement)
        self._scope = self._scope.getParent()
        return BoundBlockStatement(statements)
    
    def BindVariableDeclaration(self,syntax):
           
            name = syntax.getIdentifier().getText()
            isReadOnly = syntax.getKeyword().getType() == Tokens.ConstKeyword 
            initializer = self.BindExpression(syntax.getIntializer())
            variable =  VariableSymbole(name, isReadOnly, initializer.type())

            succed = self._scope.tryDeclare(variable)
    
            if not succed :
                self._diagnostics.ReportVariableAlreadyDeclared(syntax.getIdentifier().getSpan(), name)

            return  BoundVariableDeclaration(variable, initializer)

    def BindExpressionStatement(self,syntax):
        expression = self.BindExpression(syntax.getExpression())
        return BoundExpressionStatement(expression)


    def BindIfStatement(self,syntax):
        condition = self.BindExpressionIf(syntax.getCondition(),bool)
        statement = self.BindStatement(syntax.getThenStatement())
        elseStatement = None if syntax.getElseClauseSyntax() == None else self.BindStatement(syntax.getElseClauseSyntax().getElseStatement())
        return BoundIfStatement(condition,statement,elseStatement)
    
    def BindWhileStatement(self,syntax):
        condition = self.BindExpressionIf(syntax.getCondition(),bool)
        print("wow",condition.getType())
        body = self.BindStatement(syntax.getBody())
        print("before",body.getType())

        new_var = BoundWhileStatement(condition,body)
        print("wow",new_var.getBody().getType())

        return new_var
    def BindForStatement(self,syntax):
        lowerBound = self.BindExpressionIf(syntax.getLowerBound(),int)
        upperBound = self.BindExpressionIf(syntax.getUpperBound(),int)

        self._scope = BoundScope(self._scope)

        name = syntax.getIdentifier().getText()

        variable = VariableSymbole(name,True,int)

        if not self._scope.tryDeclare(variable) :
            self._diagnostics.ReportVariableAlreadyDeclared(syntax.getIdentifier().getSpan(),name)

        body = self.BindStatement(syntax.getBody())

        self._scope = self._scope.getParent()

        return BoundForStatement(variable,lowerBound,upperBound,body)
            



    def BindExpressionIf(self,syntax,targetType):
        result = self.BindExpression(syntax)
        if result.type() != targetType :
           self._diagnostics.ReportCannotConvert(syntax.getSpan(),result.type(), targetType)
        
        return result

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
        variable =  self._scope.tryLookUp(name)

        if not variable[0]:
            self._diagnostics.ReportUndefinedName(syntax.getIdentifierToken().getSpan(),name)
            return BoundLiteralExpression(0)
        # self._variables[name].getType() if self._variables[name].getType() == None else object
        return BoundVariableExpression(variable[1])


    def BindAssignmentExpression(self,syntax):
       name =  syntax.getIdentifierToken().getText()
       boundExpression = self.BindExpression(syntax.getExpression())

       exist = self._scope.tryLookUp(name)
       print(name)
       if not exist[0]:
            self._diagnostics.ReportUndefinedName(syntax.getIdentifierToken().getSpan(),name)
            return boundExpression
       
       if exist[1].getIsReadOnly() :
            self._diagnostics.ReportCannotAssign(syntax.getEqualsToken().getSpan(),name)

        
       if exist[1] != None and boundExpression.type() != exist[1].type():
            self._diagnostics.ReportCannotConvert(syntax.getExpression().getLiteralToken().getSpan(),boundExpression.type(),exist[1].type())
            return boundExpression

    #    defaultValue = 0 if boundExpression.type() == int else (False if boundExpression.type() == bool else None)

    #    if defaultValue == None :
    #        raise Exception("Unsupported variable type {}".format(boundExpression.getType()))
         
       return BoundAssignmentExpression(exist[1],boundExpression) 

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
        # print(self._diagnostics)
        return self._diagnostics
    
    def getVariables(self):
        return self._variables