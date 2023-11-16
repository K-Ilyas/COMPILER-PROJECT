

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
    OpenBraceToken = auto(),
    CloseBraceToken = auto(),
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
    VarKeyword= auto(),
    ConstKeyword = auto(),
    IdentifierToken = auto(),
    BangToken = auto(),
    AmpersandAmpersandToken = auto(),
    PipePipeToken = auto(),
    EqualsEqualsToken = auto(),
    BangEqualsToken = auto(),
    EqualsToken = auto(),
    CompilationUnit = auto(),
    BlockStatement = auto(),
    CommaToken = auto(),
    ExpressionStatement= auto(),
    VariableDeclaration = auto(),
    SemiColonToken = auto(),
    LessOrEqualsToken = auto(),
    LessToken = auto(),
    GreatOrEqualsToken = auto(),
    GreatToken = auto(),
    IfKeyword = auto(),
    ElseKeyword = auto(),
    IfStatement = auto(),
    ElseClause =auto()
    ThenKeyword= auto(),
    WhileKeyword = auto(),
    WhileStatement = auto(),
    ForStatement = auto(),
    ForKeyword = auto(),
    DoKeyword = auto(),
    ToKeyword = auto(),
    GlobalScope = auto()