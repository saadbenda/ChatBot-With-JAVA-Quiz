#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saad.bendaoud
#
# Created:     09/08/2019
# Copyright:   (c) saad.bendaoud 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saad.bendaoud
#
# Created:     19/07/2019
# Copyright:   (c) saad.bendaoud 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import webbrowser
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QEvent, QThread , QMetaType
from PyQt5.QtGui import QTextCursor, QTextBlock

import view.Chat as Chat
import view.Login as Login
import view.Editor as Editor

import View
import Controller
import threading
import time

w=None
answerAvailable = threading.Event()
answer=''
class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.chat = Chat.Ui_Dialog()
        self.chat.setupUi(self)
        self.chat.robot.setPlainText("Bienvenue sur le chatBot d'Accenture Maroc\nComment t'appelles-tu ? " )
        self.chat.human.installEventFilter(self)
        self.chat.GitHub.clicked.connect(lambda: webbrowser.open('https://saadbenda.github.io/ChatBot-With-JAVA-Quiz/')) # connecting the clicked signal with btnClicked slot
        self.chat.Admin.clicked.connect(self.login)
        self.show()

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and
            source is self.chat.human):
            if event.key()==Qt.Key_Enter:
                GuiView.sendAnswer(self)
        return super(AppWindow, self).eventFilter(source, event)


    def login(self):
        self.window=QtWidgets.QMainWindow()
        self.login = Login.Ui_Dialog()
        self.login.setupUi(self.window)
        self.login.connection.clicked.connect(self.checkAdmin)
        self.user=self.login.lineEdit.text()
        self.password=self.login.lineEdit_2.text()
        self.login.connection.clicked.connect(self.checkAdmin)
        self.window.show()

    def questionEditor(self):
        self.window=QtWidgets.QMainWindow()
        self.questions = Editor.Ui_Dialog()
        self.questions.setupUi(self.window)
        self.questions.pushButton.clicked.connect(self.sendQuestion)
        self.window.show()

    def checkAdmin(self):
        user=self.login.lineEdit.text()
        password=self.login.lineEdit_2.text()
        if user=='test' and password=='test':
            self.window.hide()
            self.questionEditor()
    def sendQuestion(self):
        self.question=self.questions.textEdit.toPlainText()
        self.explanation=self.questions.textEdit_2.toPlainText()
        self.optionA=self.questions.lineEdit.text()
        self.optionB=self.questions.lineEdit_2.text()
        self.optionC=self.questions.lineEdit_3.text()
        self.optionD=self.questions.lineEdit_4.text()
        self.options=[self.optionA, self.optionB, self.optionC, self.optionD]
        self.temp=self.questions.lineEdit_5.text()
        print('temp ',self.temp)
        self.answer='ERROR'
        if self.temp=='a':
            self.answer=self.optionA
        elif self.temp== 'b':
            self.answer=self.optionB
        elif self.temp=='c':
            self.answer=self.optionC
        elif self.temp=='d':
            self.answer=self.optionD
        Controller.addQuestion(self.question, self.options, self.answer, self.explanation)
        self.window.hide()

class myThread(QThread):
    signalAvailable = QtCore.pyqtSignal()
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()
        self.quit()

    def run(self):
        while not answerAvailable.is_set():
            time.sleep(5.000)
            print("I'm waiting for your response!")

class GuiView(View.View):
    def __init__(self):
        self.myThread = myThread()

    def startView(self):
        global w
        app = QApplication(sys.argv)
        w = AppWindow()
        w.show()
        w.chat.robot.setPlainText("Bienvenue sur le chatBot d'Accenture Maroc")
        self.getName()
        sys.exit(app.exec_())

    def endView(self):
        w.chat.robot.appendPlainText('\nAurevoir et à Bientôt!')
        time.sleep(1.000)

    def launchThread(self, controllerName):
        if controllerName=='getName':
            self.myThread.finished.connect(self.controllerGetName)
        elif controllerName=='startNewSession':
            print('inside')
            self.myThread.finished.connect(self.controllerStartNewSession)
        self.myThread.start()

    def controllerGetName(self):
        name=str(answer)
        Controller.checkName(name)
        answerAvailable.clear()

    def getName(self):
        w.chat.robot.appendPlainText("\nComment t'appelles tu ?")
        controllerName='getName'
        self.launchThread(controllerName)
    def controllerStartNewSession(self):
        age=str(answer)
        Controller.newUser(name, age)
        GuiView.showNumQuestions(self)
        Controller.checkScore(name)
        answerAvailable.clear()

    def showNumQuestions(self):
        w.chat.robot.setPlainText("Combien de questions veux-tu ? ")

    def startNewSession(self,name):
        controllerName='startNewSession'
        w.chat.robot.setPlainText("Bienvenue %s sur le chatBot"%name.capitalize())
        w.chat.robot.appendPlainText("\nQuel âge as-tu dddd? ")
        answerAvail=False
        self.launchThread(controllerName)

    def startSession(self):
        w.chat.robot.setPlainText("Heureux de te revoir %s ! Ton dernier score est de : %s"%(name.capitalize(),score))
        self.showNumQuestions()

    def sendAnswer(self):
        global answer
        temp=self.chat.human.toPlainText()
        if temp != '':
            self.answer=str(temp)
            answer=temp
            answerAvailable.set()
