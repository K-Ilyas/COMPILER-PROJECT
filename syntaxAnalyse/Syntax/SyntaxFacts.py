

from Tokens import Tokens


class SynataxFacts():

    @staticmethod
    def getUnrayOperatorPrecedence(type):
        match type :
            case Tokens.PlusToken | Tokens.MinusToken | Tokens.BangToken:
                return 6
            case _:
                return 0
    
    @staticmethod
    def getBinayOperatorPrecedence(type):
        match type :
            case Tokens.SlashToken | Tokens.StarToken:
                return 5
            case Tokens.PlusToken | Tokens.MinusToken:
                return 4
            case Tokens.EqualsEqualsToken | Tokens.BangEqualsToken | Tokens.LessToken | Tokens.GreatToken | Tokens.LessOrEqualsToken | Tokens.GreatOrEqualsToken : 
                return 3
            case Tokens.AmpersandAmpersandToken :
                return 2
            case  Tokens.PipePipeToken:
                return 1
            case _:
                return 0
    @staticmethod
    def getKeywordType(txt):
        match txt :
            case "program":
                return Tokens.ProgramToken
            case "true":
                 return Tokens.TrueKeyword
            case "false":
                return Tokens.FalseKeyword
            case "const":
                 return Tokens.ConstKeyword
            case "var":
                return Tokens.VarKeyword
            case "if":
                return Tokens.IfKeyword
            case "then":
                return Tokens.ThenKeyword
            case "else" : 
                return Tokens.ElseKeyword
            case "while":
                return Tokens.WhileKeyword
            case "for":
                return Tokens.ForKeyword
            case "do":
                return Tokens.DoKeyword
            case "to":
                return Tokens.ToKeyword
            case "write":
                return Tokens.WriteKeyword
            case "read":
                return Tokens.ReadKeyword
            case "begin":
                return Tokens.OpenBraceToken
            case "end":
                return Tokens.CloseBraceToken
            case _:
                return Tokens.IdentifierToken
    @staticmethod
    def GetUnaryOperatorKinds() :
        for type in Tokens :
            if SynataxFacts.getUnrayOperatorPrecedence(type) > 0:
                yield type
    @staticmethod
    def GetBinaryOperatorKinds() :
        for type in Tokens :
            if SynataxFacts.getBinayOperatorPrecedence(type) > 0:
                yield type
    @staticmethod
    def GetText( type) :
            match (type):
                case Tokens.ProgramToken :
                    return "program"
                case Tokens.PlusToken:
                    return "+"
                case Tokens.MinusToken:
                    return "-"
                case Tokens.StarToken:
                    return "*"
                case Tokens.SlashToken:
                    return "/"
                case Tokens.BangToken:
                    return "!"
                case Tokens.AntiSlashToken :
                    return '\n'
                case Tokens.EqualsToken:
                    return ":="
                case Tokens.DoubleQuteToken :
                    return '"'
                case Tokens.AmpersandAmpersandToken:
                    return "&&"
                case Tokens.PipePipeToken:
                    return "||"
                case Tokens.LessOrEqualsToken :
                    return "<="
                case Tokens.LessToken :
                    return "<"
                case Tokens.GreatToken :
                    return ">"
                case Tokens.LessOrEqualsToken:
                    return ">="    
                case Tokens.EqualsEqualsToken:
                    return "="
                case Tokens.BangEqualsToken:
                    return "<>"
                case Tokens.OpenParenthesisToken:
                    return "("
                case Tokens.CloseParenthesisToken:
                    return ")"
                case Tokens.OpenBraceToken:
                    return "begin"
                case Tokens.CloseBraceToken:
                    return "end"
                case Tokens.CommaToken :
                    return ","
                case Tokens.FalseKeyword:
                    return "false"
                case Tokens.TrueKeyword:
                    return "true"
                case Tokens.VarKeyword:
                    return "var"
                case Tokens.ConstKeyword :
                    return "const"
                case Tokens.IfKeyword :
                    return "if"
                case Tokens.ElseKeyword :
                    return "else"
                case Tokens.ThenKeyword :
                    return "then"
                case Tokens.WhileKeyword:
                    return "while"
                case Tokens.DoKeyword :
                    return "do"
                case Tokens.ForKeyword :
                    return "for"
                case Tokens.ToKeyword :
                    return "to"
                case Tokens.StringToken :
                    return "String"
                case Tokens.WriteKeyword :
                    return "write"
                case Tokens.ReadKeyword :
                    return "read"
                
                case _:
                    return None
        