## Tingimuslause Pythonis
## Tingimuslause millegi kontrollimiseks
## Lisa muutuja age
## Omista muutujale age väärtus 18
age = 18    
## Lisa tingimuslause kui väärtus on 18 või suurem siis väljasta Terminali tekst "Võid hääletada Riigikogu valmistel"
if age >= 18:
    print("Võid hääletada Riigikogu valmistel")
else:
    print("Oled liiga noor, et hääletada Riigikogu valimisteks")
## Käivita programm ja testi väärtust muutes age väärtust
## Lisa tingimuslause kui väärtus on 16 või suurem siis väljasta Terminali tekst "Võid hääletada KOV valmistel"
if age >= 16:
    print("Võid hääletada KOV valmistel")
## Käivita programm ja testi väärtust muutes age väärtust


## Tingimuslause üldine loogika
## Lisa faili muutuja number_to_check
## Lisa tingimuslause
## kui muutuja väärus on alla 100, väljastatakse Terminali tekst "Muutuja väärtus VÄÄRTUS on alla 100"
## kui väärtus on 100 siis väljastatakse Terminali tekst "Muutuja väärtus VÄÄRTUS on täpselt 100"
## kui väärtus on yöe 100 siis väljastatakse Terminali tekst "Muutuja väärtus VÄÄRTUS on üle 100"
## Testi muutuja number_to_check väärtust muutes ja programmi seejärel käivitades kas tingimuslause töötab korrektselt
number_to_check = 100
if number_to_check < 100:       
    print(f"Muutuja väärtus {number_to_check} on alla 100")
if number_to_check == 100:     
    print(f"Muutuja väärtus {number_to_check} on täpselt 100")
if number_to_check > 100:      
    print(f"Muutuja väärtus {number_to_check} on üle 100")


## Tingimuslause if .. else
## Lisa fingimuslasuse, mis kontrollib kas isik on täiskasvanu. Kui vanus on 18 või suurem, siis väljastab teksti "Oled täiskasvanu" kui alla, siis "Ei ole täiskasvanu"
## Testi muutuja age väärtust muutes ja programmi seejärel käivitades kas tingimuslause töötab korrektselt
age = 17
if age >= 18:
    print("Oled täiskasvanu")
else:
    print("Ei ole täiskasvanu")

is_adult = age >= 18
print(F"Kas isik on täiskasvanud? {is_adult}")