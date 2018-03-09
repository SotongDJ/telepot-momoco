class Argo:
    def __init__(self):
        super(Argo, self).__init__()
        self.usrdir = ''

        self.temra = {
        "datte":"",
        "namma":"", "klass":"", "shoop":"",
        "fromm":"", "price":"", "karen":"",
        "toooo":"", "tpric":"", "tkare":"",
        "desci":"",
        }

        self.tamta = {
            0 : 'datte',
            1 : 'namma',
            2 : 'klass',
            3 : 'shoop',
            11 : 'fromm',
            12 : 'karen',
            13 : 'price',
            21 : 'toooo',
            22 : 'tkare',
            23 : 'tpric',
            30 : 'desci',
        }

        self.database = {
            'mode' : { 0 : '' },
            'chat' : {
                'chatid' : 0,
                'chattype' : '',
                'content_type' : '',
            },
            'keyword' : '',
            'creo' : {
                'submode' : '',
                'recom' : {},
                'temra' : self.temra,
            },
            'saci' : {
                'submode' : '',
                'setio' : {},
            }
        }

        self.veces = 0

        self.setti = {
            'dinco':'Bank', 'dexpe':'Cash',
            'genis':'Income', 'ovede':'Expense',
            'tanfe':'Transfer', 'incom':'Income',
            'karen':'MYR',
            'defSettWarn':0,
            'screen':13,
            'limit':'',
            'krset':{},
            'lingua':'enMY',
            'natio':'',
        }
