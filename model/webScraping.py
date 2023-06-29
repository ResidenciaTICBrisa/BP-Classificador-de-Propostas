"""
O beautifulsoup só funciona com sites estaticos, sites como youtube e twitch não funciona

Existem alguns sites que bloqueiam o uso de web scraping, então é necessário utilizar "headers"

"""

import requests
from bs4 import BeautifulSoup

link = "https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/"
header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

info = requests.get(link, headers=header)
site = BeautifulSoup(info.text, "html.parser")

# find_all(): Função que retorna todos os elementos encontrados entre " " no html
search = site.find("div", class_="column", id="proposal_258")

print(search, "\n")