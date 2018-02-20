import pprint, modArgona

class MsgSaci:
    def __init__(self,lingua='SiMP'):
        self.lingua = lingua

    def setion(self,danno={}):
        resut = open('descri/saciSetion.'+self.lingua).read()
        kassi = danno.get('fikasi','').split('@')
        kessi = danno.get('namnan','').split('@')

        setto = {}
        n = 0
        tabol = True
        while tabol:
            if kessi[n] != '':
                setto.update({ kassi[n] : kessi[n] })
            n = n + 1
            if n >= len(kassi):
                tabol = False
            if n >= len(kessi):
                tabol = False
        udise = danno.get('fudidi',[])
        filta = ''
        if 'datte' in setto.keys():
            filta = filta + '。datte: ' + setto.get('datte') + '\n'
        if 'namma' in setto.keys():
            filta = filta + '。namma: ' + setto.get('namma') + '\n'
        if 'klass' in setto.keys():
            filta = filta + '。klass: ' + setto.get('klass') + '\n'
        if 'shoop' in setto.keys():
            filta = filta + '。shoop: ' + setto.get('shoop') + '\n'

        fobol = False
        frasa = '。From: \n　　[@fromm@] @karen@ @price@\n'
        if 'fromm' in setto.keys():
            frasa = frasa.replace('@fromm@',setto.get('fromm'))
            fobol = True
        else:
            frasa = frasa.replace('@fromm@','　　')
        if 'karen' in setto.keys():
            frasa = frasa.replace('@karen@',setto.get('karen'))
            fobol = True
        else:
            frasa = frasa.replace('@karen@','　　')
        if 'price' in setto.keys():
            frasa = frasa.replace('@price@',setto.get('price'))
            fobol = True
        else:
            frasa = frasa.replace('@price@','　　')
        if fobol:
            filta = filta + frasa

        tobol = False
        frasa = '。To: \n　　[@toooo@] @tkare@ @tpric@\n'
        if 'toooo' in setto.keys():
            frasa = frasa.replace('@toooo@',setto.get('toooo'))
            tobol = True
        else:
            frasa = frasa.replace('@toooo@','　　')
        if 'tkare' in setto.keys():
            frasa = frasa.replace('@tkare@',setto.get('tkare'))
            tobol = True
        else:
            frasa = frasa.replace('@tkare@','　　')
        if 'tpric' in setto.keys():
            frasa = frasa.replace('@tpric@',setto.get('tpric'))
            tobol = True
        else:
            frasa = frasa.replace('@tpric@','　　')
        if tobol:
            filta = filta + frasa

        pprint.pprint(setto)
        print(filta)
        resut = resut.replace('@filta@',filta)

        return resut
