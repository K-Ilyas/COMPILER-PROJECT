

from enum import Enum, auto

class Tokens(Enum):
    NumberToken = auto(),
    SpaceToken = auto(),
    PlusToken = auto(),
    MinusToken = auto(),
    StarToken = auto(),
    SlashToken = auto(),
    OpenParenthesisToken = auto(),
    CloseParenthesisToken = auto(),
    BadToken = auto(),
    EndOfFileToken = auto(),
    LiteralExpression = auto(),
    BinaryExpression = auto(),
    NameExpression = auto(),
    AssignmentExpression = auto(),
    ParenthesizedExpressionSyntax = auto(),
    UnrayExpression = auto(),
    TrueKeyword = auto(),
    FalseKeyword = auto(),
    IdentifierToken = auto(),
    BangToken = auto(),
    AmpersandAmpersandToken = auto(),
    PipePipeToken = auto(),
    EqualsEqualsToken = auto(),
    BangEqualsToken = auto(),
    EqualsToken = auto(),
    CompilationUnit = auto()
