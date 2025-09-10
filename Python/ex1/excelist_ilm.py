import pandas as pd

data = pd.read_excel(
    r'Python\ex1\Tallinn-Harku-2004-2024.xlsx', skiprows=2)
df = pd.DataFrame(data)
df_2024 = df[df['Aasta'] == 2024]
df_2024.to_csv(r'Python\ex1\ilm.csv', index=False)
