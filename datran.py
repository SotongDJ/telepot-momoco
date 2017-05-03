import subprocess, json, time

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
        stat = {'momocobot.py':'','trmbot.py':''}

    try:
        print('momocobot.py : '+stat['momocobot.py'])
    except KeyError:
        stat['momocobot.py'] = ''

    try:
        print('trmbot.py : '+stat['trmbot.py'])
    except KeyError:
        stat['trmbot.py'] = ''

    if stat['momocobot.py'] != '':
        subprocess.call(['kill',stat['momocobot.py']])
    if stat['trmbot.py'] != '':
        subprocess.call(['kill',stat['trmbot.py']])

    subprocess.call(['pgrep', 'python'], stdout=open('database/opt/bot.pid', 'w'))
    before = open('database/opt/bot.pid').read().splitlines()

    subprocess.Popen(['python3.4', 'trmbot.py'])
    time.sleep(5)
    subprocess.call(['pgrep', 'python'], stdout=open('database/opt/bot.pid', 'w'))
    after = open('database/opt/bot.pid').read().splitlines()
    stat['trmbot.py'] = ''.join(sorted(after)).replace(''.join(sorted(before)),'')
    time.sleep(10)

    subprocess.call(['pgrep', 'python'], stdout=open('database/opt/bot.pid', 'w'))
    before = open('database/opt/bot.pid').read().splitlines()

    subprocess.Popen(['python3.4', 'momocobot.py'])
    time.sleep(5)
    subprocess.call(['pgrep', 'python'], stdout=open('database/opt/bot.pid', 'w'))
    after = open('database/opt/bot.pid').read().splitlines()
    stat['momocobot.py'] = ''.join(sorted(after)).replace(''.join(sorted(before)),'')

    statfl = open('database/opt/bot.json','w')
    json.dump(stat,statfl)
    statfl.close()
