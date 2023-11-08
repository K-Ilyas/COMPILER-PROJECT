


from ExpressionSyntax import ExpressionSyntax
from Tokens import Tokens


class ParenthesizedExpressionSyntax(ExpressionSyntax):

    def __init__(self,openParenthesisToken,expression,closeParenthesisToken) -> None:
        
        self.openParenthesisToken = openParenthesisToken
        self.expression = expression
        self.closeParenthesisToken = closeParenthesisToken

    
    def getOpenParenthesisToken(self):
        return self.openParenthesisToken
    
    def getExpression(self):
        return self.expression
    
    def getCloseParenthesisToken(self):
        return self.closeParenthesisToken
    
    def getType(self):
        return Tokens.ParenthesizedExpressionSyntax
    
    # def getChildrens(self):
    #     yield self.openParenthesisToken
    #     yield self.expression
    #     yield self.closeParenthesisToken
    
