from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from views.python_files.HomePage import LandingPage
from views.python_files.LoginPage import TheLoginPage


class WindowManager(ScreenManager):
    pass


sm = WindowManager()


class JackApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        Builder.load_file("views/kivy_files/LoginPage.kv")

        sm.add_widget(TheLoginPage(name="login"))

        return WindowManager()

if __name__ == '__main__':
    JackApp().run()
