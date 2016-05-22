#!/usr/bin/python2
import requests,json
import sqlite3 as sql
import sys

def jsonreq(uri):
	return json.loads((requests.get(uri)).text)

baseapi = "https://api.guildwars2.com/v2"
item_list = jsonreq(baseapi+"/items")
pagecount = len(item_list)/200

con = None
con = sql.connect('items.db')
with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Items")
	cur.execute("CREATE TABLE Items(Id INT, Name TEXT,NoSell BOOLEAN)")
	i = 0
	while i < pagecount:
		items = jsonreq(baseapi+"/items?page="+str(pagecount)+"&page_size=200")
		y=0
		while y < 200:
			item_id = items[y]['id']
			item_name = items[y]['name']
			item_nosell = 'NoSell' in items[y]['flags']
			cur.execute("INSERT INTO Items VALUES(?,?,?)",(item_id,item_name,item_nosell))


