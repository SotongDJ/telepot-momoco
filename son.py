from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

class LoginScreen(GridLayout):

    usnan = ObjectProperty()
    paswd = ObjectProperty()

    usnanTitle = StringProperty()
    paswdTitle = StringProperty()
    
    sumitText = StringProperty()
    usnanText = StringProperty()
    paswdText = StringProperty()

    def sumited(self,taa,tao):
        self.usnanText = taa
        self.paswdText = tao

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.usnanTitle = '名稱'
        self.paswdTitle = '密碼'
        self.sumitText = '提交'
