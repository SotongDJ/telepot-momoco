from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

    usnan = ObjectProperty()
    paswd = ObjectProperty()
    usnanIn = ObjectProperty()
    paswdIn = ObjectProperty()
    resut = ObjectProperty()
    usnanOut = StringProperty()
    paswdOut = StringProperty()

    def sumited(self, obj):
        self.resut.usnanOut = self.usnanIn.text
        self.resut.paswdOut = self.paswdIn.text

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.rows = 4
        self.usnan = GridLayout(cols=2)

        self.usnanIn = TextInput(multiline=False)
        self.usnan.add_widget(Label(text='名稱'))
        self.usnan.add_widget(self.usnanIn)
        self.add_widget(self.usnan)

        self.paswd = GridLayout(cols=2)
        self.paswdIn = TextInput(password=True, multiline=False)
        self.paswd.add_widget(Label(text='密碼'))
        self.paswd.add_widget(self.paswdIn)
        self.add_widget(self.paswd)

        self.button = Button(text='提交')
        self.button.bind(on_release=self.sumited)
        self.add_widget(self.button)

        self.usnanOut = ''
        self.paswdOut = ''

        self.result = GridLayout(cols=2)
        self.result.add_widget(Label(text='名稱：'+self.usnanOut))
        self.result.add_widget(Label(text='密碼：'+self.paswdOut))
        self.add_widget(self.result)
