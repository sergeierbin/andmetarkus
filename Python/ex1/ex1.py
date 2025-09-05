## Python faili loomine ja selle käivitamine VSCode keskkonnas
# ## Lisage kausta ex1.py fail, mis käivitades kasutab Python print() funktsiooni väljastab Terminali tekst "Python töötab" (vajadusel otsi abi built-in methods)
## Käivitage looud fail kasutades VSCode käsklust Run Python File
print('Python töötab');

## Peamised Python andmetüübid
## String (sõne)
## Lisage faili ex1.py kaks muutujat first_name ja surname ja omistage nendele enda ees- ja perenimi
first_name = "Sergei"
surname = "Erbin"

## lisage muujuja full_name, mille väärtus võrdub first_name + surname sõnade (vahel tühik)
full_name = first_name + " " + surname

## väljastage terminali muujuja full_name väärtus kasutades Python print() funktsiooni
print(full_name)

## lisage muutuja full_name_search, mille väärtuseks on full_name kus kõik tähed on suured tähed (vajadusel otsi abi "string methods")
full_name_search = full_name.upper()

## väljastage terminali muujuja full_name_search väärtus kasutades Python print() funktsiooni
print(full_name_search)

## Numbers (int ja float)
## Lisage muutuja age ja omistage sellele täisarvuline väärtus
age = 2025-1988

## Lisage muutuja height ja omistage sellele väärtus täpsusega kaks kohta peale koma
height = 1.88

## Kasutades print ja format string funktsiooni väljastage Terminali tekst "Mu vanus on VANUS ja pikkus on PIKKUS." kus tekstis muutujad VANUS ja PIKKUS asendatakse muutuja väärtusega.
print(f"Mu vanus on {age} ja pikkus on {height}.")
print(full_name[:1])

## Lisage muutuja hashed_name, mis võtab aluseks surname ja kus on asendatud kõik tähed alates teisest tähest väikse nime esitähega.
hashed_name = surname[0] + (len(surname)-1)*surname[0].lower()
print(hashed_name) 

## Lisage muutuja initials, kus on kokku liidetud ees- ja perenimest mõlemast kas esimesest tähte
initials = first_name[:2] + '.'+ surname[:2]+ '.'
print(initials)

print(age * first_name)

boys_names = ["Ain", "Peeter", "Kusti", "Karl"]
print(boys_names)