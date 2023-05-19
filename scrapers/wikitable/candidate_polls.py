import pandas as pd
import requests
import os

# Define the scraping and updating function
def scrape_and_update():
    url = 'https://es.wikipedia.org/wiki/Anexo:Encuestas_de_intenci%C3%B3n_de_voto_para_las_elecciones_presidenciales_de_Argentina_de_2023'

    # Specify header row index
    header_row = 0

    # Set decimal and thousands separators
    decimal = ','
    thousands = '.'

    tables = pd.read_html(url, header=header_row, decimal=decimal, thousands=thousands)

    # table on the page
    df = tables[2]

    # Rename columns
    df.columns = ['Date', 'Pollster', 'Sample', 'Fernández(FdeT)', 'C. Kirchner (FdeT)',
                  'Scioli (FdeT)', 'Kicillof (FdeT)', 'Massa (FdeT)', 'Larreta (JXC)',
                  'Macri (JXC)', 'Bullrich (JXC)', 'Vidal (JXC)', 'Manes (JXC)',
                  'Lousteau (JXC)', 'Morales (JXC)', 'Millei (LLA)', 'Del Caño (FIT-U)',
                  'Espert (AL)', 'Schiaretti (PF)', 'Others', 'Blank', 'Undecided']

    # Filter out rows where Date is NaN
    df = df[df['Date'].notna()]

    # Remove rows containing specific words
    df = df[~df.astype(str).apply(lambda x: x.str.contains('anuncia|se lanza|Villarruel', case=False)).any(axis=1)]

    # Drop specified columns
    columns_to_drop = ['Fernández(FdeT)', 'C. Kirchner (FdeT)', 'Lousteau (JXC)', 'Manes (JXC)', 'Espert (AL)', 'Macri (JXC)', 'Vidal (JXC)']
    df = df.drop(columns_to_drop, axis=1)

    # Drop duplicate header row by index
    dup_idx = df[df['Date'].str.startswith('Fecha')].index
    df = df.drop(dup_idx)

    # Save to CSV
    csv_file = 'candidate_polls.csv'
    df.to_csv(csv_file, index=False)

    # Update Datawrapper table using the Datawrapper API
    datawrapper_table_id = 'UkZzQ'
    api_key = os.environ['DATAWRAPPERAPI']
    update_url = f'https://api.datawrapper.de/v3/charts/UkZzQ/data'

    # Read the CSV file
    with open(csv_file, 'rb') as file:
        csv_data = file.read()

    # Prepare headers with API key
    headers = {
        'Authorization': api_key,
        'Content-Type': 'text/csv'
    }

    # Make the API request to update the Datawrapper table
    response = requests.put(update_url, headers=headers, data=csv_data)

    # Check the response status
    if response.status_code == 200:
        print('Datawrapper table updated successfully.')
    else:
        print(f'Error updating Datawrapper table. Status code: {response.status_code}')
        print(response.text)

scrape_and_update()
