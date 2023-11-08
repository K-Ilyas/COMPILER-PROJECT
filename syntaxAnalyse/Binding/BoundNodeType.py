
from enum import Enum, auto


class BoundNodeType(Enum):
    UnrayExpression = auto(),
    LiteralExpression = auto(),
    BinaryExpression = auto(),
    VariableExpression = auto(),
    AssignmentExpression = auto()
