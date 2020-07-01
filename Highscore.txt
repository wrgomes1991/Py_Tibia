import requests
from bs4 import BeautifulSoup
import json

Worlds = ["Antica", "Assombra", "Astera", "Belluma", "Belobra", "Bona", "Calmera", "Carnera",
          "Celebra", "Celesta", "Concorda", "Cosera", "Damora", "Descubra", "Dibra", "Duna",
          "Emera", "Epoca", "Epoca", "Estela", "Faluna", "Harmonia", "Helera",
          "Honbra", "Impera", "Inabra", "Javibra", "Joenra",
          "Kalibra", "Kenora", "Lobera", "Luminera", "Lutabra", "Macabra", "Menera",
          "Mitigera", "Monza", "Nefera", "Noctera",
          "Nossobra", "Olera", "Ombra", "Pacembra", "Pacera", "Peloria", "Premia",
          "Pyra", "Quelibra", "Quintera", "Refugia",
          "Relania", "Relembra", "Secura", "Serdebra", "Serenebra", "Solidera",
          "Talera", "Torpera", "Tortura", "Unica", "Venebra",
          "Wintera", "Xandebra", "Xylona", "Yonabra", "Ysolera", "Zenobra", "Zuna", "Zunera"]
json_file = open('Highscore.json', 'w')
data = []
for Worldpage in Worlds:
    for Page in range(1, 13):
        page = requests.get(f'https://www.tibia.com/community/?subtopic=highscores&world={Worldpage}'
                            f'&list=experience&profession=0&currentpage={Page}')
        soup = BeautifulSoup(page.content, 'html.parser')
        rows = soup.select('.TableContent tr')
        for row in rows[1:25]:
            columns = row.find_all("td")
            ranking = columns[0].get_text()
            name = columns[1].get_text()
            vocation = columns[2].get_text()
            level = columns[3].get_text()
            points = columns[4].get_text()
            extracted_data = f'{ranking, name, vocation, level, points}'
            json.dump(extracted_data, json_file)