import modSearch, auth, pprint
from core import modDatabase, modVariables
usrdir = 'database/usr/'+str(auth.id())
rawdb = modDatabase.opendb(usrdir).get('raw')
defal = modVariables.Argo()
tamta = defal.tamta
ma = input('dynamic(two subject): ')
mam = ma.split(' ')
na = input('static: ')
la = modSearch.exper(usrdir,mam[0]+' '+mam[1]+' '+na)
a = la['resudi']
ia = la['fikasi']
ba = modSearch.exper(usrdir,mam[0]+' '+na)
b = ba['resudi']
bi = ba['fikasi']
ca = modSearch.exper(usrdir,mam[1]+' '+na)
c = ca['resudi']
ci = ca['fikasi']
i=ia+'@'+bi+'@'+ci
ni=i.split('@')
ni=list(set(ni))
d = []
d.extend(a)
d.extend(b)
d.extend(c)
d=sorted(list(set(d)))
print('a:'+mam[0]+' '+mam[1]+' '+na)
print('b:'+mam[0]+' '+na)
print('c:'+mam[1]+' '+na)
nak = ''
for las in sorted(list(tamta)):
    if tamta[las] in ni:
        nak = nak + ':' + tamta[las]
print('kasso'+nak)
for n in d:
    rek = rawdb.get(n)
    if n in a:
        aa='a'
    else:
        aa=' '
    if n in b:
        bb = 'b'
    else:
        bb=' '
    if n in c:
        cc='c'
    else:
        cc=' '

    nok=''
    for las in sorted(list(tamta)):
        if tamta[las] in ni:
            nok = nok + ':' + rek[tamta[las]].replace('\n',' ')
    print(n+':'+aa+bb+cc+nok)
