import re

text = "See on Näide! Tekstist, mida normaliseerida:  Õunad, pirnid ja banaanid."

# 1. Väiketähed
text = text.lower()

# 2. Kirjavahemärkide eemaldamine
text = re.sub(r'[^\w\s]', '', text)

# 3. Ülearuste tühikute eemaldamine
text = re.sub(r'\s+', ' ', text).strip()

print(text)
# väljund: see on näide tekstist mida normaliseerida õunad pirnid ja banaanid


text = "Tere!   (Kas sa tuled?)  Ma ei tea...võib-olla,   aga -- vaatame!  Õhtul, kell 18:00, \"Kohvikus\"."

# Eemalda liigsed tühikud (asenda mitu tühikut ühega)
text = re.sub(r'\s+', ' ', text).strip()

text = re.sub(r'[()]', '', text)           # eemaldab kõik sulud
text = re.sub(r'\s+', ' ', text).strip()   # normaliseerib tühikud
text = text.replace('\\"', '')
text = re.sub(r'--', '', text)            # asendab topeltkriipsu ühega
text = re.sub(r'\.\.\.', ',', text)      # asendab kolm punkti kolme punktiga
text = re.sub(r'([!?.,;:])', r'\1 ', text)
text = re.sub(r'\s+', ' ', text).strip()   # normaliseerib tühikud
text = re.sub(r': ', ':', text)      # asendab kolm punkti kolme punktiga
text = re.sub(r'"', '', text)


print(text)
# väljund: Tere! (Kas sa tuled?) Ma ei tea...võib-olla, aga -- vaatame! Õhtul, kell 18:00, \"Kohvikus\"."


sonad = ["    õun", "banaan    ", "    pirn    ", "ploom", "    viinamari    "]
# Eemalda iga sõna algusest ja lõpust tühikud
sonad = [s.strip() for s in sonad]
print(sonad)

puhastatud_sonad = []
for s in sonad:
    puhastatud_sonad.append(s.strip())
    print(puhastatud_sonad)


summad = ["1,234.56", "12,000.00", "5,678.90", "100.00", "23,456.78"]
print('Algne: ', summad)
# [] Moodusta uus järjend, kus summades on eraldatud tuhande eristaja "," ning sõne on teisendatud ujukomaarvuks(float)

summad_ilma_komadeta = [s.replace(',', '') for s in summad]
print('Ilma komadeta: ', summad_ilma_komadeta)

summad_float = [float(s) for s in summad_ilma_komadeta]
print('Float ', summad_float)

summad_1_rida = [float(s.replace(',', '')) for s in summad]
print('1 rida ', summad_1_rida)
