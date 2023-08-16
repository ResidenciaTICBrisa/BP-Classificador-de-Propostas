import requests
import zipfile
import io
import os

def download_and_extract_zip(url, output_dir):
    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extractall(output_dir)
            print("sucesso")
    else:
        print("falha")
    
    files_to_delete = [
                        "brasilparticipativo.presidencia.gov.br-open-data-results.csv",
                        "brasilparticipativo.presidencia.gov.br-open-data-result_comments.csv",
                        "brasilparticipativo.presidencia.gov.br-open-data-proposal_comments.csv",
                        "brasilparticipativo.presidencia.gov.br-open-data-projects.csv",
                        "brasilparticipativo.presidencia.gov.br-open-data-meetings.csv",
                        "brasilparticipativo.presidencia.gov.br-open-data-meeting_comments.csv"
    ]

    for file_name in files_to_delete:
        file_path = os.path.join(output_dir, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("arquivo para ser deletado não foi encontrado")

if __name__ == "__main__":
    url = "https://brasilparticipativo.presidencia.gov.br/open-data/download"
    output_dir = "./data_extraction"
    download_and_extract_zip(url, output_dir)