from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

class LoginScreen(GridLayout):

    usnan = ObjectProperty()
    paswd = ObjectProperty()
    usnanIn = ObjectProperty()
    paswdIn = ObjectProperty()
    resut = ObjectProperty()
    usnanOut = ObjectProperty()
    paswdOut = ObjectProperty()

    usnanText = StringProperty()
    paswdText = StringProperty()
    sumitText = StringProperty()
    uOtext = StringProperty()
    pOtext = StringProperty()

    def sendinu(self,tast):
        self.uOtext = tast
        print(self.uOtext + tast)

    def sendinp(self,tast):
        self.pOtext = tast
        print(self.pOtext + tast)

    def sumited(self,taa,tao):
        self.uOtext = taa
        self.pOtext = tao

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.usnanText = '名稱'
        self.paswdText = '密碼'
        self.sumitText = '提交'
