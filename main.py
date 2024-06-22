from PyQt5.QtWidgets import QApplication, QWidget
from main_window import *

app = QApplication([])
win = QWidget()
window_width = 600
window_height = 500

win.resize(window_width,window_height)
win.move(300,300)
win.setWindowTitle("Memory Card")

win.setLayout(main_v_layout)

win.show()
app.exec_()