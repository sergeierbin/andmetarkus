import re
riigid = ["Eesti", "Austria", "Belgia", "Andorra",
          "Hispaania", "Soome", "Albaania", "Itaalia"]

# Leida riigid, mis algavad tähega 'A'

for riik in riigid:
    if riik.startswith(("A", "E")):
        print(riik)
# Lisa "A" tähega algavad riigig uue listi

a_riigid = []
for riik in riigid:
    if riik.startswith(("A", "E")):
        a_riigid.append(riik)
print(a_riigid)

for riik in riigid:
    if riik[0] in ("A", "E"):   # esimene täht kuulub hulka
        print(riik)


for riik in riigid:
    if re.match(r'^[AE]', riik):
        print(riik)

valitud = [riik for riik in riigid if riik.startswith(("A", "E"))]
print(valitud)


toidud = {
    "õun": {
        "kalorsus": 52,
        "vitamiinid": ["C", "K", "B6"],
        "mineraalid": ["Kaalium", "Magneesium"],
        "süsivesikud": 14,
        "rasv": 0.2,
        "valk": 0.3
    },
    "banaan": {
        "kalorsus": 89,
        "vitamiinid": ["C", "B6"],
        "mineraalid": ["Kaalium", "Magneesium"],
        "süsivesikud": 23,
        "rasv": 0.3,
        "valk": 1.1
    },
    "kanafilee": {
        "kalorsus": 165,
        "vitamiinid": ["B3", "B6", "B12"],
        "mineraalid": ["Fosfor", "Seleen"],
        "süsivesikud": 0,
        "rasv": 3.6,
        "valk": 31.0
    },
    "kartul": {
        "kalorsus": 77,
        "vitamiinid": ["C", "B6"],
        "mineraalid": ["Kaalium", "Raud"],
        "süsivesikud": 17,
        "rasv": 0.1,
        "valk": 2.0
    },
    "lõhe": {
        "kalorsus": 208,
        "vitamiinid": ["D", "B12", "B6"],
        "mineraalid": ["Seleen", "Fosfor"],
        "süsivesikud": 0,
        "rasv": 13.0,
        "valk": 20.0
    },
    "riis": {
        "kalorsus": 130,
        "vitamiinid": ["B1", "B3", "B6"],
        "mineraalid": ["Magneesium", "Fosfor"],
        "süsivesikud": 28,
        "rasv": 0.3,
        "valk": 2.7
    }
}

"""Mida sõnastikuga on vaja teha:

 Otsida välja kõik toidud, mille mineraalide hulgas on "Kaalium", ja väljasta nende nimed terminali.
 Lisada lisatunnus "makro" väärtusega "süsivesikurohke", "rasvane" kui vastav osakaal makrotoitainetest on üle 50%. Muudel juhtudel lisa tekst "mitmekülgne"
 Otsida välja kõik toidud, mille vitamiinide hulgas on vähemalt kaks B vitamiini ja lisa need uude sõnastikku "b_vitaamini_rikkad"""

# 1. Otsida välja kõik toidud, mille mineraalide hulgas on "Kaalium", ja väljasta nende nimed terminali.
for toit, omadused in toidud.items():
    if "Kaalium" in omadused["mineraalid"]:
        print(toit)

# 2. Lisada lisatunnus "makro" väärtusega "süsivesikurohke", "rasvane" kui vastav osakaal makrotoitainetest on üle 50%. Muudel juhtudel lisa tekst "mitmekülgne"
for omadused in toidud.values():
    sysivesikud = omadused["süsivesikud"]
    rasv = omadused["rasv"]
    valk = omadused["valk"]
    kogus = sysivesikud + rasv + valk
    if kogus == 0:
        omadused["makro"] = "mitmekülgne"
    else:
        if sysivesikud / kogus > 0.5:
            omadused["makro"] = "süsivesikurohke"
        elif rasv / kogus > 0.5:
            omadused["makro"] = "rasvane"
        else:
            omadused["makro"] = "mitmekülgne"
print(toidud)

# 3. Otsida välja kõik toidud, mille vitamiinide hulgas on vähemalt kaks B vitamiini ja lisa need uude sõnastikku "b_vitaamini_rikkad"
b_vitaamini_rikkad = {}
for toit, omadused in toidud.items():
    b_vitamiinide_arv = sum(
        1 for vitamiin in omadused["vitamiinid"] if vitamiin.startswith("B"))
    if b_vitamiinide_arv >= 2:
        b_vitaamini_rikkad[toit] = omadused
print(b_vitaamini_rikkad)
