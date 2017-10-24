class MsgSetti:
    def __init__(self,lingua):
        self.lingua = lingua

        self.warn = open('descri/settiWarn.'+lingua).read()

        self.discard = open('descri/settiDiscard.'+lingua).read()

    def main(self,setti):
        resut = open('descri/settiMain.'+self.lingua).read()
        for n in setti.keys():
            resut = resut.replace('@'+n+'@',keyse.get(n,"____"))
        return resut

    def lista(self,setti):
        resut = open('descri/settiLista.'+self.lingua).read()
        for n in setti.keys():
            resut = resut.replace('@'+n+'@',keyse.get(n,"____"))
        return resut

    def setup(self,keywo):
        resut = open('descri/settiSetup.'+self.lingua).read()
        for n in setti.keys():
            resut = resut.replace('@'+n+'@',keyse.get(n,"____"))
        return resut

    def fins(self,setti):
        resut = open('descri/settiFins.'+self.lingua).read()
        for n in setti.keys():
            resut = resut.replace('@'+n+'@',keyse.get(n,"____"))
        return resut
