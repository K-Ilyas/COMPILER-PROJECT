

# The `Parse` class is used for parsing and evaluating mathematical expressions.

from copy import deepcopy
from typing import Any
from AssignmentExpressionSyntax import AssignmentExpressionSyntax
from BinaryExpressionSyntax import BinaryExpressionSyntax
from CompilationUnitSyntax import CompilationUnitSyntax
from DiagnosticBag import DiagnosticBag
from Lex import Lex
from LiteralExpressionSyntax import LiteralExpressionSyntax
from NameExpressionSyntax import NameExpressionSyntax
from ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from SourceText import SourceText
from SyntaxFacts import SynataxFacts
from SyntaxToken import SyntaxToken
import SyntaxTree
from Tokens import Tokens
from UnrayExpressionSyntax import UnrayExpressionSyntax


class Parse:
    __listTokens = []
    __position = 0
    __errors = DiagnosticBag()
    __text = None

    def __init__(self, txt:SourceText) -> None:
        lex = Lex(txt)
        self.__text = txt
        while True:
            token = lex.NextToken()
            if token.getType() == Tokens.EndOfFileToken:
                self.__listTokens.append(token)
                break

            if token.getType() != Tokens.BadToken and token.getType() != Tokens.SpaceToken:
                self.__listTokens.append(token)

        
        self.__errors.AddErrors(lex.getErrors())
        # self.__errors =  deepcopy(lex.getErrors())

    # get a token with a offset as a margin
    def look(self, offset: int) -> SyntaxToken:
        index = self.__position + offset

        if index >= len(self.__listTokens):
            return self.__listTokens[-1]

        return self.__listTokens[index]
    
    def getText(self):
        return self.__text
    
    def current(self):
        return self.look(0)

    def NextToken(self):
        current = self.current()
        self.__position += 1
        return current

    def getTokens(self):
        return self.__listTokens

    def getErrors(self) -> Any:
        return self.__errors

    def MatchToken(self, type):
        if self.current().getType() == type:
            return self.NextToken()
        
        self.__errors.ReportUnexpectedToken(
            self.current().getSpan(), self.current().getType(), type)
        # self.__errors.append("Error : Unexptected Token {type} expected {ty}".format(
        #     type=self.current().getType(), ty=type))

        return SyntaxToken(type, self.current().getPos(), "''", None)

    def ParseCompilationUnit(self):
        expression = self.ParseExpression()
        endFileToken = self.MatchToken(Tokens.EndOfFileToken)
        return CompilationUnitSyntax(expression, endFileToken)
    

    def ParseExpression(self):
        return self.parseAssignmentExpression()
    
    def parseAssignmentExpression(self):
        if self.look(0).getType() == Tokens.IdentifierToken and self.look(1).getType() == Tokens.EqualsToken :
            identifierToken = self.NextToken()
            operatorToken = self.NextToken()
            right = self.parseAssignmentExpression()
            return AssignmentExpressionSyntax(identifierToken,operatorToken,right)
        
        return self.ParseBinaryExpression()
        # left = self.ParseBinaryExpression()
        # while self.current().getType() == Tokens.EqualsToken :
        #     operatorToken = self.NextToken()
        #     right = self.parseAssignmentExpression()
        #     left = AssignmentExpressionSyntax()


    def ParseBinaryExpression(self, parentPrecedence=0):

        left = None

        unrayOperatorPrecedence = SynataxFacts.getUnrayOperatorPrecedence(
            self.current().getType())

        if unrayOperatorPrecedence != 0 and unrayOperatorPrecedence >= parentPrecedence:
            operatorToken = self.NextToken()
            operand = self.ParseBinaryExpression(unrayOperatorPrecedence)
            left = UnrayExpressionSyntax(operatorToken, operand)
        else:
            left = self.ParsePrimaryExpression()
            # print(left.getIdentifierToken().getText())

        while True:
            precedence = SynataxFacts.getBinayOperatorPrecedence(
                self.current().getType())
            if precedence == 0 or precedence <= parentPrecedence:
                break

            operatorToken = self.NextToken()
            right = self.ParseBinaryExpression(precedence)


            left = BinaryExpressionSyntax(left, operatorToken, right)

        return left

    # def ParseTerm(self):
    #     left = self.ParseFactor()

    #     while self.current().getType() == Tokens.PlusToken or self.current().getType() == Tokens.MinusToken :
    #         opertorToken = self.NextToken()
    #         right = self.ParseFactor()
    #         left = BinaryExpressionSyntax(left,opertorToken,right)

    #     return left

    # def ParseFactor(self):
    #     left = self.ParsePrimaryExpression()

    #     while self.current().getType() == Tokens.StarToken or self.current().getType() == Tokens.SlashToken :
    #         opertorToken = self.NextToken()
    #         right = self.ParsePrimaryExpression()
    #         left = BinaryExpressionSyntax(left,opertorToken,right)

    #     return left

    def type(self):
        return Tokens.BinaryExpression

    def ParsePrimaryExpression(self):
        match self.current().getType() :
            case Tokens.OpenParenthesisToken :
                return self.ParseParenthesizedExpression()
            case Tokens.TrueKeyword | Tokens.FalseKeyword :
                return self.ParseBooleanLiteral()
            case Tokens.NumberToken :
                return self.ParseNumberLiteral()
            case Tokens.IdentifierToken : 
                return self.ParseNameExpression()
            case _:
                return self.ParseNameExpression()
        # if self.current().getType() == Tokens.OpenParenthesisToken:
        #     left = self.NextToken()
        #     # I need some changes her
        #     expression = self.ParseExpression()
        #     right = self.MatchToken(Tokens.CloseParenthesisToken)
        #     return ParenthesizedExpressionSyntax(left, expression, right)
        # elif self.current().getType() == Tokens.TrueKeyword or self.current().getType() == Tokens.FalseKeyword:
        #     keywordToken = self.NextToken()
        #     value = keywordToken.getType() == Tokens.TrueKeyword

        #     return LiteralExpressionSyntax(keywordToken, value)
        # elif self.current().getType() == Tokens.IdentifierToken :
        #     identifierToken = self.NextToken()
        #     # if self.current().getType() == Tokens.EqualsToken :
        
         
        #     return NameExpressionSyntax(identifierToken)

        # numberToken = self.MatchToken(Tokens.NumberToken)
        # return LiteralExpressionSyntax(numberToken)
    
    def ParseParenthesizedExpression(self):
            left = self.MatchToken(Tokens.OpenParenthesisToken)
            # I need some changes her
            expression = self.ParseExpression()
            right = self.MatchToken(Tokens.CloseParenthesisToken)
            return ParenthesizedExpressionSyntax(left, expression, right)
    
    def ParseBooleanLiteral(self):
            isTrue = self.current().getType() == Tokens.TrueKeyword
            keywordToken = self.MatchToken(Tokens.TrueKeyword) if isTrue else self.MatchToken(Tokens.FalseKeyword)
            return LiteralExpressionSyntax(keywordToken,  isTrue)
    
    def ParseNumberLiteral(self):
           numberToken = self.MatchToken(Tokens.NumberToken)
           return LiteralExpressionSyntax(numberToken)
    
    def ParseNameExpression(self):
            identifierToken = self.MatchToken(Tokens.IdentifierToken)
            return NameExpressionSyntax(identifierToken)
