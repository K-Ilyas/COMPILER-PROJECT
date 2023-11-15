
from abc import ABC, abstractmethod
from io import StringIO

from pyparsing import Iterable

from TextSpan import TextSpan


class SyntaxNode(ABC):
        @abstractmethod
        def getType(self):
            return None
        
        def span(self):
            first = self.getChildrens()[0]
            last = self.getChildrens[-1]
            return TextSpan.fromBounds(first,last)
        def getChildrens(self):
            properties = vars(self)  # Replace 'self' with your actual instance
          
            
            for property_name in properties:

              property_value = getattr(self, property_name)
              
            # Check if the property is of type SyntaxNode
              if isinstance(property_value, SyntaxNode):
                  
                  yield property_value
                  
            # Check if the property is of type IEnumerable<SyntaxNode>
              elif isinstance(property_value, Iterable) and all(isinstance(child, SyntaxNode) for child in property_value):

                 for child in property_value:
                    yield child

        # def WriteTo(self,writer):
        #     return SyntaxNode.printResultAsTree(writer,self)
        
        # @staticmethod
        # def printResultAsTree(writer,child,sep="",isLast = True):
        #       marker =   "└──" if isLast else "├──"
        #       writer(sep,end="")
        #       writer(marker,end="")
        #       writer(child.getType(),end="")
              
        #       from SyntaxToken import SyntaxToken

        #       if isinstance(child,SyntaxToken) and child.getValue() != None :
        #           writer("  ",end="")
        #           writer(child.getValue(),end="")
        
        #       writer("")

        #       sep += "    " if isLast else "│   "

        #       lst =  list(child.getChildrens())

        #       last = lst[-1] if len(lst) != 0 else child

        #       for child2 in child.getChildrens():
        #          SyntaxNode.printResultAsTree(writer,child2,sep, last == child2)

        # def __str__(self):
        #    with StringIO() as writer:
        #        self.WriteTo(writer)
        #        return writer.getvalue()