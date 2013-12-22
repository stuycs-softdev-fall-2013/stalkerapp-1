
from pymongo import Connection
import json,time

c = Connection()
db = c.stalkerapp
users = db.users
#u=users.find({'user':'z'})
#users.insert({'user':'z','pass':'z'})
#users.drop()

# geo routines

# tracking page
# drop inactive for 5 minutes
# get all current

def updateCurrent(name,loc):
    # remove old current
    # add new current
   db.current.remove({'name':name})
   newitem = {'name':name,'timestamp':time.time(),
              'geo':{'type':'Point',
                     'coordinates':loc}}
   db.current.insert(newitem)

def getCurrents():
    return json.dumps([x for x in db.current.find({},{'_id':False})])


def removeOld():
    """
    remove any entries in current that are more than 5  minutes old
    """
    now=time.time()
    toremove = [x for x in db.current.find() if now-x['timestamp']>60*5]  # remove 5 minutes old
    for r in toremove:
        print r


    


# merge like locations that are within a certain rage
# 
# add a location (merge in to closest or add new)




def checkCredentials(username,password):
    res=users.find({"user":username,"pass":password})
    return len([x for x in res])==1

def addUser(username,password):
    res = users.find({'usr':username})
    if len([x for x in res])>0:
        return None
    users.insert({'user':username,'pass':password})
    return (username,password)

if __name__=='__main__':
    removeOld()
