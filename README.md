# COMPILER-PROJECT


### features : 

* Basic REPL (read-eval-print loop) for an expression evaluator
* Added lexer, a parser, evaluator, binder ( to verify the result of each statement ) 
* Handle `+`, `-`, `*`, `/`, `||`, `&&` and parenthesized expressions
* support `<`, `<=`, `>=`, and `>`
* Support `int`, `string`, `bool` Data types.
* Print syntax trees ( Tree represenation of the parser )
* support unray operators (`-`,`+`)
* declare variables : `var` to declare global variables and `const` to declare read-only variables
* support scopes ( define nested scops using Curly brackets `{`,`}`)
* support position and Line Numbers
* support if-statements, while-statements and for-statements
* support scopes
* Tree example :
  
``` 
└──Tokens.CompilationUnit
    ├──Tokens.ExpressionStatement
    │   └──Tokens.BinaryExpression
    │       ├──Tokens.LiteralExpression
    │       │   └──Tokens.NumberToken  20
    │       ├──Tokens.PlusToken
    │       └──Tokens.LiteralExpression
    │           └──Tokens.NumberToken  20
    └──Tokens.EndOfFileToken
```

### project description :

**Our project consist of 5 main parts :**
- Lexer : it turns the text into list of Tokens like `NumberToken`, `StringToken`, ... etc.
- Parser : in our project we used a recursive descent parser is a kind of top-down parser built from a set of mutually recursive procedures (or a non-recursive equivalent) where each such procedure implements one of the nonterminals of the grammar. Thus the structure of the resulting program closely mirrors that of the grammar it recognizes [learn more](https://www.bing.com/search?pglt=43&q=recursive+descent+parser&cvid=d7423b2343ca46b38e2510b1e047b6e8&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQc5MDZqMGoxqAIAsAIA&FORM=ANNTA1&PC=NMTS)
- Binder : it represents the semantic analysis of our compiler and will perform things like looking up variable names in scope, performing type checks, and enforcing correctness rules.
- Evaluator : it is a program that walks the syntax tree directly and calculate the result of the syntax tree povided by the parser after bind it, it has several functions to handle different cases like variable declaration, while evaluation, if statement evaluation, ... etc.
- Code Generator : it is a program that transform the tree provided by the parser into c code.


