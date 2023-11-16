
from enum import Enum, auto


class BoundNodeType(Enum):
    UnrayExpression = auto(),
    LiteralExpression = auto(),
    BinaryExpression = auto(),
    VariableExpression = auto(),
    AssignmentExpression = auto(),
    BlockStatement = auto(),
    ExpressionStatement = auto(),
    VariableDeclaration = auto(),
    IfStatement = auto(),
    WhileStatement = auto(),
    ForStatement = auto(),
    GlobalScope = auto()