from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QButtonGroup, QGroupBox, QPushButton, QSpinBox

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
spb_timer = QSpinBox()
spb_timer.setValue(30)
lb_timer = QLabel("хвилин")
lb_q = QLabel('')

RadioGroupBox = QGroupBox("Варіанти відповідей") #frame with QRadioButtons
RadioGroup = QButtonGroup()

rb_1 = QRadioButton('')
rb_2 = QRadioButton('')
rb_3 = QRadioButton('')
rb_4 = QRadioButton('')

RadioGroup.addButton(rb_1)
RadioGroup.addButton(rb_2)
RadioGroup.addButton(rb_3)
RadioGroup.addButton(rb_4)

AnswerBox = QGroupBox("Результат теста")
lb_result = QLabel('') #True/False
lb_correct = QLabel('') #Correct answer

btn_submit = QPushButton('')

v_layout_ans1 = QVBoxLayout()
v_layout_ans2 = QVBoxLayout()
h_layout_ans3 = QHBoxLayout()

v_layout_ans1.addWidget(rb_1)
v_layout_ans1.addWidget(rb_2)
v_layout_ans2.addWidget(rb_3)
v_layout_ans2.addWidget(rb_4)

h_layout_ans3.addLayout(v_layout_ans1)
h_layout_ans3.addLayout(v_layout_ans2)

RadioGroupBox.setLayout(h_layout_ans3)

v_layout_res = QVBoxLayout()
v_layout_res.addWidget(lb_result, alignment=Qt.AlignLeft | Qt.AlignTop)
v_layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter)

AnswerBox.setLayout(v_layout_res)
AnswerBox.hide()

h_layout_1 = QHBoxLayout()
h_layout_2 = QHBoxLayout()
h_layout_3 = QHBoxLayout()
h_layout_4 = QHBoxLayout()

h_layout_1.addWidget(btn_menu)
h_layout_1.addWidget(btn_rest)
h_layout_1.addWidget(spb_timer)
h_layout_1.addWidget(lb_timer)

h_layout_2.addWidget(lb_q, alignment=Qt.AlignCenter)

h_layout_3.addWidget(RadioGroupBox)
h_layout_3.addWidget(AnswerBox)

h_layout_4.addWidget(btn_submit, stretch=2)

main_v_layout = QVBoxLayout()

main_v_layout.addLayout(h_layout_1)
main_v_layout.addLayout(h_layout_2)
main_v_layout.addLayout(h_layout_3)
main_v_layout.addLayout(h_layout_4)