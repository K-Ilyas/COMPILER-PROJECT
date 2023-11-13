# COMPILER-PROJECT


### features : 

* Basic REPL (read-eval-print loop) for an expression evaluator
* Added lexer, a parser, evaluator, binder ( to verify the result of each statement ) 
* Handle `+`, `-`, `*`, `/`, `||`, `&&` and parenthesized expressions
* Print syntax trees ( Tree represenation of the parser )
* support unray operators (`-`,`+`)
* declare variables : `var` to declare global variables and `const` to declare read-only variables
* support scopes ( define nested scops using Curly brackets `{`,`}`)

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

### next features :

* if, while and for statements


