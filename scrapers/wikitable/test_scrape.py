import requests
from bs4 import BeautifulSoup
import csv

url = "https://es.wikipedia.org/wiki/Anexo:Encuestas_de_intenci%C3%B3n_de_voto_para_las_elecciones_presidenciales_de_Argentina_de_2023"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find_all('table')[0]

rows = table.find_all('tr')

# modify table headers to display in English
headers = ['Polling firm', 'Date', 'Sample size', 'Frente de Todos', 'Juntos por el Cambio', 'La Libertad Avanca', 'Consenso Federal', 'Frente de Izquierda', 'Others', 'Blank', 'Undecided', 'Lead']

# write table headers to CSV file
with open('spanish_voting_intentions.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

# extract table data and write to CSV file
with open('spanish_voting_intentions.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    prev_row_cells = None  # initialize previous row cells to None

    for row in rows[1:]:
        if row.find('th'):
            data = [row.find('th').text.strip()]
        else:
            data = []

        # check if previous row cells is None
        if prev_row_cells is None:
            prev_row_cells = len(row.find_all('td'))

        for td in row.find_all('td'):
            if td.find('a'):
                data.append(td.find('a').get('title', td.text.strip()))
            else:
                text = td.text.strip()
                if ',' in text:
                    text = text.replace(',', '.')
                elif '.' in text:
                    text = text.replace('.', '', 1)
                data.append(text)

        # check if current row has fewer cells than previous row
        if len(data) < prev_row_cells:
            num_missing_cells = prev_row_cells - len(data)
            empty_cells = [''] * num_missing_cells
            data = empty_cells + data

        writer.writerow(data)

        # update previous row cells
        prev_row_cells = len(data)