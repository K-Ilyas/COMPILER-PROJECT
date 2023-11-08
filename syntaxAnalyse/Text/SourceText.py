

from TextLine import TextLine
from TextSpan import TextSpan


class SourceText:

    _text = None

    def __init__(self, text) -> None:
        self._text = text
        self.lines = self.ParseLines(self, text)
    def __getitem__(self, index: int) -> str:
        return self._text[index]
    
    def length(self):
        return len(self._text)

    def getLineIndex(self,position):
        lower = 0 
        upper = len(self.lines) - 1

        while lower <= upper :
            index = int(lower + (upper - lower) / 2)
            start = self.lines[index].getStart()

            if position == start: 
                return index
            if start > position :
                upper = index - 1
            else :
                lower = index + 1
        
        return lower - 1
    
    def getLines(self):
        return self.lines


    def ParseLines(self, sourceText, text):
        result = []
        position = 0
        lineStart = 0

        while position < len(text):
            lineBreakWidth = SourceText.getLineBreakWith(text, position)

            if lineBreakWidth == 0:
                position += 1

            else :
                self.addLine( result,  sourceText,  position,  lineStart,  lineBreakWidth)
                position += lineBreakWidth
                lineStart = position
            
        if position >= lineStart :
                self.addLine(result, sourceText, position, lineStart , 0)

        return result

    def addLine(self, result,  sourceText,  position,  lineStart,  lineBreakWidth):
        lineLength = position - lineStart
        lineLengthIncludingLineBreak = lineLength + lineBreakWidth
        line =  TextLine(sourceText, lineStart, lineLength, lineLengthIncludingLineBreak)
        result.append(line)

        
    @staticmethod
    def getLineBreakWith( text, i):
        c = text[i]
        l = '\0' if i + 1 >= len(text) else text[i+1]

        if c == '\r' and l == '\n':
            return 2

        if c == '\r' or c == '\n':
            return 1

        return 0
    @staticmethod
    def From(text):
        return SourceText(text)

    def ToString(self) -> str:
        return self._text
    
    def ToString_span(self,span) -> str:
        return self._text[span.getStart():span.getStart()+span.getLength()]
    
    def ToString_start(self,start,length) -> str:
        return self._text[start:length]
