# List
# Loo fail ex9.py
# Moodusta eraldi loend names_starting_with_a kuhu lisad a tähega algavad nimed loendist names_sorted (kasuta list comprehensionit)
names_sorted = ["Anna", "Kati", "Mari", "Jaanika", "Malle", "Kersti", "Ann"]

# Moodusta eraldi loend names_containing_a kuhu lisad a tähte sisaldavad nimed loendist names_sorted (kasuta list comprehensionit)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# nimed mis on lühemad kui 4 tm
names_shorter_than_4 = [name for name in names_sorted if len(name) < 4]
print(names_shorter_than_4)
