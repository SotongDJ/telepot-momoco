import subprocess, json

def update(targetBot):
    try:
        statfl = open('database/opt/bot.json','r')
        stat = json.load(statfl)
        statfl.close()
    except FileNotFoundError:
        temp = open('bot.json','w')
        temp.close()
        stat = {targetBot+'.py':''}

    if stat[targetBot+'.py'] != '':
        subprocess.call(['kill',stat[targetBot+'.py']])
        subprocess.call(['git','pull'])

    subprocess.call(['pgrep', 'python'], stdout=open('database/opt/bot.pid', 'w'))
    before = open('database/opt/bot.pid').read().splitlines()

    subprocess.Popen(['python3.4', targetBot+'.py'])

    subprocess.call(['pgrep', 'python'], stdout=open('database/opt/bot.pid', 'w'))
    after = open('database/opt/bot.pid').read().splitlines()

    stat[targetBot+'.py'] = ''.join(set(after)).replace(''.join(set(before)),'')
    statfl = open('database/opt/bot.json','w')
    json.dump(stat,statfl)
    statfl.close()
