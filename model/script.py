import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import zipfile

# Baixar as propostas esta dando erro de certificado ssl
def baixa_propostas(url):
    # Obter o nome do arquivo a partir do link
    file_name = os.path.basename(url)

    # Enviar uma solicitação para obter o conteúdo do arquivo
    response = requests.get(url)

    
    if response.status_code == 200:
        # Caminho completo para o arquivo
        file_path = os.path.join(os.getcwd(), file_name)

        # Salvar o arquivo
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print("Download concluído. Arquivo salvo em:", file_path)
    else:
        print("Falha ao fazer o download do arquivo.")

# Extrai o arquivo zip do brasil participativo
with zipfile.ZipFile('/home/leandro/Documentos/Trabalho/model/brasilparticipativo.presidencia.gov.br-open-data.zip', 'r') as zip_ref:
    for arquivo in zip_ref.namelist():
        if arquivo.endswith('brasilparticipativo.presidencia.gov.br-open-data-proposals.csv'):
            zip_ref.extract(arquivo, '/home/leandro/Documentos/Trabalho/model')
            break
    


# Le as propostas
propostas = pd.read_csv("model/brasilparticipativo.presidencia.gov.br-open-data-proposals.csv", delimiter=";")

#seleciona as colunas que precisa
propostas = pd.DataFrame(propostas, columns=['category/name/pt-BR','title/pt-BR','body/pt-BR'])

#retira as linhas que estao vazias
proposta = propostas.dropna()

# Coluna somente com as propostas
coluna_html = propostas['body/pt-BR']

# retira as tags html da coluna de propostas do csv
texto_extraido = []
for elemento_html in coluna_html:
    soup = BeautifulSoup(elemento_html, 'html.parser')
    texto = soup.get_text()
    texto_extraido.append(texto)

propostas['body/pt-BR'] = texto_extraido  # Sobrescreve a coluna com o texto extraído

#Retorna o novo csv limpo

propostas.to_csv('model/propostas.csv', index=False)

# remove o csv antigo 
os.remove('/home/leandro/Documentos/Trabalho/model/brasilparticipativo.presidencia.gov.br-open-data-proposals.csv')