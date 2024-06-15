class Widget():
    def __init__(self,text,x_num,y_num):
        self.text = text
        self.x = x_num
        self.y = y_num

    def print_info(self):
        print("Надпис:", self.text)
        print("Розташування:", self.x, self.y)
class Button(Widget):
    def __init__(self, text, x_num, y_num, is_clicked):
        super().__init__(text, x_num, y_num)
        self.is_clicked = is_clicked
    def click(self):
        self.is_clicked = True
        print("Ви зареєстровані")

btn = Button("Брати участь",100,100,False)
btn.print_info()
q = input("Хочете разеєструватися? (так/ні)").lower()
if q == "так":
    btn.click()
else:
    print("А шкода")