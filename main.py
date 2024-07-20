from PyQt5.QtWidgets import QApplication, QWidget
from random import choice,shuffle
from time import sleep

app = QApplication([])

from main_window import *
from menu_window import *

class Question():
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.attempts = 0
        self.correct = 0
    def got_right(self):
        #print('Це правильна відповідь!')
        self.attempts +=1
        self.correct +=1
    def got_wrong(self):
        #print('Відповідь невірна')
        self.attempts +=1
def show_question(random_question):
    rb_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    shuffle(rb_list)

    answer = rb_list[0]
    wrong_answer1 = rb_list[1]
    wrong_answer2 = rb_list[2]
    wrong_answer3 = rb_list[3]

    lb_quest.setText(random_question.question)
    answer.setText(random_question.answer)
    wrong_answer1.setText(random_question.wrong_answer1)
    wrong_answer2.setText(random_question.wrong_answer2)
    wrong_answer3.setText(random_question.wrong_answer3)

    btn_ok.setText("Відповісти")

def click_OK():
    if btn_ok.text() == 'Відповісти':
        check_answer()
def rest():
    t = spb_timer.value()
    win.hide()
    sleep(t)
    win.show()

def menu():
    m_win.show()
    win.hide()
def back():
    m_win.hide()
    win.show()

q1 = Question('Яблуко','apple','application','pineapple','apply')
q2 = Question('Дім','house','horse','hurry', 'hour')
q3 = Question('Миша','mouse','mouth','muse','museum')
q4 = Question('Число','number','digit','amount','summary')
questions = [q1, q2, q3, q4]
random_question = choice(questions)

############################################

win = QWidget()
window_width = 600
window_height = 500

win.resize(window_width,window_height)
win.move(300,300)
win.setWindowTitle("Memory Card")

win.setLayout(main_v_layout)

############################################

show_question(random_question)
btn_ok.clicked.connect(click_OK)
btn_rest.clicked.connect(rest)
btn_menu.clicked.connect(menu)

win.show()

############################################

m_win = QWidget()
m_win.resize(window_height,window_width)
m_win.move(300,300)
m_win.setLayout(v_menu_layout)
m_win.hide()

############################################
btn_back.clicked.connect(back)

app.exec_()
