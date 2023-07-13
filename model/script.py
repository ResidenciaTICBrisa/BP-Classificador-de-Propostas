import pandas as pd
import os
import requests

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

# Exemplo de uso da função
url = "https://brasilparticipativo.presidencia.gov.br/open-data/download"
baixa_propostas(url)

