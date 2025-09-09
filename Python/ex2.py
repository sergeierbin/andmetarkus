# andmed csv failis

import csv

data_from_csv = []

with open(r'C:\Users\opilane\Documents\andmetarkus\Python\analysis\input\CustomerTable.csv', 'r', encoding='utf-8') as file:
    # tekitab reader objekti
    reader = csv.reader(file, delimiter=',')
    # teisendab reader objekti listiks
    data_from_csv = list(reader)

print(data_from_csv)

# esimene rida
insert_statement = "INSERT INTO customers"

# insert_statement + veergude nimed
# insert_statement += pikalt kirjutades insert_statement2 = insert_statement + ....

insert_statement += f"\n({','.join(data_from_csv[0])}) \nVALUES "

# mis väärtused lisada (read kuni eelviimane)
for row in data_from_csv[1:-1]:
    insert_statement += f"\n({','.join(row)}),"

# viimase rea jaoks ei ole koma vajalik
# seega eraldi käsitlus
insert_statement += f"\n({','.join(data_from_csv[-1])});"
print(insert_statement)
