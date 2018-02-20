import pprint, modArgona

class MsgSaci:
    def __init__(self,lingua='SiMP'):
        self.lingua = lingua

    def filtan(self,setto={}):
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
        # print(filta)
        return filta

    def resan(self,udidi={}):
        filta = '　'
        if 'datte' in udidi.keys():
            filta = filta + udidi.get('datte') + '\n'

        nabol = False
        frasa = '　'
        if 'namma' in udidi.keys():
            frasa = frasa + udidi.get('namma') + '　'
            nabol = True
        if 'klass' in udidi.keys():
            frasa = frasa + udidi.get('klass') + '　'
            nabol = True
        if 'shoop' in udidi.keys():
            frasa = frasa + udidi.get('shoop') + '　'
            nabol = True
        if nabol:
            filta = filta + frasa + '\n'


        fobol = False
        frasa = '　F: [@fromm@] @karen@ @price@\n'
        if 'fromm' in udidi.keys():
            frasa = frasa.replace('@fromm@',udidi.get('fromm'))
            fobol = True
        else:
            frasa = frasa.replace('@fromm@','　　')
        if 'karen' in udidi.keys():
            frasa = frasa.replace('@karen@',udidi.get('karen'))
            fobol = True
        else:
            frasa = frasa.replace('@karen@','　　')
        if 'price' in udidi.keys():
            frasa = frasa.replace('@price@',udidi.get('price'))
            fobol = True
        else:
            frasa = frasa.replace('@price@','　　')
        if fobol:
            filta = filta + frasa

        tobol = False
        frasa = '　T: [@toooo@] @tkare@ @tpric@\n'
        if 'toooo' in udidi.keys():
            frasa = frasa.replace('@toooo@',udidi.get('toooo'))
            tobol = True
        else:
            frasa = frasa.replace('@toooo@','　　')
        if 'tkare' in udidi.keys():
            frasa = frasa.replace('@tkare@',udidi.get('tkare'))
            tobol = True
        else:
            frasa = frasa.replace('@tkare@','　　')
        if 'tpric' in udidi.keys():
            frasa = frasa.replace('@tpric@',udidi.get('tpric'))
            tobol = True
        else:
            frasa = frasa.replace('@tpric@','　　')
        if tobol:
            filta = filta + frasa
        # print(filta)
        return filta

    def setion(self,danno={},rawdi={}):
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
        # pprint.pprint(setto)

        filta = self.filtan(setto=setto)

        udise = danno.get('fudidi',[])
        resal = ''
        for uuid in udise:
            udidi = rawdi.get(uuid,{})
            for kassi in list(setto.keys()):
                if kassi not in ['fromm','karen','price','toooo','tkare','tpric']:
                    if setto.get(kassi,'-') == udidi.get(kassi,'='):
                        null = udidi.pop(kassi)
            resal = resal + "/uuid" + uuid + "\n"
            resal = resal + self.resan(udidi=udidi)

        resut = resut.replace('@filta@',filta)
        resut = resut.replace('@resal@',resal)

        return resut
