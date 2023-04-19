import requests
from bs4 import BeautifulSoup
import csv

url = "https://es.wikipedia.org/wiki/Anexo:Encuestas_de_intenci%C3%B3n_de_voto_para_las_elecciones_presidenciales_de_Argentina_de_2023"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find_all('table')[0] # select the first table on the page

rows = table.find_all('tr')

# extract table headers
headers = []
for th in rows[0].find_all('th'):
    if th.find('a'):
        headers.append(th.find('a')['title'])
    else:
        headers.append(th.text.strip())

# find the index of the "Encuestadora" column and replace it with "Polling firm"
pollster_index = headers.index("Encuestadora")
headers[pollster_index] = "Polling firm"

# write table headers to CSV file
with open('voting_intentions_spanish.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

# extract table data and write to CSV file
with open('voting_intentions_spanish.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    for row in rows[1:]:
        if row.find('th'):
            data = [row.find('th').text.strip()]
        else:
            data = []
        for td in row.find_all('td'):
            if td.find('a'):
                data.append(td.find('a').get('title', td.text.strip()))
            else:
                data.append(td.text.strip())
        writer.writerow(data)