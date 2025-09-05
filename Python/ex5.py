## FOR töötab listi läbi
## WHILE töötab kuni tingimus on täidetud

## Tsükkel FOR kasutamine Pythonis
## Järjendi elementide töötlus FOR tsükli abil
## Loo uus järjend girl_names mis sisaldab nimesid: Jaanika, Malle, Kersti, Ann, Mari, Kati
girl_names = ["Jaanika", "Malle", "Kersti", "Ann", "Mari", "Kati"]
## Kasutades FOR tsüklit väljasta kõik järjendi nimed üks haaval terminali
print("\nLahendus x\n")
for name in girl_names:
    print(name)

## Kasutades FOR tsüklit väljasta järjendi kaks esimest nime terminali
print("\nLahendus x\n")
for name in girl_names  [:2]:
    print(name) 

print("\nLahendus x\n")
for i in range(2):
    print(girl_names)

## Kasutades FOR tsüklit väljasta järjendi teine kuni neljas nimi terminali
print("\nLahendus x\n")
for name in girl_names[1:4]:
    print(name)

## Kasutades FOR tsüklit väljasta kõik järjendi elemendid üks haaval terminali alustades järjendi lõpust (viimasest elemendist)
print("\nLahendus x\n")
for name in reversed(girl_names):
    print(name)

## Kasutades FOR tsüklit ja tingimuslauset väljasta terminali nimed, mis algavad K tähega.
print("\nLahendus x\n")
for name in girl_names:
    if name.startswith('K'):
        print(name)

## 2 nimekirja, kus on sees list, kus on M tähegaalgavad nimed
## Teeme listi
list = []
for name in girl_names:
    if name.startswith('M'):
        print(name)
        list.append(name)
print(list)

sorted_names = {"M":[]}
for name in girl_names:
    if name.startswith('M'):
        print(name)
        list.append(name)
print(sorted_names)
