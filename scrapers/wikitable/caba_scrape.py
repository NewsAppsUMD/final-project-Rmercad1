import pandas as pd

url = 'https://es.wikipedia.org/wiki/Elecciones_de_la_Ciudad_Aut%C3%B3noma_de_Buenos_Aires_de_2023'

# Specify header row index
header_row = 0

# Set decimal and thousands separators
decimal = ','
thousands = '.'

tables = pd.read_html(url, header=header_row, decimal=decimal, thousands=thousands)

# table on the page
df = tables[7]

# Rename columns
df.columns = ['Date', 'Pollster', 'Sample', 'Juntos por el Cambio', 'Frente de Todos',
             'La Libertad Avanza', 'Frente de Izquierda', 'Others', 'Blank',
             'Undecided', 'Lead']

# Filter out rows where Date is NaN
df = df[df['Date'].notna()]

# Drop duplicate header row by index
dup_idx = df[df['Date'].str.startswith('Fecha')].index
df = df.drop(dup_idx)

# Save to CSV
df.to_csv('caba_polls.csv', index=False)
