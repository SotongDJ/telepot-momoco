def admin(id):
    if id == int(open("database/admin").read()):
        return True
    else:
        return False

def check():
    if id == str(open("database/admin").read()):
        return "Admin id is: "+open("database/admin").read()
    else:
        return "No permision"

def id():
    return open("database/admin").read()

def user():
    #list a user list (return  a list of userid)
