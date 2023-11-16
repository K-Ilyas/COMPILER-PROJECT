
from TextSpan import TextSpan
from SyntaxNode import SyntaxNode


class SyntaxToken(SyntaxNode):
    
    def __init__(self,type,pos,txt,value) -> None:
        self.type = type
        self.pos = pos
        self.txt = txt
        self.value = value

    def type(self):
            return self.type
    def getType(self):
        return self.type
    
    def getText(self):
        return self.txt
    
    def getValue(self):
        return self.value
    
    def getPos(self):
        return self.pos 
    
    def getSpan(self):
         return TextSpan(self.pos, 0 if self.txt is None else len(self.txt))