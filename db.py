from pymongo import Connection
import json,time
# MONGODB_DATABASE

################################################################################
#
#        setting up the database
#
################################################################################

c = Connection()
db = c.stalkerapp
users = db.users

################################################################################
#
#        tracking routines
#
################################################################################


def updateCurrent(name,loc):
   """
   remove the old current for this user
   and add in a new location
   """
   print "HELLO"
   db.current.remove({'name':name})
   print "World"
   newitem = {'name':name,'timestamp':time.time(),
              'geo':{'type':'Point',
                     'coordinates':loc}}
   db.current.insert(newitem)

def getCurrents():
   """
   return everyone logged in right now
   """
   return json.dumps([x for x in db.current.find({},{'_id':False})])


def removeOld():
    """
    remove any entries in current that are more than 5  minutes old
    """
    now=time.time()
    toremove = [x for x in db.current.find() if now-x['timestamp']>60*5]  # remove 5 minutes old
    for r in toremove:
        db.current.remove(r)


    


################################################################################
#
#        User routines
#
################################################################################


def checkCredentials(username,password):
    res=users.find({"user":username,"pass":password})
    return len([x for x in res])==1

def addUser(username,password):
    res = users.find({'usr':username})
    if len([x for x in res])>0:
        return None
    users.insert({'user':username,'pass':password})
    return (username,password)


################################################################################
#
#        main (for testing)
#
################################################################################

if __name__=='__main__':
    removeOld()
