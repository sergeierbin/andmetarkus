import pandas as pd
import requests

url = 'https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php'

response = requests.get(url)
xml_content = response.content


df = pd.read_xml(xml_content, xpath='.//place')

min_temp_row = df[df['tempmin'] - df['tempmin'].min()]
max_temp_row = df[df['tempmax'] == df['tempmax'].max()]

print(min_temp_row)
print(max_temp_row)
