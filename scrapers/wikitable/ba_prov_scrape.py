import csv
import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Elecciones_provinciales_de_Buenos_Aires_de_2023"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

table = soup.find("span", {"id": "Encuestas_de_opinión"}).find_next("table")

with open("ba_prov_poll_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for row in table.find_all("tr")[1:]:
        columns = row.find_all("td")

        # Check if the row has the expected number of columns
        if len(columns) == 6:
            date = columns[0].get_text().strip()
            polling_firm = columns[1].get_text().strip()
            sample_size = columns[2].get_text().strip().replace(".", "")
            margin_of_error = columns[3].get_text().strip().replace("%", "")
            undecided = columns[4].get_text().strip().replace("%", "")
            peronist_front = columns[5].get_text().strip().replace("%", "")

            writer.writerow([date, polling_firm, sample_size, margin_of_error, undecided, peronist_front])