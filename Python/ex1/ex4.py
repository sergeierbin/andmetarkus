## Funkstioonid
## Funkstioon väite tõesuse kontrollimiseks

## Loo fukstioon nimega is_adult, mis võtab parameetriks age täisarvu
## Lisa fingimuslasuse, mis kontrollib kui sisendparameeter on 18 või suurem, siis väljastab tõenäärtuse True, vastasel juhul False
## Testi terminalis funktsiooni väärtust funktsiooni andes sisendiks erinevaid väärtusi
## Lisa funkstiooni kontroll, mis kontrollib kas muutuja on arv ja ei ole negatiivne arv. Kui tuvastatakse viga siis tagastatab funktsioon False
## Testi terminalis funktsiooni väärtust andes funktsiooni sisendiks erinevaid väärtusi
## Loo tingimuslause, mis kasutab vanuse kontrollimiseks funkstiooni is_adult. Kui tõene siis tagastab terminali "Võib Valida" vastasel juhul "Ei või valida".

def is_adult(age: int) -> bool:
    """Kontrollib kas vanus on 18 või suurem ja mitte negatiivne arv."""
    return age >=18
print(is_adult(20))
print(is_adult(17))

age = 20
if is_adult(age):
    print("Võib Valida")
else:
    print("Ei või valida")

## Funkstioon väärtuse olemasolu kontrollimiseks loendis
## Lisa loend eu_northen_country_codes sõnedega DK, EE, FI, IS, LT, LV, NO, SE
## Lisa funktsioon is_northen_country (mis võtab vastu 2 kohalise riigi koodi country_code) ja tagastab kas tõenäärtuse True kui riigi kood on loetelus. vastasel juhul tagastab False.
## Funktsioon peab tagastama alati väärtuse False, kui sisend ei ole kahetäheline string
## Testi terminalis funktsiooni väljundit andes funktsiooni sisendiks erinevaid väärtusi

eu_northen_country_codes = ["DK", "EE", "FI", "IS", "LT", "LV", "NO", "SE"]
def is_northen_country(country_code: str) -> bool:
    """Kontrollib kas riigi kood on Põhjamaade hulgas."""
    if not isinstance(country_code, str) or len(country_code) != 2:
        return False
    return country_code.upper() in eu_northen_country_codes


print(is_northen_country("EE"))
print(is_northen_country("US"))
print(is_northen_country("Est"))
print(is_northen_country(12))