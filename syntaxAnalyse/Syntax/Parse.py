

# The `Parse` class is used for parsing and evaluating mathematical expressions.

from typing import Any
from AssignmentExpressionSyntax import AssignmentExpressionSyntax
from BinaryExpressionSyntax import BinaryExpressionSyntax
from BlockStatementSyntax import BlockStatementSyntax
from CompilationUnitSyntax import CompilationUnitSyntax
from DiagnosticBag import DiagnosticBag
from ElseClauseSyntax import ElseClauseSyntax
from ExpressionStatementSyntax import ExpressionStatementSyntax
from ForStatementSyntax import ForStatementSyntax
from GlobalScopeSyntax import GlobalScopeSyntax
from IfStatementSyntax import IfStatementSyntax
from Lex import Lex
from LiteralExpressionSyntax import LiteralExpressionSyntax
from NameExpressionSyntax import NameExpressionSyntax
from ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from ReadFunctionSyntax import ReadFunctionSyntax
from SourceText import SourceText
from SyntaxFacts import SynataxFacts
from SyntaxToken import SyntaxToken
import SyntaxTree
from Tokens import Tokens
from UnrayExpressionSyntax import UnrayExpressionSyntax
from VariableDeclarationSyntax import VariableDeclarationSyntax
from WhileStatementSyntax import WhileStatementSyntax
from WriteFunctionSyntax import WriteFunctionSyntax


class Parse:
    __listTokens = None
    __position = 0
    __errors = None
    __text = None

    def __init__(self, txt:SourceText) -> None:
        self.__listTokens = []
        lex = Lex(txt)
        self.__text = txt
        self.__errors = DiagnosticBag()
        isString = False
        while True:
            token = lex.NextToken()
   
            if token.getType() == Tokens.EndOfFileToken:
                self.__listTokens.append(token)
                break
            if token.getType() == Tokens.DoubleQuteToken :
                isString = not isString

            if  (not isString) and  token.getType() != Tokens.BadToken and token.getType() != Tokens.CommentToken and token.getType() != Tokens.SpaceToken:
                self.__listTokens.append(token)
            else :
                if token.getType() != Tokens.BadToken and token.getType() != Tokens.CommentToken  and isString :
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
    
    def MatchTokenVar(self, type):
        if self.current().getType() == type:
            return self.NextTokenVar()
    
    def MatchToken(self, type):
        if self.current().getType() == type:
            return self.NextToken()
        
        self.__errors.ReportUnexpectedToken(
            self.current().getSpan(), self.current().getType(), type)
        
        # self.__errors.append("Error : Unexptected Token {type} expected {ty}".format(
        #     type=self.current().getType(), ty=type))

        return SyntaxToken(type, self.current().getPos(), "''", None)
    
    def ParseStatement(self):

        if self.current().getType() == Tokens.OpenBraceToken :
            return self.ParseBlockStatement()
        if self.current().getType() == Tokens.VarKeyword or self.current().getType() == Tokens.ConstKeyword :
            return self.ParseVariableDeclaration()
        if self.current().getType() == Tokens.IfKeyword: 
            return self.ParseIfStatement()
        if self.current().getType() == Tokens.WhileKeyword: 
            return self.ParseWhileStatement() 
        if self.current().getType() == Tokens.ForKeyword: 
            return self.ParseForStatement() 
        if self.current().getType() == Tokens.WriteKeyword :
            return self.ParseWriteFunction()
        if self.current().getType() == Tokens.ReadKeyword :
            return self.ParseReadFunction()
        return self.ParseExpressionStatement()
    
    def ParseWhileStatement(self):
        keyword = self.MatchToken(Tokens.WhileKeyword)
        condition = self.ParseExpression()
        doKeyword = self.MatchToken(Tokens.DoKeyword)
        body = self.ParseStatement()
        return WhileStatementSyntax(keyword,condition,doKeyword,body)
    
    def ParseForStatement(self):
        forkeyword = self.MatchToken(Tokens.ForKeyword)
        identifier = self.MatchToken(Tokens.IdentifierToken)
        equalsToken = self.MatchToken(Tokens.EqualsToken)
        lowerBound = self.ParseExpression()
        tokeyword = self.MatchToken(Tokens.ToKeyword)
        upperBound = self.ParseExpression()
        body = self.ParseStatement()
        return ForStatementSyntax(forkeyword,identifier,equalsToken,lowerBound,tokeyword,upperBound,body)
    


    def ParseWriteFunction(self):
            writekeyword = self.MatchToken(Tokens.WriteKeyword)
            primaryExpressions = self.ParseBlockExpressions()
            semiColonToken = self.MatchToken(Tokens.SemiColonToken)
            return WriteFunctionSyntax(writekeyword,primaryExpressions[0],primaryExpressions[1],primaryExpressions[2],semiColonToken)

    def ParseReadFunction(self):
            readKeyword = self.MatchToken(Tokens.ReadKeyword)
            assignmentExpressions = self.ParseBlockAssignments()
            semiColonToken = self.MatchToken(Tokens.SemiColonToken)
            return ReadFunctionSyntax(readKeyword,assignmentExpressions[0],assignmentExpressions[1],assignmentExpressions[2],semiColonToken)


    def ParseVariableDeclaration(self):
        VariableDeclarations= []
        variablesPosition = []
        expected = Tokens.ConstKeyword if  self.current().getType() == Tokens.ConstKeyword else Tokens.VarKeyword
        keyword = self.MatchToken(expected)
        identifier = self.MatchToken(Tokens.IdentifierToken)
        deletePos = self.__position
        enterTest = False
        while True :
            if self.current().getType() == Tokens.CommaToken:
                self.MatchToken(Tokens.CommaToken)
                variablesPosition.append(self.__position)
                VariableDeclarations.append(self.MatchToken(Tokens.IdentifierToken))
                enterTest = True
            else :
                break
        equalPos = self.__position
        
        equals = None
        intializer = None
        semiColonToken = None

        if self.current().getType() == Tokens.SemiColonToken :
            equals = None
            intializer = LiteralExpressionSyntax(SyntaxToken(Tokens.NumberToken,0,"",0))
            semiColonToken = self.MatchToken(Tokens.SemiColonToken)
        else :
          equals = self.MatchToken(Tokens.EqualsToken)
          intializer = self.ParseExpression()
          semiColonToken = self.MatchToken(Tokens.SemiColonToken)
        
        if enterTest :

           for i in range(deletePos,equalPos) :
            #    print("this is wrong",self.__listTokens[i].getText())
               self.__listTokens[i] = SyntaxToken(Tokens.SpaceToken,i," ",None)
            #    self.__position -=1

           for item in VariableDeclarations :

               for token in self.__listTokens[self.__position-1:equalPos-1:-1] :
                   self.__listTokens.insert(self.__position,token)
        
               self.__listTokens.insert(self.__position,item)
               self.__listTokens.insert(self.__position,keyword)


      
        return VariableDeclarationSyntax(keyword,identifier,equals,intializer,semiColonToken)
    
    def ParseExpressionStatement(self):
        expression = self.ParseExpression()
        return ExpressionStatementSyntax(expression)
    
    def ParseBlockExpressions(self):
        openParenthesisToken  = self.MatchToken(Tokens.OpenParenthesisToken)
        statements = [] 
        while self.current().getType() != Tokens.EndOfFileToken and self.current().getType() != Tokens.CloseParenthesisToken  and self.current().getType() != Tokens.CommaToken:
            statement = self.parseAssignmentExpression()
            statements.append(statement)
            if self.current().getType() == Tokens.CommaToken :
                self.NextToken()
        closeParenthesisToken = self.MatchToken(Tokens.CloseParenthesisToken)
        return (openParenthesisToken,statements,closeParenthesisToken)
    
    def ParseBlockAssignments(self):
        openParenthesisToken  = self.MatchToken(Tokens.OpenParenthesisToken)
        statements = [] 

        while self.current().getType() != Tokens.EndOfFileToken and self.current().getType() != Tokens.CloseParenthesisToken  and self.current().getType() != Tokens.CommaToken:
            statement = self.ParseNameExpression()
            statements.append(statement)
            if self.current().getType() == Tokens.CommaToken :
                self.NextToken()
        closeParenthesisToken = self.MatchToken(Tokens.CloseParenthesisToken)
        return (openParenthesisToken,statements,closeParenthesisToken)
    
    def ParseBlockStatement(self):
        statements = []
        openBraceToken = self.MatchToken(Tokens.OpenBraceToken) 
        while self.current().getType() != Tokens.EndOfFileToken and self.current().getType() != Tokens.CloseBraceToken   :
            startToken = self.current() 
            statement = self.ParseStatement()
            statements.append(statement)
            
        closeBraceToken = self.MatchToken(Tokens.CloseBraceToken)
        return BlockStatementSyntax(openBraceToken,statements,closeBraceToken)

    
    def ParseGloablScope(self):
        if self.current().getType() == Tokens.OpenBraceToken :
            return self.ParseStatement() 
        statements = []
        while self.current().getType() != Tokens.EndOfFileToken   :
           startToken = self.current() 

           statement = self.ParseStatement()
           statements.append(statement)
           if self.current() == startToken and self.current().getType() != Tokens.VarKeyword and self.current().getType() != Tokens.ConstKeyword  :
                self.NextToken()

        return GlobalScopeSyntax(statements)
    
    def ParseIfStatement(self):
        keyword = self.MatchToken(Tokens.IfKeyword)
        condition = self.ParseExpression()
        thenKeyword = self.MatchToken(Tokens.ThenKeyword)
        statement = self.ParseStatement()
        elseClause = self.ParseElseClause()

        return IfStatementSyntax(keyword,condition,thenKeyword,statement,elseClause)
    
    
    def ParseElseClause(self):
        if self.current().getType() != Tokens.ElseKeyword :
            return None
        keyword = self.MatchToken(Tokens.ElseKeyword)
        statement = self.ParseStatement()
        return ElseClauseSyntax(keyword,statement)

    def ParseCompilationUnit(self):
        programToken = self.MatchToken(Tokens.ProgramToken)
        startIndex = self.__position
        value = self.MatchToken(Tokens.IdentifierToken).getText()
        while self.current().getType() != Tokens.SemiColonToken and self.current().getType() == Tokens.IdentifierToken:
            value += self.NextToken().getText()
        
        programNameToken = SyntaxToken(Tokens.NameProgramToken,startIndex,value,value)
        semiColonToken = self.MatchToken(Tokens.SemiColonToken)

        statement = self.ParseGloablScope()

        endStatementToken = self.MatchToken(Tokens.EndOfFileToken)
        return CompilationUnitSyntax(programToken,programNameToken,semiColonToken,statement, endStatementToken)

    def ParseExpression(self):
        return self.parseAssignmentExpression()
    
    def parseAssignmentExpression(self):
        if self.look(0).getType() == Tokens.IdentifierToken and self.look(1).getType() == Tokens.EqualsToken :
            identifierToken = self.NextToken()
            operatorToken = self.NextToken()
            right = self.parseAssignmentExpression()
            semiColonToken = self.MatchToken(Tokens.SemiColonToken)
            return AssignmentExpressionSyntax(identifierToken,operatorToken,right,semiColonToken)
        binaryExpression = self.ParseBinaryExpression()
        
        return binaryExpression

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
            case Tokens.DoubleQuteToken :
                return self.ParseStringLiteral()
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
    
    def ParseStringLiteral(self):
        startIndex = self.__position
        self.MatchToken(Tokens.DoubleQuteToken)  
        value = ""
        while self.current().getType() != Tokens.DoubleQuteToken :
            # next = self.NextToken().getText()
            # if next == '\n':
            #     value += '\\n'
            # else : value += next
            value = value + self.NextToken().getText()
        self.MatchToken(Tokens.DoubleQuteToken)
        return LiteralExpressionSyntax(SyntaxToken(Tokens.StringToken,startIndex,value,value))
    
    def ParseNameExpression(self):
            identifierToken = self.MatchToken(Tokens.IdentifierToken)
            return NameExpressionSyntax(identifierToken)
