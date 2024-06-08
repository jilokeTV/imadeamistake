class Title:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.appearance = True
    def hide(self):
        self.appearance = False
        print(self.text, "- приховано")
    def show(self):
        self.appearance = True
        print(self.text, "- відображено")
    def print_status(self):
        print('Надпис:', self.text)
        print('Розташування:',"(",self.x, self.y,")") 
        print('Видимість:',self.appearance)

winner_1=Title("Дізнатися переможця прямо зараз!", 150, 50)
winner_1.print_status()
winner_2=Title("Переможець може бути тільки один", 150, -100)
winner_2.print_status()
winner_2.hide()
