#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saad.bendaoud
#
# Created:     15/07/2019
# Copyright:   (c) saad.bendaoud 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#classic import
import random
import string
#import MVC
import Model
import DebugView
#import App
import View
import GuiView

score=[0]
i=0

def checkName(name):
    viewList=[DebugView.DebugView(), GuiView.GuiView()]
    view=viewList[i]
    nameExist=Model.checkName(name)[0]
    if nameExist:
        data=Model.loadUser(Model.checkName(name)[1])
        user=Model.User(data["name"], data["age"], data["score"])
        view.startSession(user.name, user.score)
    else:
        view.startNewSession(name)

def newUser(name, age):
    user=Model.User(name, age)
    Model.addUser(user)

def loadQuestions(numQuestions):
    i=0
    viewList=[DebugView.DebugView(), GuiView.GuiView()]
    view=viewList[i]
    questionsOptions=[]
    numQuestions=int(numQuestions)
    questions=Model.loadQuestions()
    lastIndex=len(questions)
    if lastIndex<numQuestions:
        view.showErrorNumQuestions(lastIndex)
    sample=random.sample(range(lastIndex),numQuestions)
    for i in sample:
        l=questions[str(i)]["options"]
        questionsOptions.append([str(i),questions[str(i)]["question"],random.sample(l,len(l))])
    view.showQuestions(questionsOptions)

def checkAnswer(idQuestion, answer):
    i=0
    viewList=[DebugView.DebugView(), GuiView.GuiView()]
    view=viewList[i]
    question=Model.checkAnswer(str(idQuestion))
    q=question["answer"][0].replace(' ','')
    answer=answer.replace(' ','')
    if answer==q:
        result=True
        addScore()
    else:
        result=False
    view.showAnswer(question["answer"][1], result)

def addScore():
    score[0]=score[0]+1

def checkScore(name):
    viewList=[DebugView.DebugView(), GuiView.GuiView()]
    view=viewList[i]
    Model.updateScore(name, score[0])
    view.showScore(score[0])

def addQuestion(question, options, answer, explanation):
    Model.addQuestion(question, options, answer, explanation)

def start(ans):
    viewList=[DebugView.DebugView(), GuiView.GuiView()]
    global i
    if ans=='DebugView':
        i=0
        view=viewList[i]
        view.startView()
        view.endView()
    elif ans=='GuiView':
        i=1
        view=viewList[i]
        view.startView()
        view.endView()


if __name__ == '__main__':
    ans=input('DebugView or GuiView : ')
    start(ans)
