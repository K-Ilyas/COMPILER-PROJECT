

from Binding.BoundNode import BoundNode
from abc import abstractmethod


class BoundExpression(BoundNode):

    @abstractmethod 
    def type(self):
        return None
    