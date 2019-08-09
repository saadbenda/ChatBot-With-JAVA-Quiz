#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saad.bendaoud
#
# Created:     16/07/2019
# Copyright:   (c) saad.bendaoud 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#classic import
import string
#import MVC
import Controller
import View

class DebugView(View.View):
    def __init__(self):
        pass
    def startView(self):
       print ("Bienvenue sur le chatBot d'Accenture Maroc")
       name = input("Comment t'appelles tu ?")
       Controller.checkName(name)

    def startSession(self, name, score):
        print("Heureux de te revoir %s ! Ton dernier score est de : %s"%(name.capitalize(),score))#capitalize = put the first letter in upper case
        self.showNumQuestions()

        Controller.checkScore(name)

    def startNewSession(self, name):
        print("Bienvenue %s sur le chatBot"%name.capitalize())
        age = input("Quel âge as-tu ? ")
        Controller.newUser(name, age)
        self.showNumQuestions()

        Controller.checkScore(name)

    def showNumQuestions(self):
        numQuestions = input("Combien de questions veux-tu ? ")
        print("Chargement des questions ... ")
        Controller.loadQuestions(numQuestions)

    def showQuestions(self,questionsOptions):
        for q in questionsOptions:
            print('\nQuestion : ', q[1])
            i=0
            options=[]
            for o in q[2]:
                options.append([i,o])
                print('%s : %s'%(i,o))
                i=i+1
            answer = input('Quelle est ta réponse ? ')
            Controller.checkAnswer(q[0], options[int(answer)][1])

    def showAnswer(self,answer, result):
        if result :
            print('Bonne Réponse ! ',answer)
        else:
            print('Mauvaise Réponse ! ',answer)

    def showScore(self,score):
        print("Ton score est de : ",score)
    def showErrorNumQuestions(self,lastIndex):
        print("Tu demandes trop de questions, je n'ai que %s questions à te proposer"%lastIndex)
        showNumQuestions()


    def endView(self):
       print ('\nAurevoir et à Bientôt!')