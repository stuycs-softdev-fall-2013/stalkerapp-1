
from pymongo import Connection

c = Connection()
db = c.stalkerapp
users = db.users
#u=users.find({'user':'z'})
#users.insert({'user':'z','pass':'z'})
#users.drop()

# geo routines

# tracking page
# add active - add a new location to active
# drop inactive for 5 minutes
# get all current

# stalking page
# fields have: name location count

# merge like locations that are within a certain rage
# 
# add a location (merge in to closest or add new)

#needs
# drop
def checkCredentials(username,password):
    res=users.find({"user":username,"pass":password})
    return len([x for x in res])==1

def addUser(username,password):
    res = users.find({'usr':username})
    if len([x for x in res])>0:
        return None
    users.insert({'user':username,'pass':password})
    return (username,password)

