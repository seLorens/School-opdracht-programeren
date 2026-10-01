# Importeer de benodigde modules
from database_wrapper import Database 
import pprint
import json

## ------- DATABASE CONNECTIE ---------- ##
# parameters voor connectie met de database
db = Database(host="localhost", gebruiker="user", wachtwoord="password", database="sportcompetitie")

# altijd verbinding openen om query's uit te voeren
db.connect()

## ------- SPORTER INLEZEN ---------- ##
# Haal de eigenschappen op uit de database
sporter_id = 2 # dit kan je vervangen door andere personen

# Haal de informatie van de sporter op.
sporter_query = f"SELECT naam, leeftijd, dagen_niet_beschikbaar, vaardigheden, max_inschrijfgeld, conditie, voorkeurssporten, minst_favoriete_sport, voorkeur_buitensport, maximale_aantal_spelers FROM Sporter WHERE id = {sporter_id}";

# haal de geschikte competities op en print deze
eigenschappen_sporter = db.execute_query(sporter_query)[0]
pprint.pp(eigenschappen_sporter)


## ---------- OPDRACHT 2 ---------- ##
# OPDRACHT 2.1
select_query = f"SELECT sport_id, naam, speeldag FROM sportcompetitie WHERE conditie = '{eigenschappen_sporter['conditie']}'"

# OPDRACHT 2.2
select_query = f"SELECT sport_id, naam, speeldag FROM sportcompetitie WHERE min_leeftijd <= {eigenschappen_sporter['leeftijd']}"

# OPDRACHT 2.3 en 2.4 niet relevant

# OPDRACHT 2.5
# # wat als iemand geen voorkeur sporten heeft ingevuld.
# # test de query eens met persoon_2.json
# # TODO - hoe kan je deze error oplossen?
# # met een IF statement
# select_query = f"SELECT naam, conditie, vaardigheden FROM Sportcompetitie" 
# select_query += f"WHERE naam IN("
# voorkeurssporten = eigenschappen_sporter["voorkeurssporten"]
# for i in range(len(voorkeurssporten)):
#     if i > 0:
#         select_query += ", " ## waar dient deze code voor? 
#     select_query += f"'{voorkeurssporten[i]}'"
# select_query += f")"

# OPDRACHT 2.6
SELECT_query = f"SELECT naam, conditie, min_leeftijd, inschrijfgeld FROM sportcompetitie"
select_query += f"WHERE inschrijfgeld <  {eigenschappen_sporter["max_inschrijfgeld"]} or inschrijfgeld = NULL"
select_query += f"ORDER BY inschrijfgeld DESC"

# OPDRACHT 2.7
## test de query eens met persoon_2.json
## doet je query het nog steeds?
select_query = f"SELECT * FROM sportcompetitie "
select_query += f"WHERE "
dagen_niet_beschikbaar = eigenschappen_sporter["dagen_niet_beschikbaar"]
if (len(dagen_niet_beschikbaar) > 0):
    select_query += f"Speeldag NOT IN("
    
    for i in range(len(dagen_niet_beschikbaar)):
        if i > 0:
            select_query += ", "
        select_query += f"'{dagen_niet_beschikbaar[i]}'"
    select_query += f") and "
select_query += f"max_spelers <= {eigenschappen_sporter["maximale_aantal_spelers"]}"
   
    #  for i in range(len(dagen_niet_beschikbaar)):
    #         if i > 0:
    #             select_query += ", "
    #         select_query += f"'{dagen_niet_beschikbaar[i]}'"
    #     select_query += f") AND"
    # select_query += f" max_spelers <= {eigenschappen_sporter["maximale_aantal_spelers"]}"



# OPDRACHT 2.8
select_query = f"SELECT naam, speeldag"
select_query += f"From sportcompetitie"
select_query += f"WHERE "
voorkeurssporten = eigenschappen_sporter["voorkeurssporten"]
if (len(voorkeurssporten) > 0):
    select_query += f"Naam IN ("

    for i in range(len(voorkeurssporten)):
        if i > 0:
            select_query += ", "
        select_query += f"'{voorkeurssporten[i]}'"
    select_query += f") AND "
select_query += f"binnensport IS NOT {eigenschappen_sporter["voorkeur_buitensport"]}"

# select_query = f"SELECT naam, speeldag FROM Sportcompetitie " 
# select_query += f"WHERE "
# voorkeurssporten = eigenschappen_sporter["voorkeurssporten"]
# if (len(voorkeurssporten) > 0):
#     select_query += f"naam IN ("

#     for i in range(len(voorkeurssporten)):
#         if i > 0:
#             select_query += ", " ## waar dient deze code voor? 
#         select_query += f"'{voorkeurssporten[i]}'"
#     select_query += f") AND "
# select_query += f"binnensport IS NOT {eigenschappen_sporter["voorkeur_buitensport"]}"

# OPDRACHT 2.9
# TODO

# OPDRACHT 2.10
# TODO


# print de query om te kijken of hij goed is
print(select_query)

# haal de geschikte competities op en print deze
geschikte_competities = db.execute_query(select_query)
pprint.pp(geschikte_competities)

# altijd verbinding sluiten met de database als je klaar bent
db.close()


## ---------- OPDRACHT 1 ---------- ##
# Met de eigenschappen van de sporter en de sportcompetities in de database ga je een lijst maken met geschikte competities
# Je gaat de volgende gegevens wegschrijven naar een output.json bestand:
#	naam
#	leeftijd
#	dagen_niet_beschikbaar
#	vaardigheden
#	max_inschrijfgeld
#   conditie
#	voorkeurssporten
#   minst_favoriete_sport
#	voorkeur_buitensport
#	maximale_aantal_spelers
# Hieronder een begin...
competities = {
    "sportergegevens" : {
        "naam" : eigenschappen_sporter["naam"],
        "leeftijd" : eigenschappen_sporter["leeftijd"],
        "dagen_niet_beschikbaar": eigenschappen_sporter["dagen_niet_beschikbaar"],
        "vaardigheden" : eigenschappen_sporter["vaardigheden"],
        "max_inschrijfgeld" : eigenschappen_sporter["max_inschrijfgeld"],
        "conditie" : eigenschappen_sporter["conditie"],
        "voorkeurssporten" : eigenschappen_sporter["voorkeurssporten"],
        "minst_favoriete_sport" : eigenschappen_sporter["minst_favoriete_sport"],
        "maximale_aantal_spelers" : eigenschappen_sporter["maximale_aantal_spelers"]
    },
    "geschikte_competities" : geschikte_competities # we stoppen de hele lijst met competities in de JSON (vanaf opdracht 2)
}

# uiteindelijk schrijven we de dictionary weg naar een JSON-bestand
with open('geschikte_competities.json', 'w') as json_bestand_uitvoer:
    json.dump(competities, json_bestand_uitvoer, indent=4)