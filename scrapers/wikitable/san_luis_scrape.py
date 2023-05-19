import pandas as pd

url = 'https://es.wikipedia.org/wiki/Elecciones_provinciales_de_San_Luis_de_2023'

# Specify header row index
header_row = 0

# Set decimal and thousands separators
decimal = ','
thousands = '.'

tables = pd.read_html(url, header=header_row, decimal=decimal, thousands=thousands)

# Ninth table on the page
df = tables[8]

# Rename columns
df.columns = ['Date', 'Pollster', 'Frente de Todos', 'Juntos por el Cambio', 'Frente de Izquierda', 'Movimiento al Socialismo', 'Blank', 'Undecided', 'Lead', 'unnamed', 'unnamed']

# Filter out rows where Date is NaN
df = df[df['Date'].notna()]

# Drop duplicate header row by index
dup_idx = df[df['Date'].str.startswith('Fecha')].index
df = df.drop(dup_idx)

# Save to CSV
df.to_csv('san_luis_polls.csv', index=False)
