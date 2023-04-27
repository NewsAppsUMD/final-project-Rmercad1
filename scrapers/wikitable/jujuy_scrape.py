import pandas as pd

url = 'https://es.wikipedia.org/wiki/Elecciones_provinciales_de_Jujuy_de_2023'

# Specify header row index
header_row = 0

# Set decimal and thousands separators
decimal = ','
thousands = '.'

tables = pd.read_html(url, header=header_row, decimal=decimal, thousands=thousands)

# table on the page
df = tables[3]

# Rename columns
df.columns = ['Date', 'Pollster', 'Frente Cambia Jujuy (Carlos Sadir)', 'Frente de Todos (Rubén Rivarola)', 'Frente de Izquierda (Alejandro Vilca)',
             'Unidad por Jujuy (Juan Cardozo)', 'VIA + PL (Cecilia Casasco)', 'Jujuy tiene Futuro (Rodolfo Tecchi)', 'Others',
             'Blank', 'Undecided']

# Filter out rows where Date is NaN
df = df[df['Date'].notna()]

# Drop duplicate header row by index
dup_idx = df[df['Date'].str.startswith('Fecha')].index
df = df.drop(dup_idx)

# Save to CSV
df.to_csv('jujuy_polls.csv', index=False)