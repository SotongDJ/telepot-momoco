class MsgMain:
    def __init__(*args, **kwargs):
        super(MsgMain, self).__init__(*args, **kwargs)

    def start(lingua):
        return open('descri/mainStart.'+lingua).read()

    def help(lingua):
        return open('descri/mainHelp.'+lingua).read()

    def bored(lingua):
        return open('descri/mainBored.'+lingua).read()

    def timesout(lingua):
        return open('descri/mainTimesout.'+lingua).read()

    def error(lingua):
        return open('descri/mainError.'+lingua).read()

    def selection(lingua,keyse):
        resut = open('descri/mainSelection.'+lingua).read()
        for n in keyse.keys():
            resut = resut.replace('@'+n+'@',keyse.get(n,"____"))
        return resut

    def home(lingua,keyse):
        resut = open('descri/mainHome.'+lingua).read()
        for n in keyse.keys():
            resut = resut.replace('@'+n+'@',keyse.get(n,"____"))
        return resut
