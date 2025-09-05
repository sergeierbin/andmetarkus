## Peamised Python andmestruktuurid
## List (Sõnede järjend)
## Loo uus järjend boys_names mis sisaldab nimesid: Ain, Peeter, Kusti, Karl
boys_names = ["Ain", "Peeter", "Kusti", "Karl"]
## Lisa loodud järjendisse boys_names täiendav nimi "Margus"
boys_names.append("Margus")
print(boys_names)

## Loo uus järjend girl_names mis sisaldab nimesid: Jaanika, Malle, Kersti, Ann
girl_names = ["Jaanika", "Malle", "Kersti", "Ann"]

## Loo uus tühi järjend names
## Lisa sinna elemendid nii boys_names ja ka girl_names kõik elemendid
names = []
names = boys_names + girl_names
print("names:" + str(names))

## Moodusta uus järjend names_sorted, mis sisaldab nimesid sorteeritud tähestiku järjekorras.
## Väljasta Terminali järjend names_sorted
names_sorted = sorted(names)
print("names sorted:" + str(names_sorted))

## Väljasta Terminali mis väärtused tagastavad meetodid max(), min() järjendi girl_names puhul
print (max(girl_names))
print (min(girl_names))

## Väljasta Terminali mitu elementi on järjendis names_sorted
print(len(names_sorted))

## Väljasta Terminali järjendi names_sorted esimene element
print(names_sorted[0])

## Väljasta Terminali järjendi names_sorted viimane element
boys_names.reverse()
print(boys_names)

## Lisa järjendisse boys_names_reverse järjend boys_names pööratud järjekorras
## Väljasta Terminali järjend boys_names_reverse

## Set (Hulk)
## Loo järjend transaction_customer_id
## Lisa sinna väärtused 1, 2, 5, 2, 4, 8
## Trüki loodud järjend välja terminali
transaction_customer_id = [1, 2, 5, 2, 4, 8]
print(transaction_customer_id)

## Loo hulk active_customers kuhu lisad transaction_customer_id väärtused
## Trüki loodud hulk välja terminali
active_customers = set(transaction_customer_id)
print(active_customers)

## Loo hulk all_customers väärtustega 1,2,3,4,5,6,7,8,9,10. Väärtuste loomiseks kasuta funksiooni range()
all_customers = set(range(1,11))
print(all_customers)

## Loo hulk passive_customers kuhu lisad kõik kliendikoodid, mis ei ole tehinguid teinud.
passive_customers = all_customers - active_customers
print(passive_customers)

## Dictionary (Sõnastik)
## Loo uus sõnastik my_company_data, mis sisaldab järgmist infot
## id on 12345678
## name: "Best Analytics Ever"
## mille sees on omakoda sõnastik year_sales väärtustega
## 2023: 12000.00
## 2024: 15000.00
my_company_data = {
    "id": 12345678,
    "name": "Best Analytics Ever",
    "year_sales": {
        2023: 12000.00,
        2024: 15000.00
    }
}

## Väljasta Terminali loodud sõnastik
print(my_company_data)

## Väljasta Terminali my_company_data nimetus
print(my_company_data["name"])

## Väljasta Terminali my_company_data 2023 aasta müügi väärtus kujul "Ettevõtte {Ettevõtte nimi} müük aastal 2023 oli {väärtus} eurot."
print(f"Ettevõtte {my_company_data['name']} müük aastal 2023 oli {my_company_data['year_sales'][2023]} eurot.")

## Muutke ettevõtte nimi ära
my_company_data["name"] = "Uus Nimi OÜ"
print(my_company_data)

## Lisage my_company_data Järjend offices väärtustega Tallinn, Tartu, Helsinki
## Väljasta Terminali muudetud sõnastik

my_company_data.update({"address": "Tartu mnt 1, Tallinn"})
print(my_company_data)

my_company_data["year_sales"][2025] = 40000
print(my_company_data)

## Tuple (Ennik)
## Loo uus ennik popular_boys_names, mis sisaldab nimesid Peeter, Karl
## Väljastage ennik popular_boys_names terminali
popular_boys_names = ("Peeter", "Karl")
print(popular_boys_names)

## Väljastage enniku esimene elemeny popular_boys_names terminali

## Loo uus ennik random_data, mis sisaldab väärtusi: Viis, 5, 5.0

## Väljastage ennik random_data terminali