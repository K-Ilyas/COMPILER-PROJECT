

import sys
from EvaluationResult import EvaluationResult
import threading
import os
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(0, ROOT_DIR+'/syntaxAnalyse')
from Binding.Binder import Binder
from Evaluator import Evaluator

class Compiltaion:
    _globalScope = None

    def __init__(self,previous=None,syntaxTree=None) -> None:

        if syntaxTree == None :
           self.syntaxTree= previous 
           self.previous = None
        else :
           self.previous = previous
           self.syntaxTree= syntaxTree 
           


    def getSyntaxTree(self):
        return self.syntaxTree
    def globalScope(self):

        if self._globalScope == None:
            globalScope = Binder.bindGlobalScope(None if self.previous == None else self.previous.globalScope() , self.syntaxTree.getRoot())
            if self._globalScope is None :
                self._globalScope = globalScope

        return self._globalScope
    
    def ContinueWith(self,syntaxTree):
        return Compiltaion(self,syntaxTree)


    def evaluate(self,variables):

        diagnostics = self.syntaxTree.getErrors().getDiagnostics() + self.globalScope().getDiagnostics().getDiagnostics()
        
        if len(diagnostics) !=0 :
            return EvaluationResult(diagnostics,None)
        evaluator = Evaluator(self.globalScope().getStatement(),variables)
        value = evaluator.result()
        return EvaluationResult([],value)