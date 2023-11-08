

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
            case Tokens.EqualsEqualsToken | Tokens.BangEqualsToken : 
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
            case "true":
                 return Tokens.TrueKeyword
            case "false":
                return Tokens.FalseKeyword
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
                case Tokens.EqualsToken:
                    return "="
                case Tokens.AmpersandAmpersandToken:
                    return "&&"
                case Tokens.PipePipeToken:
                    return "||"
                case Tokens.EqualsEqualsToken:
                    return "=="
                case Tokens.BangEqualsToken:
                    return "!="
                case Tokens.OpenParenthesisToken:
                    return "("
                case Tokens.CloseParenthesisToken:
                    return ")"
                case Tokens.FalseKeyword:
                    return "false"
                case Tokens.TrueKeyword:
                    return "true"
                case _:
                    return None
        