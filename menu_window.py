from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

lb_quest = QLabel("Введіть запитання")
lb_cor_ans = QLabel("Введіть вірну відповідь")
lb_wr_ans1 = QLabel("Введіть першу хибну відповідь")
lb_wr_ans2 = QLabel("Введіть другу хибну відповідь")
lb_wr_ans3 = QLabel("Введіть третю хибну відповідь")

le_quest = QLineEdit()
le_cor_ans = QLineEdit()
le_wr_ans1 = QLineEdit()
le_wr_ans2 = QLineEdit()
le_wr_ans3 = QLineEdit()

btn_add = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")

lb_stat = QLabel("Статистика:")
lb_atte = QLabel("Разів відповіли: 0")
lb_cor = QLabel("Вірно відповіли: 0")
lb_sus_rate = QLabel("Успішність: 0%")

btn_back = QPushButton("Назад")

v_layout_menu1 = QVBoxLayout()
v_layout_menu2 = QVBoxLayout()
v_layout_menu3 = QVBoxLayout()

v_layout_menu1.addWidget(lb_quest)
v_layout_menu1.addWidget(lb_cor_ans)
v_layout_menu1.addWidget(lb_wr_ans1)
v_layout_menu1.addWidget(lb_wr_ans2)
v_layout_menu1.addWidget(lb_wr_ans3)

v_layout_menu2.addWidget(le_quest)
v_layout_menu2.addWidget(le_cor_ans)
v_layout_menu2.addWidget(le_wr_ans1)
v_layout_menu2.addWidget(le_wr_ans2)
v_layout_menu2.addWidget(le_wr_ans3)

v_layout_menu3.addWidget(lb_stat)
v_layout_menu3.addWidget(lb_atte)
v_layout_menu3.addWidget(lb_cor)
v_layout_menu3.addWidget(lb_sus_rate)

h_layout_menu1 = QHBoxLayout()
h_layout_menu2 = QHBoxLayout()
h_layout_menu3 = QHBoxLayout()
h_layout_menu4 = QHBoxLayout()

h_layout_menu1.addLayout(v_layout_menu1)
h_layout_menu1.addLayout(v_layout_menu2)

h_layout_menu2.addWidget(btn_add)
h_layout_menu2.addWidget(btn_clear)

h_layout_menu3.addLayout(v_layout_menu3)

h_layout_menu4.addWidget(btn_back)

v_menu_layout = QVBoxLayout()

v_menu_layout.addLayout(h_layout_menu1)
v_menu_layout.addLayout(h_layout_menu2)
v_menu_layout.addLayout(h_layout_menu3)
v_menu_layout.addLayout(h_layout_menu4)