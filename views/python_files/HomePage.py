from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen


class WindowManager(ScreenManager):
    pass


sm = WindowManager()


class LandingPage(MDScreen):

    def logout(self):
        sm.current = "login"
        pass

