

from TextSpan import TextSpan


class TextLine :

    def __init__(self,text,start,length,lengthIncludingLineBreak) -> None:
            self.text = text
            self.start = start
            self.length = length
            self.lengthIncludingLineBreak = lengthIncludingLineBreak

    def getText(self):
          return self.text
    
    def getStart(self):
          return self.start
    
    def getLength(self):
          return self.length
    
    def getLengthIncludingLineBreak(self):
          return self.lengthIncludingLineBreak
    
    def end(self):
          return self.start + self.length
    
    def span(self):
          return TextSpan(self.start,self.length)
    
    def SpanIncludingLineBreak(self):
          TextSpan(self.start, self.lengthIncludingLineBreak)

    def ToString_span(self):
      return self.text.ToString_span(self.span)
    
