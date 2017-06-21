from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

    def sumited(self, obj):
        self.usnanOut = Label(text=self.usnanIn.text)
        self.paswdOut = Label(text=self.paswdIn.text)

        self.usnan.clear_widgets()
        self.paswd.clear_widgets()
        self.clear_widgets()

        self.usnan.add_widget(Label(text='User Name'))
        self.usnan.add_widget(self.usnanOut)
        self.add_widget(self.usnan)

        self.paswd.add_widget(Label(text='Password'))
        self.paswd.add_widget(self.paswdOut)
        self.add_widget(self.paswd)

        self.add_widget(Label(text='Summited',size_hint_y=1))


    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.rows = 3
        self.usnan = GridLayout(cols=2,size_hint_y=1)

        self.usnanIn = TextInput(multiline=False)
        self.usnan.add_widget(Label(text='User Name'))
        self.usnan.add_widget(self.usnanIn)
        self.add_widget(self.usnan)

        self.paswd = GridLayout(cols=3,size_hint_y=1)
        self.paswdIn = TextInput(password=True, multiline=False)
        self.paswd.add_widget(Label(text='Password'))
        self.paswd.add_widget(self.paswdIn)
        self.add_widget(self.paswd)

        self.button = Button(text='Sumit',size_hint_y=1)
        self.button.bind(on_release=self.sumited)
        self.add_widget(self.button)
