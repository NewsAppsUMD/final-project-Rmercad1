import pandas as pd

url = 'https://es.wikipedia.org/wiki/Elecciones_provinciales_de_C%C3%B3rdoba_de_2023'

# Specify header row index
header_row = 0

# Set decimal and thousands separators
decimal = ','
thousands = '.'

try:
    tables = pd.read_html(url, header=header_row, decimal=decimal, thousands=thousands, flavor='bs4')
    valid_tables = []
    
    for table in tables:
        try:
            _ = int(table.columns[0])
            valid_tables.append(table)
        except (ValueError, AttributeError):
            continue
    
    # Print the number of valid tables
    print(f"Number of valid tables on the page: {len(valid_tables)}")
except ValueError as e:
    print(f"Error occurred while parsing HTML tables: {e}")