def keywo(text):
    dicto= {
        'sf' : {
            "dt":"datte",
            "nm":"namma", "kl":"klass", "sh":"shoop",
            "fr":"fromm", "pr":"price", "kr":"karen",
            "to":"toooo", "tp":"tpric", "tk":"tkare",

            "in":"dinco", "ex":"dexpe",
            "gi":"genis", "oe":"ovede",
            "tf":"tanfe", "ic":"incom",
        },
        'fs' : {
            "datte":"dt",
            "namma":"nm", "klass":"kl", "shoop":"sh",
            "fromm":"fr", "price":"pr", "karen":"kr",
            "toooo":"to", "tpric":"tp", "tkare":"tk",

            "dinco":"in", "dexpe":"ex",
            "genis":"gi", "ovede":"oe",
            "tanfe":"tf", "incom":"ic",
        },
        'klass' : {
            'Acc':['fr','to','in','ex','gi','oe'],
            'Kas':['kl','tf','ic'],
            'Ken':['kr','tk'],
            'Pis':['pr','tp'],
        },
        'ssalk' : {
            "datte":"Date",
            "namma":"e.g Name", "shoop":"e.g. Seller",
            'fromm':'Account','toooo':'Account','dinco':'Account','dexpe':'Account','genis':'Account','ovede':'Account',
            'klass':'Category','tanfe':'Category','incom':'Category',
            'karen':'Currency','tkare':'Currency',
            'price':'Price','tpric':'Price',
        },
    }
    return dicto[text]
