import views.python_files.calc
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


Builder.load_file("views/kivy_files/calc.kv")


class MyApp(MDApp):
    def build(self):
        self.title = "calculadora"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("views/kivy_files/main.kv")


MyApp().run()
