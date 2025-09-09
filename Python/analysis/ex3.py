import pandas as pd

file_name = r'C:\Users\opilane\Documents\andmetarkus\Python\analysis\input\ProductTable.xlsx'

data = pd.read_excel(file_name)

data_dict = data.to_dict(orient='records')
print(data)
print(data_dict)

file_name1 = r'C:\Users\opilane\Documents\andmetarkus\Python\analysis\input\CustomerTable.csv'

data1 = pd.read_csv(file_name1)

data_dict1 = data1.to_dict(orient='records')
print(data1)
print(data_dict1)


# Andmed Exceli failis

# 1. Importimiseks kasuta panda
# 2. Lae andmed failist ProductTable.xlsx
# 3. Teisenda andmed sõnastiku kujule
# 4. Väljasta andmed teriminali

# Andmed Excelisse (pandas)
# 1. Lae andmed failist CustomerTable.csv
# 2. Salvesta andmed exceli vormingus faili "customers"
