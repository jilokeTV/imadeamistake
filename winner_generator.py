from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
win=QWidget()

text=QLabel("Натисніть, щоб дізнатися переможця:")
number=QLabel("?")
button=QPushButton("Згенерувати")

v_line=QVBoxLayout()

v_line.addWidget(text)
v_line.addWidget(number)
v_line.addWidget(button)

win.setLayout(v_line)

def show_winner(num):
    num = randint(1,100)
    number.setText(str(num))
    text.setText("Переможець:")

button.clicked.connect(show_winner)

win.show()
app.exec()