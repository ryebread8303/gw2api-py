#!/usr/bin/python2
import requests,json
import sqlite3 as sql
import sys

def jsonreq(uri):
	return json.loads((requests.get(uri)).text)

def insertitem(idnum,name,nosell):
	cur.execute("INSERT INTO Items VALUES(?,?,?)",(idnum,name,nosell))

baseapi = "https://api.guildwars2.com/v2"
item_list = jsonreq(baseapi+"/items")
pagecount = len(item_list)/200

con = None

try:
	con = sql.connect('items.db')
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Items")
	cur.execute("DROP TABLE IF EXISTS Prices")
	cur.execute("CREATE TABLE Items(Id INT, Name TEXT,NoSell BOOLEAN)")
	cur.execute("CREATE TABLE Prices(Id INT, Buys INT, Sells INT, Day INT, Year IN)")
	for i in range(pagecount):
		print "Loading page: "+str(i+1)+" of "+str(pagecount)
		items = jsonreq(baseapi+"/items?page="+str(i)+"&page_size=200")
		for item in items:
			item_id = item['id']
			item_name = item['name']
			item_nosell = 'NoSell' in item['flags']
			insertitem(item_id,item_name,item_nosell)
	con.commit()

except sql.Error, e:
	print "Error: %s" %e.args[0]
	sys.exit(1)

finally:
	if con:
		con.close()
