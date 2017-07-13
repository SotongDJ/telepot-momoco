import modDatabase, modVariables
def comman(prese,testa):
    usrdir = prese.get('usrdir','')
    lingua = prese.get('lingua','enMY')

    keywo = prese.get('keywo','')
    keyse = prese.get('keyse','')
    primo = prese.get('modli','')
    submo = prese.get('submo','')
    temra = prese.get('temra',modVariables.keywo('temra'))
    recom = prese.get('recom',{})
    chset = prese.get('chset',{})
    stati = prese.get('stati',modVariables.keywo('statics'))
    listi = prese.get('listi',modVariables.keywo('listi'))
    setti = prese.get('setti',modVariables.keywo('setting'))
    karatio = prese.get('karatio',{})

    rawdb = modDatabase.opendb(usrdir).get('raw',{})
    keydb = modDatabase.opendb(usrdir).get('key',{})

    prese.update({ 'resut' : { 'forma' : '', 'conte' : {} } })



    return prese
