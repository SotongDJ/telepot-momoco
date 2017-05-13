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

def abratioResut(resut):
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
    a = """Analytics Cards
——————————
Between """+dtempo+' and '+utempo+"""
Choosing from """+conde+' ('+skdic.get(conda)+"""),
Showing Ratio of """+skdic.get(targe)

    b = """Graph of Ratio:
——————————
"""+'\n'.join(pri)+"""

Description:
——————————
"""+des+"""

Total: """+karen+' '+'　'+sam+' ('+par+'%, '+kub+')'

    c = """Statistics:
——————————
Max : """+statik.get('max','')+' '+karen+' '+statik.get('maxPc','')+"""
Min : """+statik.get('min','')+' '+karen+' '+statik.get('minPc','')+"""

Mode :
＋Times : """+statik.get('time','')+"""
＋Date :
"""+statik.get('dafro','')+"""
——————————
　/Back"""
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

def atrenKeywo(keywo):
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

def atrenResut(resut):
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

Total: """+karen+'　'+sam

    c = """Statistics:
——————————
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


def disca():
    final="""¡ Discard !
——————————

　Closed Statistics Card

——————————
　/whats_now　/setting
"""
    return final
