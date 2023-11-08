


from abc import ABC,abstractclassmethod


class BoundNode(ABC):

    @abstractclassmethod 
    def getType(self):
        return None