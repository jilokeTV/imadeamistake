from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QHBoxLayout

def uncor():
    msg = QMessageBox()
    msg.setText("Відповідь неправильна")
    msg.exec_()
def cor():
    msg = QMessageBox()
    msg.setText("Відповідь правильна")
    msg.exec_()

app = QApplication([])
win = QWidget()

win.setWindowTitle("Конкурс від Crazy People")
win.resize(350,250)

question = QLabel('В якому році канал отримав "золоту кнопку" від YouTube?')
btn_answer1 = QRadioButton("2005")
btn_answer2 = QRadioButton("2010")
btn_answer3 = QRadioButton("2015")
btn_answer4 = QRadioButton("2020")

v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

h_line1.addWidget(question, alignment=Qt.AlignCenter)
h_line2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
h_line2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
h_line3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
h_line3.addWidget(btn_answer4, alignment=Qt.AlignCenter)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

win.setLayout(v_line)

btn_answer1.clicked.connect(uncor)
btn_answer1.clicked.connect(uncor)
btn_answer1.clicked.connect(cor)
btn_answer1.clicked.connect(uncor)

win.show()
app.exec_()