from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
import pprint

class LoginScreen(GridLayout):

    usnan = ObjectProperty()
    paswd = ObjectProperty()

    usnanTitle = StringProperty()
    paswdTitle = StringProperty()

    sumitText = StringProperty()
    usnanText = StringProperty()
    paswdText = StringProperty()
    closeText = StringProperty()
    usrdir = StringProperty()

    def sumited(self,taa,tao):
        self.usnanText = taa
        self.paswdText = tao

    def close(self):
        App.get_running_app().stop()

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.usnanTitle = 'Name'
        self.paswdTitle = 'Password'
        self.sumitText = 'Sumit'
        self.closeText = 'Close'
