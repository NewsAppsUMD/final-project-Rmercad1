import pandas as pd

url = 'https://es.wikipedia.org/wiki/Elecciones_provinciales_de_Salta_de_2023'

# Specify header row index
header_row = 0

# Set decimal and thousands separators
decimal = ','
thousands = '.'

tables = pd.read_html(url, header=header_row, decimal=decimal, thousands=thousands)

# table on the page
df = tables[4]

# Rename columns
df.columns = ['Date', 'Pollster', 'Partido Identidad Salteña (Gustavo Sáenz)', 'Frente de Todos (Walter Raúl Wayar)', 'Juntos por el Cambio (Miguel Nanni)',
             'Avancemos (Emiliano Estrada)', 'Frente de Izquierda (Gabriel Musa)', 'Others',
             'Blank', 'Undecided']

# Filter out rows where Date is NaN
df = df[df['Date'].notna()]

# Drop duplicate header row by index
dup_idx = df[df['Date'].str.startswith('Fecha')].index
df = df.drop(dup_idx)

# Save to CSV
df.to_csv('salta_polls.csv', index=False)