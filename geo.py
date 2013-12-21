from pymongo import Connection
from pymongo import GEO2D
c = Connection()
db = c.geotest
g = db.g
#print g.insert({'name':'home','loc':[40.74901,-73.99952]})
#g.insert({'name':'10th','loc':[40.74960,-74.00280]})
#g.insert({'name':'stuy','loc':[40.71797,-74.01403]})

#print g.create_index([("loc",GEO2D)])

home = g.find({'name':'home'})[0]
loc= home['loc']

f = g.find({'loc':{'$within':{'$center':[loc,.011]}}})

for l in f:
    print l
