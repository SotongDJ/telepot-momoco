class MsgMain:
    def __init__(self,lingua):
        self.lingua = lingua

        self.start = open('descri/mainStart.'+lingua).read()

        self.help = open('descri/mainHelp.'+lingua).read()

        self.bored = open('descri/mainBored.'+lingua).read()

        self.timesout = open('descri/mainTimesout.'+lingua).read()

        self.error = open('descri/mainError.'+lingua).read()

    def selection(self,keyse):
        resut = open('descri/mainSelection.'+self.lingua).read()
        for n in keyse.keys():
            resut = resut.replace('@'+n+'@',keyse.get(n,"____"))
        return resut

    def home(self,keyse):
        resut = open('descri/mainHome.'+self.lingua).read()
        for n in keyse.keys():
            resut = resut.replace('@'+n+'@',keyse.get(n,"____"))
        return resut
