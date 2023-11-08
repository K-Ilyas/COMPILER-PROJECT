

import sys
from EvaluationResult import EvaluationResult

sys.path.insert(0, 'C:/Users/ilyas/Documents/compiler/syntaxAnalyse')
from Binding.Binder import Binder
from Evaluator import Evaluator

class Compiltaion:


    def __init__(self,syntaxTree) -> None:
        self.syntaxTree= syntaxTree 


    def getSyntaxTree(self):
        return self.syntaxTree
    

    def evaluate(self,variables):

        binder = Binder(variables)
        boundExpression = binder.BindExpression(self.syntaxTree.getRoot().getExpression())

        diagnostics = self.syntaxTree.getErrors().getDiagnostics() + binder.getDignostics().getDiagnostics()
        
        if len(diagnostics) !=0 :
            return EvaluationResult(diagnostics,None)
        evaluator = Evaluator(boundExpression,variables)
        value = evaluator.result()
        return EvaluationResult([],value)