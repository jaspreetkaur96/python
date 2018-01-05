import urllib
import pymongo
import json
from urllib import urlopen
y = "https://news.ycombinator.com/jobs"
page = urlopen(y)

from bs4 import BeautifulSoup

data={}
data['jobs']=[]
soup=BeautifulSoup(page,"lxml")
all_links=soup.find_all("a",class_="storylink")
for x in all_links :
 data['jobs'].append({'title':x.string,'link':x.get("href")})

with open('data.json', 'w') as outfile:  
   json.dump(data, outfile)
#Python is to use store your data in a dict object, which can contain other nested dicts, arrays, booleans, or other primitive types like integers and strings. You can find a more detailed list of data types supported here.
#json.dumps, which returns the actual JSON string instead of sending it directly to a writable object. This can give you some more control if you need to make some changes to the JSON string (like encrypting it, for example).

#connection = pymongo.MongoClient("mongodb://27017")
#db=connection.a
#record1 = db.a_connection 
#p=open('data.json','r')
#parsed=json.loads(p.read())

#for item in parsed :
 #record1.insert(item)

#print x.string,",",x.get("href")
