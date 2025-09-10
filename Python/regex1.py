import regex as re

string = 'Tere! Minu telefoninumber on 51234567, kuid töö jaoks kasutan tihti ka vormingut +372 5123 4567. Mõnikord kirjutatakse numbrid ka nii: 372-5123-4567 või isegi (372) 5123 4567. Mõned inimesed lisavad vahele tühikuid, näiteks 51 234 567 või +372-51-234-567. Vanemad kontaktid võivad olla kujul 6 123 456 või 6123456. Palun helista mulle, kui vajad abi!'

matches = re.findall(
    r'(\+372[\s-]?)?(\(?372\)?[\s-]?)?(\d{2,4}[\s-]?\d{3}[\s-]?\d{3,4})', string)
print(matches)
