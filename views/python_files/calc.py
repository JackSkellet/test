from logging import root
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.lang import Builder

prev = ""
expression = ""
prox = ""


class calc(Screen):
    out = StringProperty('')
    Window.size = (420, 200)
    Window.minimum_width, Window.minimum_height = Window.size

    def my_callback(self, inpt):
        global prev
        global expression
        global prox

        if inpt == "=":
            prox = str(eval(expression))
            self.out = prox
            expression = ""
            prev = prox


        elif inpt == "ac":
            expression = ""
            prev = ""
            prox = ""
            self.out = expression



        else:
            expression = prev + inpt
            prev = expression
            self.out = expression


class calcApp(MDApp):
    def build(self):
        def press(text):
            print("called: ", text)

        return calc()


if __name__ == '__main__':
    calcApp().run()