import pandas as pd

url = 'https://es.wikipedia.org/wiki/Anexo:Encuestas_de_intenci%C3%B3n_de_voto_para_las_elecciones_presidenciales_de_Argentina_de_2023'
tables = pd.read_html(url)

# Second table on the page
df = tables[2]
df.to_csv('candidate_polls.csv', index=False)