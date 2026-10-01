# import modulen
from pathlib import Path
import json
import pprint
from database_wrapper import Database


# -----------------------------------------
# Database initialisatie en verbinden
# -----------------------------------------
# parameters voor connectie met de database
db = Database(host="localhost", gebruiker="user", wachtwoord="password", database="sportcompetitie")
# altijd verbinding openen om query's uit te voeren
db.connect()


# -----------------------------------------
# Haal de eigenschappen op van een bezoeker
# -----------------------------------------

# SQL-query om alle gegevens van één personeelslid op te halen op basis van het ID.
select_query = f"SELECT * FROM sportcompetitie"
print(select_query)
resultaat = db.execute_query(select_query)
db.close()
# voorbeeld van hoe je bij een eigenschap komt
print(resultaat)
