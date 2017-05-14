import mmcDefauV,pprint
def chooseMode(ligua):
    final = open('descrimmc/'+ligua+'/analiChoose.descri').read()
    return final

def abratioMain(ligua,dicto):
    final = open('descrimmc/'+ligua+'/abratioMain.descri').read()
    final = final.replace('@mode@',dicto.get('mode',''))
    final = final.replace('@dtempo@',dicto.get('dtempo',''))
    final = final.replace('@utempo@',dicto.get('utempo',''))
    final = final.replace('@conde@',dicto.get('conde',''))
    final = final.replace('@conda@',dicto.get('conda',''))
    final = final.replace('@targe@',dicto.get('targe',''))
    return final

def abratioKeywo(ligua,keywo):
    final = open('descrimmc/'+ligua+'/abratioKeywo.descri').read()
    final = final.replace('@keywo@',keywo)
    return final

def abratioResut(ligua,resut):
    print('resut : '+pprint.pformat(resut, compact=True))

    dtempo = resut.get('dtempo','')
    utempo = resut.get('utempo','')
    conda = resut.get('conda','')
    conde = resut.get('conde','')
    targe = resut.get('targe','')
    pri = resut.get('pri',[])
    des = resut.get('des','')
    karen = resut.get('karen','')
    sam = resut.get('sam','')
    par = resut.get('par','')
    kub = resut.get('kub','')
    statik = resut.get('statik','')

    skdic = mmcDefauV.keywo('ssalk')

    a = open('descrimmc/'+ligua+'/abratioResutA.descri').read()
    a = a.replace('@dtempo@',dtempo)
    a = a.replace('@utempo@',utempo)
    a = a.replace('@conde@',conde)
    a = a.replace('@conda@',skdic.get(conda))
    a = a.replace('@targe@',skdic.get(targe))

    b = open('descrimmc/'+ligua+'/abratioResutB.descri').read()
    b = b.replace('@pri@','\n'.join(pri))
    b = b.replace('@des@',des)
    b = b.replace('@karen@',karen)
    b = b.replace('@sam@',sam)
    b = b.replace('@par@',par)
    b = b.replace('@kub@',kub)

    c = open('descrimmc/'+ligua+'/abratioResutC.descri').read()
    c = c.replace('@max@',statik.get('max',''))
    c = c.replace('@karen@',karen)
    c = c.replace('@maxPc@',statik.get('maxPc',''))
    c = c.replace('@max@',statik.get('max',''))
    c = c.replace('@min@',statik.get('min',''))
    c = c.replace('@minPc@',statik.get('minPc',''))
    c = c.replace('@time@',statik.get('time',''))
    c = c.replace('@dafro@',statik.get('dafro',''))

    return [a,b,c]

def atrenMain(ligua,dicto):
    ledic=mmcDefauV.keywo('leve')
    final="""Selection Card
——————————
Mode: """+dicto.get('mode','')+"""
　　——————　　
Set time period:
　Begin: """+dicto.get('dtempo','')+"""
　End: """+dicto.get('utempo','')+"""
(Format of Date: yyyy-mm-dd)
　　——————　　
Target Class:
　"""+dicto.get('conde','')+"""
　From :"""+dicto.get('conda','')+"""
　/change_conda (Top Class)
　　——————　　
Viewing Level:"""+ledic.get(dicto.get('leve',10),'')+"""
　Day View
　/set_Leve_in_Day
　Month View
　/set_Leve_in_Month
　Year View
　/set_Leve_in_Year
——————————
　/Back　/Analysis
"""
    return final

def atrenKeywo(ligua,keywo):
    final="""Keyword Card
——————————
Keyword: """+keywo+"""
　　——————　　
Set time period:
　Begin
　/set_as_dtempo
　End
　/set_as_utempo
　　——————　　
Target Class:
　/set_as_conde
——————————
　/Back
"""
    return final

def atrenResut(ligua,resut):
    print('resut : '+pprint.pformat(resut, compact=True))
    dtempo = resut.get('dtempo','')
    utempo = resut.get('utempo','')
    conda = resut.get('conda','')
    conde = resut.get('conde','')
    graf = resut.get('graf',[])
    des = resut.get('des','')
    karen = resut.get('karen','')
    sam = resut.get('sam','')
    statik = resut.get('statik','')
    skdic = mmcDefauV.keywo('ssalk')
    a = """Analytics Cards
——————————
Between """+dtempo+' and '+utempo+"""
Showing Trend of """+conde+' ('+skdic.get(conda)+')'

    b = """Graph of Trend:
——————————
"""+'\n'.join(graf)+"""

Description:
——————————
"""+des+"""

Total: """+karen+'　'+str(sam)

    c = """Statistics:
——————————
Total: """+karen+'　'+str(sam)+' ('+karen+'　'+str(san)+""")
Average: """+karen+'　'+str(vam)+' ('+karen+'　'+str(van)+""")
Normal (Removed Extreme Value)

Single:
＋Max : """+statik.get('sinMax','')+' '+karen+' '+statik.get('sinMaxPc','')+"""
＋Min : """+statik.get('sinMin','')+' '+karen+' '+statik.get('sinMinPc','')+"""

Overall:
＋Max : """+karen+' '+statik.get('oveMaxPc','')+"""
"""+statik.get('oveMaxDat','')+"""
＋Min : """+karen+' '+statik.get('oveMinPc','')+"""
"""+statik.get('oveMinDat','')+"""

Mode :
＋Times : """+statik.get('time','')+"""
＋Date :
"""+statik.get('modeDat','')+"""
——————————
　/Back
"""
    return [a,b,c]


def disca(ligua):
    final = open('descrimmc/'+ligua+'/analiDisca.descri').read()
    return final
