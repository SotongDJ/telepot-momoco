from core import modDatabase
from core import tool

def listKeywo(usrdir,limit=[]):
    print('modKeywo.listKeywo: '+tool.mask(usrdir))
    keydb = modDatabase.opendb(usrdir).get('key',{})
    resut = {}
    if limit == []:
        limit = ['datte','price','tpric','desci','karen','tkare']
    for kas in keydb.keys():
        if kas not in limit:
            for keywo in keydb.get(kas,{}).keys():
                numon = 0
                metdi = {}
                metse = []

                metdi = resut.get(keywo,{})
                metse = metdi.get(kas,[])
                metse.extend(keydb.get(kas,{}).get(keywo,[]))
                metdi.update({ kas : metse })
                resut.update({ keywo : metdi })
    return resut
