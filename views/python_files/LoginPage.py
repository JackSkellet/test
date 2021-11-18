from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from views.python_files.HomePage import LandingPage


class TheLoginPage(MDScreen):

    def verify(self, user, password):
        with open('stuff/Creds.txt', 'r') as f:
            lines = f.readlines()
            usr = lines[0].strip()
            pswd = lines[1].strip()

        if user == usr and password == pswd:
            return True

    def clear(self):
        self.ids.user.text = ""
        self.ids.password.text = ""

    def login(self):
        if self.verify(user=self.ids.user.text, password=self.ids.password.text):
            try:
                from main import sm
                print(sm.current_screen)
                sm.add_widget(LandingPage(name="landingpage"))
                sm.current = "landingpage"
            except Exception as e:
                print(e)

        else:
            print("uh oh")