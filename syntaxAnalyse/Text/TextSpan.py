


class TextSpan:

    def __init__(self,start,length) -> None:
        self.start = start 
        self.length = length
    
    def getStart(self):
        return self.start
    
    def getLength(self):
        return self.length
    
    def getEnd(self):
        return self.start + self.length
    
    @staticmethod 
    def fromBounds(start,end):
        length = end - start
        return TextSpan(start,length)