#!/usr/bin/python2
import requests,json,time
import sqlite3 as sql
import sys

def jsonreq(uri):
	return json.loads((requests.get(uri)).text)

def insertitem(idnum,buys,sells,day,year):
	cur.execute("INSERT INTO Prices VALUES(?,?,?,?,?)",(idnum,buys,sells,day,year))

baseapi = "https://api.guildwars2.com/v2"
item_list = jsonreq(baseapi+"/commerce/prices")
pagecount = len(item_list)/200

con = None

try:
	con = sql.connect('items.db')
	cur = con.cursor()
	day = time.gmtime()[7]
	year = time.gmtime()[0]
	for i in range(pagecount):
		print "Loading page: "+str(i+1)+" of "+str(pagecount)
		prices = jsonreq(baseapi+"/commerce/prices?page="+str(i)+"&page_size=200")
		for price in prices:
			item_id = price['id']
			buy = price['buys']['unit_price']
			sell = price['sells']['unit_price']
			insertitem(item_id,buy,sell,day,year)
	con.commit()

except sql.Error, e:
	print "Error: %s" %e.args[0]
	sys.exit(1)

finally:
	if con:
		con.close()
