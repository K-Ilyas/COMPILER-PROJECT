# COMPILER-PROJECT

# Syntax

## Exemple

``` {.pascal mathescape="" linenos="" bgcolor="bg"}
program test;
var name := "John";
var age;
var isCorrect := false;
var calc := ((129)+(3/9))/26;
write("Hello, my name is ", name, "\n");
write("Enter votre age \n");
read(age);
write("I am ", age, " years old\n");
write("calc = ", calc);

if age >= 18 then
    begin
        write("I am an adult\n");
    end
else
    begin
        write("I am a minor\n");
    end

var a :=15;
while a >= 0 do
begin
    write(a,"\n");
    a := a - 1;
end
```

equivalente dans python

``` {.python mathescape="" linenos="" bgcolor="bg"}
name = "John"
age = 25
calc = ((12*9)+(3/9))/26
print(f"Hello, my name is {name});
ptint(f"I am {age} years old");
print(f"calc = {calc}");
isCorrect = False
if age >= 18:
    print("I am an adult");
else:
    print("I am a minor");

a = 15;
while a >= 0:
    print(a)
    a = a - 1
```

Generated C code

``` {.c mathescape="" linenos="" bgcolor="bg"}
#include <stdio.h>
#include <stdlib.h>
int main(){
;
char* name="John";
int age=0;
char* isCorrect=0;
int calc=129+3/9/26;
printf("%s%s%s","Hello, my name is ",name,"\n");
printf("%s","Enter votre age \n");
scanf("%d",&age);
printf("%s%d%s","I am ",age," years old\n");
printf("%s%d","calc = ",calc);
if(age>=18){
printf("%s","I am an adult\n");
}
else{
printf("%s","I am a minor\n");
}
int a=15;
while(a>=0){
printf("%d%s",a,"\n");
a=a-1;
}
return 0;
}
```

## Exemple Boucle for

``` {.pascal mathescape="" linenos="" bgcolor="bg"}
    /* this is a  loop*/
for z := 12 to 100
begin
    write(z);
end    
```

En python

``` {.Python mathescape="" linenos="" bgcolor="bg"}
# this is a  loop
for z in range(12, 1000)
    print(z)
```

### Déclarations de variables :

-   **name: string = 'John';**: Déclare une variable name de type string
    et l'initialise avec la valeur 'John'.

-   **age: integer = 25;**:Déclare une variable age de type **integer**
    et l'initialise avec la valeur 25.

-   **calc: real;**: Déclare une variable calc de type **real** (nombre
    à virgule flottante) sans initialisation.

### Calculs :

**calc := ((12 \* 9) + (3 / 9)) / 26;** : Effectue un calcul et attribue
le résultat à la variable calc. Le calcul est ((12 \* 9) + (3 / 9)) /
26.

### Sortie (Output) :

-   **write(\"Hello, my name is \", name, \"$\backslash$n\");**: Affiche
    une ligne dans la console, imprimant le texte \"Hello, my name is \"
    suivi de la valeur de la variable name.

-   **write(\"I am\", age, \"years old$\backslash$n\");** : Affiche une
    ligne dans la console, imprimant le texte \"I am \" suivi de la
    valeur de la variable age et \" years old\".

-   **write('calc = ', calc,\"$\backslash$\")n;**: Affiche une ligne
    dans la console, imprimant le texte \"calc = \" suivi de la valeur
    de la variable calc.

### Instruction conditionnelle :

**if age \>= 18 then \... else \...**: Vérifie si la valeur de age est
supérieure ou égale à 18. Si c'est vrai, cela affiche **\"I am an
adult$\backslash$n\"**; sinon, cela affiche \"I am a
minor$\backslash$n\".

### Boucle (Loop) :

-   **var counter := 0;**: Déclare une variable a de type integer et
    l'initialise avec la valeur 0.

-   **while a $<$ 3 do \...**:Exécute le bloc de code à l'intérieur de
    la boucle while tant que la condition a \< 3 est vraie.

    -   **write(\"Count:\", counter,\" \");**: Affiche la valeur de a
        suivie de deux espaces dans la console.

    -   **counter := counter + 1;** Incrémente la valeur de a de 1 à
        chaque itération.

## Types de données

Dans notre compilateur **L3Lang**, nous avons 3 types :

-   entier (12, 343, 5, 6, -121, 43)

-   booléen (Vrai, Faux)

-   chaîne de caractères (\"this is a String\")

## Commentaires

En L3Lang, les commentaires sont représentés de la manière suivante :

``` c
    /* Ceci est un commentaire qui sera ignoré */
```

Cela est similaire à la syntaxe du langage C.

# Tokens

``` {.python mathescape="" linenos="" bgcolor="bg"}
from enum import Enum, auto
class Tokens(Enum):
    ProgramToken = auto(),
    NameProgramToken = auto(),
    NumberToken = auto(),
    DoubleQuteToken = auto(),
    SpaceToken = auto(),
    PlusToken = auto(),
    .
    .
    .
    ReadKeyword = auto(),
```

Une représentation simple de chaque jeton en leur attribuant un nom
spécifique lié à un numéro unique pour garantir que chaque jeton a une
représentation unique. L'ajout d'un nouveau jeton génère automatiquement
la représentation unique.

# Syntax Token

``` {.python mathescape="" linenos="" bgcolor="bg"}
class SyntaxToken(SyntaxNode):
    def __init__(self,type,pos,txt,value) -> None:
        self.type = type
        self.pos = pos
        self.txt = txt
        self.value = value
    def type(self):
        return self.type
    def getType(self):
        return self.type
    def getText(self):
        return self.txt
    def getValue(self):
        return self.value
    def getPos(self):
        return self.pos 
    def getSpan(self):
         return TextSpan(self.pos, 0 if self.txt is None else len(self.txt))
```

Une classe utilitaire utilisée pour obtenir la valeur, le texte ou la
position d'un jeton dans le code source, afin de mettre en évidence les
problèmes, les erreurs, le contenu ou la représentation d'un jeton.

# Parser

### Parse Variable declarition {#parse-variable-declarition .unnumbered}

``` {.python mathescape="" linenos="" bgcolor="bg"}
    def ParseVariableDeclaration(self):
        VariableDeclarations= []
        variablesPosition = []
        expected = Tokens.ConstKeyword if \ 
        self.current().getType() == Tokens.ConstKeyword \
        else Tokens.VarKeyword
        keyword = self.MatchToken(expected)
        identifier = self.MatchToken(Tokens.IdentifierToken)
        deletePos = self.__position
        enterTest = False
        while True :
            if self.current().getType() == Tokens.CommaToken:
                self.MatchToken(Tokens.CommaToken)
                variablesPosition.append(self.__position)
                VariableDeclarations.append(self.MatchToken(Tokens.IdentifierToken))
                enterTest = True
            else :
                break
        equalPos = self.__position
        
        equals = None
        intializer = None
        semiColonToken = None

        if self.current().getType() == Tokens.SemiColonToken :
            equals = None
            intializer = LiteralExpressionSyntax(SyntaxToken\
            (Tokens.NumberToken,0,"",0))
            semiColonToken = self.MatchToken(Tokens.SemiColonToken)
        else :
          equals = self.MatchToken(Tokens.EqualsToken)
          intializer = self.ParseExpression()
          semiColonToken = self.MatchToken(Tokens.SemiColonToken)
        
        if enterTest :

           for i in range(deletePos,equalPos) :
               self.__listTokens[i] = SyntaxToken(Tokens.SpaceToken,i," ",None)
           for item in VariableDeclarations :
               for token in self.__listTokens[self.__position-1:equalPos-1:-1] :
               self.__listTokens.insert(self.__position,token)
               self.__listTokens.insert(self.__position,item)
               self.__listTokens.insert(self.__position,keyword)      
        return VariableDeclarationSyntax(keyword,identifier,equals,\
        intializer,semiColonToken)
```

Cette fonction analyse la déclaration de variables suivant une syntaxe
spécifique après avoir analysé le code source. Nous cherchons d'abord le
mot-clé \"const\" ou \"var\" pour commencer la déclaration de variable.
Ensuite, nous commençons notre analyse à la recherche du jeton
\"identificateur\" qui définit le nom de la variable. Nous vérifions
également la présence du séparateur de virgule afin de pouvoir écrire
plusieurs déclarations de variables sur une seule ligne. Ensuite, nous
vérifions l'existence du jeton \"égal\". Si c'est le cas, nous
commençons l'analyse de l'expression binaire à partir du jeton \"égal\"
jusqu'au jeton point-virgule, qui identifie la fin de la déclaration. À
chaque phase de la déclaration de variable, nous générons une erreur si
l'un des jetons mentionnés ci-dessus est manquant. Remarque : par
défaut, la variable prend la valeur 0 si aucune valeur n'est fournie par
le programmeur. Enfin, nous stockons le résultat dans une classe appelée
\"SyntaxVariableDeclaration\".

## Exemple {#exemple-1 .unnumbered}

le nom de fichier est **test.L3Lang**

``` {.pascal mathescape="" linenos="" bgcolor="bg"}
program testCodeGen;
    var a := 12;
    var c:= a+3;
    write(c);
```

``` {.bash language="bash"}
$ python L3Lang -s test.L3Lang
```

![[]{#fig:SyntaxTree label="fig:SyntaxTree"}
SyntaxTree](tree.png){#fig:SyntaxTree width="0.75\\linewidth"}

## Analyseur de descente prédictive récursive: {#analyseur-de-descente-prédictive-récursive .unnumbered}

L'analyseur de descente récursive est une méthode descendante d'analyse
syntaxique dans laquelle un ensemble de procédures récursives est
utilisé pour traiter les entrées. Une procédure est associée à chaque
non-terminal d'une grammaire. Ici, nous considérons une forme simple
d'analyse de descente récursive appelée Predictive Recursive Descent
Parser, dans laquelle le symbole d'anticipation détermine sans ambiguïté
le flux de contrôle à travers le corps de la procédure pour chaque
non-terminal. La séquence d'appels de procédure lors de l'analyse d'une
string d'entrée définit implicitement un arbre d'analyse pour l'entrée
et peut être utilisée pour créer un arbre d'analyse explicite, si vous
le souhaitez. Dans l'analyse par descente récursive, l'analyseur peut
avoir le choix entre plusieurs productions pour une seule instance
d'entrée, le concept de retour en arrière entre en jeu.\

![[]{#fig:SyntaxTree label="fig:SyntaxTree"}
SyntaxTree](fig05.png)

![[]{#fig:SyntaxTree label="fig:SyntaxTree"}
SyntaxTree](fig06.png)

![[]{#fig:SyntaxTree label="fig:SyntaxTree"}
SyntaxTree](fig07.png)

# Lexer

``` {.python mathescape="" linenos="" bgcolor="bg"}
        match self.current():
                case '\0':
                    self.__type= Tokens.EndOfFileToken
                case '+':
                    self.__type= Tokens.PlusToken
                    self.incPos()
                case '-':
                    self.__type= Tokens.MinusToken
                    self.incPos()
                case '*':
                    self.__type= Tokens.StarToken
                    self.incPos()
                case '/':
                   if self.lookahead() == "*":
                      self.ReadComment()
                   else :
                     self.__type= Tokens.SlashToken
                     self.incPos()
                     .
                     .
                     .
                case '0' | '1' | '2' | '3' | '4' | '5' |'6' | '7' | '8' | '9':
                    self.ReadNumberToken()
                case ' ' | '\t' | '\n' | '\r':
                    self.ReadWhiteSpace()
                case _:
                    if self.current().isalpha() :
                        self.ReadIdentifierOrKeyword()
                    elif self.current().isspace() :
                        self.ReadWhiteSpace()
                    else : 
                        self.__errors.ReportBadCharacter(self.__position, self.current())
                        self.incPos()
```

Dans cette phase, nous transformons le texte en une liste de jetons tels
que **NumberToken**, **StringToken**, etc. en les analysant caractère
par caractère tout en vérifiant les types de jetons {Lexem} fournis.

# Binder

``` {.python mathescape="" linenos="" bgcolor="bg"}
 @staticmethod
    def getBinaryOperators():

        return [
            BoundBinaryOperator(
                Tokens.PlusToken, BoundBinaryOperatorType.Addition, int),
            BoundBinaryOperator(
                Tokens.PlusToken, BoundBinaryOperatorType.StringConcatenation, str),
            BoundBinaryOperator(
                Tokens.MinusToken, BoundBinaryOperatorType.Substraction, int),
            BoundBinaryOperator(
                Tokens.SlashToken, BoundBinaryOperatorType.Division, int),
            BoundBinaryOperator(
                Tokens.StarToken, BoundBinaryOperatorType.Multiplication, int),
                .
                .
                .
            BoundBinaryOperator(
                Tokens.EqualsEqualsToken, BoundBinaryOperatorType.Equals, bool),
            BoundBinaryOperator(
                Tokens.BangEqualsToken, BoundBinaryOperatorType.NotEquals, bool),
```

Le Binder dans la partie du compilateur est responsable de la
vérification des types et de l'analyse sémantique. C'est un conteneur
qui encapsule le parseur pour fournir des informations significatives
sur les différentes branches fournies par le parseur, puis applique une
liste de fonctions pour garantir la présence des noms de variables dans
la portée, effectuer des vérifications de type et faire respecter les
règles de correction.

# Evaluator

``` {.python mathescape="" linenos="" bgcolor="bg"}
     def EvaluateBinaryExpression(self,b):

            left = self.ExpressionResult(b.getLeft())
            right = self.ExpressionResult(b.getRight())
            
            match b.getOp().getType():
                case BoundBinaryOperatorType.Addition:
                    return int(left) + int(right)
                case BoundBinaryOperatorType.Substraction:
                    return int(left) - int(right)
    
                case BoundBinaryOperatorType.Multiplication:
                    return int(left) * int(right)
                case BoundBinaryOperatorType.Division:
                    if int(right) == 0 or int(left) == 0:
                        raise Exception("Cannot devide by 0")
                    return int(left) / int(right)
                case BoundBinaryOperatorType.StringConcatenation :
                    return  str(left) +  str(right)
                case BoundBinaryOperatorType.LogicalAnd:                 
                    return bool(left) and bool(right)
                case BoundBinaryOperatorType.LogicalOr:
                    return bool(left) or bool(right)
                case BoundBinaryOperatorType.Equals:
                    return left == right
                case  BoundBinaryOperatorType.NotEquals:
                    return left != right
                case  BoundBinaryOperatorType.Less:
                    return left < right 
                case  BoundBinaryOperatorType.Greater:
                    return left > right
                case  BoundBinaryOperatorType.GreaterOrEquals:
                    return left >= right
                case  BoundBinaryOperatorType.LessOrEquals:
                    return left <= right
                case _:
                    raise Exception(
                    "Unexpected Binary operator {token}".format(token=b.getOp()))
```

Il s'agit d'un programme qui parcourt directement l'arbre syntaxique et
calcule le résultat de l'arbre syntaxique fourni par le parseur après
l'avoir lié. Il possède plusieurs fonctions pour gérer différents cas
tels que la déclaration de variables, l'évaluation de boucles \"while\",
l'évaluation des instructions \"if\", etc.

# Code Generator

``` {.python mathescape="" linenos="" bgcolor="bg"}
def compile(child, output_file, parent=None, grandparent=None):
    global variables
    if isinstance(child, SyntaxToken):
        with open(output_file, "a") as out:
            match child.getType():
                case Tokens.BlockStatement:
                    out.write("\n")              
                case Tokens.VarKeyword:
                    variable = [e[1] for e in getSibling(parent) if \
                    e[0] == Tokens.IdentifierToken][0]
                    if Tokens.NumberToken in [a.getType()\
                    for a in getAllChildren(parent)]:
                        out.write("int "+str(variable.getText())+"=")
                        variables['int'].append(variable.getText()) 
                    else : 
                        out.write("char* "+str(variable.getText())+"=")
                        variables['char*'].append(variable.getText())
                case Tokens.IdentifierToken:
                    if grandparent.getType() not in {Tokens.WriteFunction, \
                    Tokens.ReadFunction} and \
                    parent.getType() != Tokens.VariableDeclaration:
                        out.write(str(child.getText()))
                case Tokens.EqualsToken:
                    if parent.getType() != Tokens.VariableDeclaration:
                        out.write("=")
                case Tokens.NumberToken:
                    if grandparent.getType() not in {Tokens.WriteFunction, \
                    Tokens.ReadFunction}:
                        out.write(str(child.getValue()))
                case Tokens.TrueKeyword:
                    out.write("1")
                case Tokens.FalseKeyword:
                    out.write("0")
                case Tokens.CloseBraceToken:
                    out.write("}\n")
                    .
                    .
                    .
                case Tokens.ReadKeyword:
                    AllChildren = getAllChildren(parent)
                   
                    pattern = ""
                    varName = []
                    for node in AllChildren:
                        if node.getType() == Tokens.ReadKeyword:
                            out.write("scanf(")
                        elif node.getType() == Tokens.IdentifierToken:
                            varName.append(str(node.getText()))
                            if node.getText() in variables['int']: pattern += "%d"
                            else: pattern += "%s"
                        
                    out.write('"'+pattern+'",&')
                    out.write(',&'.join(map(str,varName)))
                    out.write(")")
```

Cette partie du code est responsable de générer du code C en se basant
sur l'arbre d'analyse syntaxique généré à l'étape précédente, puis le
reconstruire selon la syntaxe C. Ensuite, elle le compile en utilisant
GCC et l'exécute, tout en maintenant une trace des déclarations
multiples et des portées imbriquées.

## Exemple 

le nom de fichier est **test.L3Lang**

``` {.pascal mathescape="" linenos="" bgcolor="bg"}
    program testCodeGen
        var a := 12;
        var b := 14;
        var c:= a+b;
        write("c= ",c,"\n")
```

``` {.bash language="bash"}
$ python L3Lang -c test.L3Lang
```

Ce code sera traduit en code C suivant.

``` {.c mathescape="" linenos="" bgcolor="bg"}
    #include <stdio.h>
    #include <stdlib.h>
    int main(){
        int  a = 12;
        int b = 14;
        int c = a +b;
        print("%s%d%s","c= ",c,"\n");
        return 0;
    }
```

# Execution

``` {.python mathescape="" linenos="" bgcolor="bg"}
def compile(child, output_file, parent=None, grandparent=None):
    global variables
    if isinstance(child, SyntaxToken):
        with open(output_file, "a") as out:
            match child.getType():
                case Tokens.BlockStatement:
                    out.write("\n")              
                case Tokens.VarKeyword:
                    variable = [e[1] for e in getSibling(parent) if \
                    e[0] == Tokens.IdentifierToken][0]
                    if Tokens.NumberToken in [a.getType()\
                    for a in getAllChildren(parent)]:
                        out.write("int "+str(variable.getText())+"=")
                        variables['int'].append(variable.getText()) 
                    else : 
                        out.write("char* "+str(variable.getText())+"=")
                        variables['char*'].append(variable.getText())
                case Tokens.IdentifierToken:
                    if grandparent.getType() not in \
                    {Tokens.WriteFunction, Tokens.ReadFunction} and\
                    parent.getType() != Tokens.VariableDeclaration:
                        out.write(str(child.getText()))
                case Tokens.EqualsToken:
                    if parent.getType() != Tokens.VariableDeclaration:
                        out.write("=")
                case Tokens.NumberToken:
                    if grandparent.getType() not in {Tokens.WriteFunction, \
                    Tokens.ReadFunction}:
                        out.write(str(child.getValue()))
                case Tokens.TrueKeyword:
                    out.write("1")
                case Tokens.FalseKeyword:
                    out.write("0")
                case Tokens.CloseBraceToken:
                    out.write("}\n")
                    .
                    .
                    .
                case Tokens.ReadKeyword:
                    AllChildren = getAllChildren(parent)
                    pattern = ""
                    varName = []
                    for node in AllChildren:
                        if node.getType() == Tokens.ReadKeyword:
                            out.write("scanf(")
                        elif node.getType() == Tokens.IdentifierToken:
                            varName.append(str(node.getText()))
                            if node.getText() in variables['int']: pattern += "%d"
                            else: pattern += "%s"
                        
                    out.write('"'+pattern+'",&')
                    out.write(',&'.join(map(str,varName)))
                    out.write(")")
```

Ce script Python agit comme une interface en ligne de commande pour
notre compilateur, vous permettant de simuler ou de compiler un
programme dans la language **L3Lang**. Lorsque tu exécutes le script
avec certaines options, comme '-s' pour la simulation ou '-c' pour la
compilation, tu dois également fournir le chemin vers le fichier source
que tu veux traiter.

Le script prend ensuite le code source fourni, génère du code en langage
C en fonction de ce dernier, puis le compile en utilisant GCC. Si tu
choisis la simulation ('-s'), le script affiche le résultat de
l'evaluation du programe sans le traduire en langugue sible **C**. En
revanche, si tu choisis la compilation ('-c'), il crée un exécutable et
peut même le lancer automatiquement.

Le script gère également les erreurs et fournit des informations de
diagnostic si quelque chose ne se passe pas comme prévu pendant la
simulation ou la compilation. Il s'agit essentiellement d'un outil
pratique pour expérimenter avec un langage de programmation personnalisé
et voir comment il se comporte lors de la simulation ou de la
compilation.

## Exemple de comlilation 

Linux:

``` {.bash language="bash"}
$ /usr/bin/python3 L3Lang <FLAGS> <INPUT FILE>
```

Windows:

``` {.bash language="bash"}
$ python L3Lang <FLAGS> <INPUT FILE>
```

Ensuite, tu pourras trouver le résultat dans le répertoire \"build\" qui
sera généré automatiquement.

# Supported Feauters

1.  Basic REPL (read-eval-print loop) for an expression evaluator

2.  Added lexer, a parser, evaluator, binder ( to verify the result of
    each statement )

3.  Handle `+`, `-`, `\*`, `/`, `\|\|`, `&&` and parenthesized
    expressions

4.  support `<` , `<=`, `>=`, and `>`

5.  Support `int`, `string`, `bool` Data types.

6.  Print syntax trees ( Tree represenation of the parser )

7.  support unray operators (`-`,`+`)

8.  declare variables : `var` to declare global variables and `const` to
    declare read-only variables

9.  support scopes ( define nested scops using Curly brackets
    `begin`,`end`)

10. support position and Line Numbers

11. support if-statements, while-statements and for-statements

12. support loops :(for, while) and nested loops


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
