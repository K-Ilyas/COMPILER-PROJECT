


from enum import Enum, auto


class BoundBinaryOperatorType(Enum):
    Addition = auto(),
    Substraction = auto(),
    Multiplication = auto(),
    Division = auto(),
    LogicalAnd = auto(),
    LogicalOr = auto(),
    Equals = auto(),
    NotEquals  = auto(),
    Less = auto(),
    Greater = auto(),
    LessOrEquals = auto(),
    GreaterOrEquals = auto(),
    StringConcatenation = auto(),

