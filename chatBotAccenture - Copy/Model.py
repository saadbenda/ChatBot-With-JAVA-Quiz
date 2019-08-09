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
import json
import string
class User:
    def __init__(self, name, age, score="0"):
        self.name = name
        self.age = age
        self.score=score
    def getName(self):
        return self.name
    def getScore(self):
        return self.score

def checkName(name):
    with open('data/users.json','r+', encoding="utf-8") as file:
        data=json.load(file)#put in a dict
        for index in data:
            if data[index]["name"]==str(name):
                return [True, index]
    return [False]

def loadUser(index):
    with open('data/users.json','r', encoding="utf-8") as file:
        data=json.load(file)
        return(data[index])

def addUser(user):
    with open('data/users.json','r', encoding="utf-8") as file:
        data=json.load(file)
        lastIndex=len(data)
    dict={str(lastIndex): {"name":str(user.name), "age":str(user.age),"score":str(user.score)}}
    data.update(dict)
    with open('data/users.json','w', encoding="utf-8") as file:
        json.dump(data,file,sort_keys=True, indent=4, separators=(',', ': '))

def loadQuestions():
    with open('data/questions_answers.json','r',encoding="utf-8") as f:
        data = json.load(f)
        return data
def addQuestion(question, options, answer, explanation):
    with open('data/questions_answers.json','r', encoding="utf-8") as file:
        data=json.load(file)
        lastIndex=len(data)
        dict={str(lastIndex): {"question":str(question), "options":options,"answer":[str(answer), str(explanation)]}}
        data.update(dict)
    with open('data/questions_answers.json','w', encoding="utf-8") as file:
        json.dump(data,file,sort_keys=True, indent=4, separators=(',', ': '))

def checkAnswer(idQuestion):
    with open('data/questions_answers.json','r',encoding="utf-8") as f:
        data = json.load(f)
        return data[idQuestion]
def updateScore(name, score):
    with open('data/users.json','r', encoding="utf-8") as file:
        data=json.load(file)
        for index in data:
            if data[index]["name"]==str(name):
                data[index]["score"]=str(int(data[index]["score"])+score)
    with open('data/users.json','w', encoding="utf-8") as file:
        json.dump(data,file,sort_keys=True, indent=4, separators=(',', ': '))





