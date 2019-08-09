#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saad.bendaoud
#
# Created:     05/08/2019
# Copyright:   (c) saad.bendaoud 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from abc import ABC, abstractmethod

class View(ABC):
    def __init__(self):
        super().__init__()
    def startView(self):
        raise Exception("Can't instantiate abstract class View with abstract methods")
    def startNewSession(self,name):
        raise Exception("Can't instantiate abstract class View with abstract methods")
    def startNewSession(self, name):
        raise Exception("Can't instantiate abstract class View with abstract methods")
    def showNumQuestions(self):
        raise Exception("Can't instantiate abstract class View with abstract methods")
    def showQuestions(self,questionsOptions):
        raise Exception("Can't instantiate abstract class View with abstract methods")
    def showAnswer(self,answer, result):
        raise Exception("Can't instantiate abstract class View with abstract methods")
    def showScore(self,score):
        raise Exception("Can't instantiate abstract class View with abstract methods")
    def showErrorNumQuestions(self,lastIndex):
        raise Exception("Can't instantiate abstract class View with abstract methods")
    def endView(self):
        raise Exception("Can't instantiate abstract class View with abstract methods")





