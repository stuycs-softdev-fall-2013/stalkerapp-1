
from pymongo import Connection

c = Connection()
db = c.stalkerapp
users = db.users
#u=users.find({'user':'z'})
#users.insert({'user':'z','pass':'z'})
#users.drop()


# lookup
# add
# drpop
def checkCredentials(username,password):
    res=users.find({"user":username,"pass":password})
    return len([x for x in res])==1

def addUser(username,passw0rd):
    res = users.find({'usr':username})
    if len([x for x in res])>0:
        return None
    
    users.insert({'user':username,'pass':password})
    return (username,password)

print checkCredentials('z','fffff')
print checkCredentials('z','z')
print checkCredentials('a','fffff')
