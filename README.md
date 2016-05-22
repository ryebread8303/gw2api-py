# gw2api-py
Using the Guild Wars 2 api to gather data for a historical analysis of market data
==================================================================================

Files
-----
Run 

> init-tables.py

to create the databases and get the list of item ids and names. Run 

> get-prices.py

to obtain item buy price, sell price, with current day and year.

Database structure
------------------

Within items.db, two tables are generated.
Items(Id INT, Name TEXT, NoSell BOOLEAN)
Prices(Id INT, Buys INT, Sells INT, Day INT, Year INT)


