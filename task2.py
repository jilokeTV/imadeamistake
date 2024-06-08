class Title:
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True
    def hide(self):
        self.appearance = False
        print(self.title, "- приховано")
    def show(self):
        self.appearance = True
        print(self.title, "- відображено")
    def print_status(self,):
        print('Надпис:', self.title)
        print('Розташування:',"(",self.x, self.y,")") 
        print('Видимість:',self.appearance)

winner_1=Title("Дізнатися переможця прямо зараз!", 150, 50)
winner_1.print_status()
winner_2=Title("Переможець може бути тільки один", 150, -100)
winner_2.print_status()
winner_2.hide()