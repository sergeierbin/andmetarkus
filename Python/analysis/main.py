from file_functions import FileFunctions
import csv


def main():
   # file_path = "C:\Users\opilane\Documents\andmetarkus\Python\analysis\request-log.txt"

    print("Hello, World!")

# Siia hakkame lisama koodi, millega testime loodud funktsioone.

# Andmed tekstifailis

# Tekstifailist lugemine
# 1. Loo fail nimega "request-log.txt"
# 2. Lisa sinna käsitsi kolm rida teksti, kus iga uus rida algab reanumbriga.
# 3. Loo tekstiline muutuja "file-content".
# 4. Loe andmed tekstifailist loodud muutujasse.
# 5. Väljasta "file-content" sisu terminali.


filecontent = ""

with open("request-log.txt", encoding='utf-8') as f:
    filecontent = f.read()

print(filecontent)

# 6. Lisa uus tühi järjend "request_log_entries".
# 7. Täienda programmikoodi, kus tekstifaili iga rida. pannakse eraldi tekstina loodud järjendisse .
# 8. Väljasta terminali tekst "Logifailis on {x} rida."
# 9. Väljasta järjendi sisu terminali nii et iga rea vahel oleks täiendav reavahetus.

request_log_entries = []

with open("request-log.txt", encoding='utf-8') as f:
    for line in f:
        request_log_entries.append(line.strip())
print(f"Logifailis on {len(request_log_entries)} rida.")
print("\n".join(request_log_entries))

# Tekstifaili kirjutamine
# 1. Lisa faili nimega request-log.txt täiendavad 3 uut rida.
# 2. Väljasta uuesti faili sisu terminali.

request_log_entries = []

with open("request-log.txt", encoding='utf-8') as f:
    for line in f:
        request_log_entries.append(line.strip())
print(f"Logifailis on {len(request_log_entries)} rida.")
print("\n".join(request_log_entries))

# Funktsioonide loomine
# 1. Loo uus funkstioon "add_text", mis saab sisendidna faili nime ja lisatava teksti ning see tekst listatakse faili lõppu juurde.


def add_text(filename, text):
    try:
        # Lisa uus rida faili lõppu
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(text + "\n")

        # Loe kogu fail uuesti listiks
        request_log_entries = []
        with open(filename, encoding='utf-8') as f:
            for line in f:
                request_log_entries.append(line.strip())

        # Prindi kokkuvõte
        print(f"Logifailis on {len(request_log_entries)} rida.")
        print("\n".join(request_log_entries))

        return True
    except Exception as e:
        print(f"Viga: {e}")
        return False


add_text("request-log.txt", "7. Seitsmes rida")

# 2. Loo uus funktsioon "return_last_3_rows", mis tagastab viimased 3 faili lisatud rida.
# 3. Mida eelnevast ülesandest võiks eraldi funktsioonidesse paigutada, et koodi saaks korduvalt kasutada?


def return_last_3_rows(filename):
    """Tagasta faili viimased 3 rida listina."""
    try:
        request_log_entries = []
        with open(filename, encoding='utf-8') as f:
            for line in f:
                request_log_entries.append(line.strip())
        return request_log_entries[-3:]
    except Exception as e:
        print(f"Viga lugemisel: {e}")
        return []


if __name__ == "__main__":
    filename = "request-log.txt"

    last_3 = return_last_3_rows(filename)
    print("Viimased 3 rida:")
    print("\n".join(last_3))

# Andmed CSV failis

# 1. Lae andmed failist CustomerTable.csv
# 2. Väljasta laetud andmed terminali
# 3. Täienda programmi koodi ja salvesta laetud andmeted järjendisse "customers", mis sisaldab iga kliendi andmeid eraldi ennikus(tuple).
# 4. Esimene tulpe sisaldab päise andmeid ja järgmised elemendid kliendi andmeid
# # 5. Väljasta järjend "customers" sisu terminali.

# Opens the file.
with open(r'C:\Users\opilane\Documents\andmetarkus\Python\analysis\input\CustomerTable.csv') as csv_file:

    # Saves the file as a csv.reader object and separates the lines in file to lists of strings which were separated by the delimiter.
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Loops over each line in file.
    for row in csv_reader:

        # Prints the list of strings in that line.
        print(row)

# Andmete salvestamine SQL insert käsuna

# 1. Salvesta järjend "customers" andmed faili insert_customers.sql järgnevalt
# 2. Faili esimene rida on "INSERT INTO customers"
# 3. Faili teine rida on "VALUES {"customers" loendi esimene element}"
# 4. Järmine rida VALUES
# 5. Edasi eraldi ridadele "customers" elemendid.
# 6. Iga andmerea lõppu tuleb lisada koma ja viimase andmerea lõppu semikoolon.
# 7. Veendu, et SQL käsk oleks korrektne(sulud jms).

INSERT INTO customers
VALUES {"customers"}

# Funktioonide täiendamine
# 1. Mida eelnevast võiks lahendada funktsioonidena?


if __name__ == "__main__":
    main()
