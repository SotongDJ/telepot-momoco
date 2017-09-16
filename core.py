import tool, modDatabase, modSearch, modVariables
"""
This is the main part of Momocobot to handle income msg
and reply required msg back to user.

The codes of this file mainly lineage from comme() in momocobot.py.
"""

def hande(msg={},arg={}):
    """ handle received msg
    pass command to excute() for futher action (which is more complex)
    change cache info that store in memory (arg)
    and reply back to user
    """
    mesut=[]
    return {'mesut':mesut,'arg':arg}

def excut(msg={},arg={}):
    """ process  msg
    grab command from hande()
    assign task to other mod
    and reply result back to hande()
    """
    resut=[]
    return {'resut':resut,'arg':arg}
