import subprocess, json, time, pprint
import tool

def update():
    try:
        statfl = open('database/opt/bot.json','r')
        stat = json.load(statfl)
        statfl = open('database/opt/bot.json','w')
        json.dump({'system':'reopening'},statfl)
        statfl.close()
    except FileNotFoundError:
        subprocess.call(['mkdir','-p','database/opt'])
        temp = open('database/opt/bot.json','w')
        temp.close()
        temp = open('database/opt/bot.pid','w')
        temp.close()
        stat = {'momocobot.py':[],'trmbot.py':[]}
    print('Stage 1 [stat]: '+pprint.pformat(stat))

    try:
        print('momocobot.py : '+pprint.pformat(stat['momocobot.py']))
    except KeyError:
        stat['momocobot.py'] = []
    try:
        print('trmbot.py : '+pprint.pformat(stat['trmbot.py']))
    except KeyError:
        stat['trmbot.py'] = []
    print('Stage 2 [stat]: '+pprint.pformat(stat))

    if stat['momocobot.py'] != []:
        subprocess.call(['pkill','-e','python3.4'])
        stat = {'momocobot.py':[],'trmbot.py':[]}
    elif stat['trmbot.py'] != []:
        subprocess.call(['pkill','-e','python3.4'])
        stat = {'momocobot.py':[],'trmbot.py':[]}
    print('Stage 3 [stat]: '+pprint.pformat(stat))
    stat = {'momocobot.py':[],'trmbot.py':[]}

    subprocess.call(['pgrep','-l','python3'], stdout=open('database/opt/bot.pid', 'w'))
    before = open('database/opt/bot.pid').read().splitlines()
    print('Stage 4 (1/2) trmbot.py [before]:'+pprint.pformat(before))

    subprocess.Popen(['python3.4', 'trmbot.py'])

    subprocess.call(['pgrep','-l','python3'], stdout=open('database/opt/bot.pid', 'w'))
    after = open('database/opt/bot.pid').read().splitlines()
    print('Stage 4 (1/2) trmbot.py [after]'+pprint.pformat(after))
    stat['trmbot.py'] = list(set(after)-set(before))

    print('Stage 4 (1/2) [stat]: '+pprint.pformat(stat))


    subprocess.call(['pgrep','-l','python3'], stdout=open('database/opt/bot.pid', 'w'))
    before = open('database/opt/bot.pid').read().splitlines()
    print('Stage 4 (2/2) momocobot.py [before]:'+pprint.pformat(before))

    subprocess.Popen(['python3.4', 'momocobot.py'])

    subprocess.call(['pgrep','-l','python3'], stdout=open('database/opt/bot.pid', 'w'))
    after = open('database/opt/bot.pid').read().splitlines()
    print('after:'+pprint.pformat(after))
    stat['momocobot.py'] = list(set(after)-set(before))

    print('Stage 4 (2/2) momocobot.py [after]: '+pprint.pformat(stat))

    statfl = open('database/opt/bot.json','w')
    json.dump(stat,statfl)
    statfl.close()

for n in ['bot.json','bot.pid']:
    tool.ckpath('database/opt/',n)
