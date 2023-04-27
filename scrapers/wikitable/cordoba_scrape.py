import pandas as pd

url = 'https://es.wikipedia.org/wiki/Elecciones_provinciales_de_C%C3%B3rdoba_de_2023'

# Specify header row index
header_row = 0

# Set decimal and thousands separators
decimal = ','
thousands = '.'

tables = pd.read_html(url, header=header_row, decimal=decimal, thousands=thousands)

# table on the page
df = tables[6]

# Rename columns
df.columns = ['Date', 'Pollster', 'Sample', 'Hacemos por Córdoba', 'Juntos por el Cambio',
             'La Libertad Avanva', 'Frente de Todos', 'Frente de Izquierda', 'Others',
             'Blank', 'Undecided', 'Lead']

# Filter out rows where Date is NaN
df = df[df['Date'].notna()]

# Drop duplicate header row by index
dup_idx = df[df['Date'].str.startswith('Fecha')].index
df = df.drop(dup_idx)

# Save to CSV
df.to_csv('corboda_polls.csv', index=False)