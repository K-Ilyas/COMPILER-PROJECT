
# The `Lexer` class is used for tokenizing a given text.
from ast import literal_eval
from struct import pack, error
from pyparsing import Any
from DiagnosticBag import DiagnosticBag
from SyntaxFacts import SynataxFacts
from SyntaxToken import SyntaxToken
from TextSpan import TextSpan
from Tokens import Tokens


class Lex:
    __position = 0
    __errors = DiagnosticBag()
    __start = 0
    __value = 0
    __type = None

    def __init__(self, text) -> None:
        self.text = text

    """
    The current function returns the current character in the text, or '\0' if the position is at
    the end of the text.
    :return: the character at the current position in the text. If the current position is greater
    than or equal to the length of the text, it returns the null character '\0'.
    """

    def peek(self, offset):
        index = self.__position + offset
        if index >= self.text.length():
            return '\0'
        return self.text[index]

    def lookahead(self):
        return self.peek(1)

    def current(self):
        return self.peek(0)

    """
    The function `incPos` increments the value of the private variable `__position` by 1.
    """

    def incPos(self):
        self.__position += 1

    def getErrors(self) -> Any:
        return self.__errors
    """
    The function `NextToken` returns the next token in the text, which is a digit, along with its syntax
    type, start position, text representation, and evaluated value.
    :return: The code is returning a SyntaxToken object.
    This is a function to iterate to the next token
    """

    def NextToken(self):

        # for end of file
        self.__start = self.__position
        self.__type = Tokens.BadToken
        self.__value = None

        # if self.__position >= len(self.text):
        #     return SyntaxToken(Tokens.EndOfFileToken, self.__position, "\0", None)
        match self.current():
                case '\0':
                    self.__type= Tokens.EndOfFileToken
                case '+':
                    self.__type= Tokens.PlusToken
                    self.incPos()
                case '-':
                    self.__type= Tokens.MinusToken
                    self.incPos()
                case '*':
                    self.__type= Tokens.StarToken
                    self.incPos()
                case '/':
                   if self.lookahead() == "*":
                      self.ReadComment()
                   else :
                     self.__type= Tokens.SlashToken
                     self.incPos()
                case ",":
                    self.__type= Tokens.CommaToken
                    self.incPos()    
                case '(':
                    self.__type= Tokens.OpenParenthesisToken
                    self.incPos()
                case ')':
                    self.__type= Tokens.CloseParenthesisToken
                    self.incPos()
                case '\'':
                    self.__type= Tokens.SingleQuteToken
                    self.incPos()
                case '"':
                    self.__type= Tokens.DoubleQuteToken
                    self.incPos()
                case ';':
                    self.__type= Tokens.SemiColonToken
                    self.incPos()
                case ".":
                    self.__type= Tokens.PointToken
                    self.incPos()

                case '\\':
                    if self.lookahead() == 'n':
                     self.__type= Tokens.AntiSlashToken
                     self.__position +=2
                    else :
                      self.__type = Tokens.IgnoreToken
                      self.incPos()
                
                case '&':
                    if  self.lookahead() == '&':
                        self.__type= Tokens.AmpersandAmpersandToken
                        self.__position += 2
                
                case "!":
                    self.__type= Tokens.BangToken
                    self.incPos()
               

                case '|':
                    if self.lookahead()  == '|' :
                    
                        self.__type= Tokens.PipePipeToken
                        self.__position += 2
            
                case ':':
                    if self.lookahead() == '=' :
                        self.__type= Tokens.EqualsToken
                        self.__position += 2

                
                case '=':
                        self.__type= Tokens.EqualsEqualsToken
                        self.incPos()
                
                
                case '<':
                    if self.lookahead() == '>' : 
                        self.__type= Tokens.BangEqualsToken
                        self.__position += 2
                    elif self.lookahead() == '=':
                        self.__type= Tokens.LessOrEqualsToken
                        self.__position += 2 
                    else :
                        self.__type= Tokens.LessToken
                        self.incPos()
        
                case '>':
                    if self.lookahead() == '=':
                        self.__type= Tokens.GreatOrEqualsToken
                        self.__position += 2 
                    else :
                        self.__type= Tokens.GreatToken
                        self.incPos()
                
                case '<':
                    if self.lookahead() == '>' : 
                        self.__type= Tokens.BangEqualsToken
                        self.__position += 2
                    elif self.lookahead() == '=':
                        self.__type= Tokens.LessOrEqualsToken
                        self.__position += 2 
                    else :
                        self.__type= Tokens.LessToken
                        self.incPos()   

                 
                 
                case '0' | '1' | '2' | '3' | '4' | '5' |'6' | '7' | '8' | '9':
                
                    self.ReadNumberToken()
                
     
                
                
                case ' ' | '\t' | '\n' | '\r':
          
                    self.ReadWhiteSpace()
                case _:
                    if self.current().isalpha() :
                    
                        self.ReadIdentifierOrKeyword()
                    
                    elif self.current().isspace() :
                    
                        self.ReadWhiteSpace()
                    
                    else : 
                    
                        self.__errors.ReportBadCharacter(self.__position, self.current())
                        self.incPos()
                    
    
        length = self.__position - self.__start

        text = SynataxFacts.GetText(self.__type)

        

        if text == None :
            text = self.text.ToString_start( self.__start,self.__start + length )
   
        return  SyntaxToken(self.__type, self.__start, text, self.__value)
    
    def ReadComment(self):
         while True :
           self.incPos()
           if self.current() == "*" and self.lookahead() == "/" :
             break
         self.__position +=2
       
         self.__type = Tokens.CommentToken 
         
    def ReadWhiteSpace(self):
        while (self.current().isspace()):
                self.incPos()
        self.__type = Tokens.SpaceToken 

    
    def ReadNumberToken(self):
        while (self.current().isdigit()):
                self.incPos()
        txt = self.text.ToString_start(self.__start,self.__position)
        try:
                pack("I", int(txt))
        except error:
                self.__errors.ReportInvalidInt32(TextSpan(self.__start,self.__position-self.__start),txt,int)
               
        self.__value = literal_eval(txt) 
        self.__type = Tokens.NumberToken

    def ReadIdentifierOrKeyword(self):

        while (self.current().isalpha()):
                self.incPos()

        txt = self.text.ToString_start( self.__start,self.__position)
        
        self.__type = SynataxFacts.getKeywordType(txt)
