import pandas as pd
from spacy.tokens import DocBin
import spacy
import re
import sys, getopt, os

def to_spacy(df, outfile):
  nlp = spacy.blank("pt")
  # nlp = spacy.load('pt_core_news_sm')
  db = DocBin()

  for _, row in df.iterrows():
    doc = nlp(row['Corpo'])
    doc.cats = {category: 0 for category in df['Tema'].unique()}
    doc.cats[row['Tema']] = 1
    db.add(doc)
  db.to_disk(outfile)

def arguments(argv):
  args = dict()
  args['dir-destination'] = './'
  args['help'] = f'{argv[0]} -s <source-file> -d <destination-dir>'

  try:
    opts, _ = getopt.getopt(argv[1:], 'hs:d:', ['help', 'source=', 'destination='])
  except:
    print(args['help'])
    sys.exit(2)

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print(args['help'])
      sys.exit(2)
    elif opt in ("-s", "--source"):
      args['file'] = arg
    elif opt in ("-d", "--destination"):
      args['dir-destination'] = arg

  return args

def main(args):
  # DATA EXTRACTION
  # Info: O dataset tem 3519 propostas. A quantidade de propostas com temas não-nulos são 3241.
  try:
    data = pd.read_csv(args['file'])
  except:
    print('You must pass the source file for the preparation! More info, run the script with "-help".')
    sys.exit(2)

  # A coluna de Ministérios tem info semelhante à coluna Tema, porém com mais valores nulos 
  # data_minis = data[['Ministério', 'Corpo']]
  data = data[['Tema', 'Corpo']]


  ## Ajustando coluna Tema
  data.dropna(subset=['Tema'], inplace=True)  # Removendo colunas nulas
  data.drop(data[data['Tema'] == 'Tema '].index, inplace=True)  # Removendo coluna "Tema "

  temas = data['Tema'].unique() # Pegando valores únicos
  temas = dict(enumerate(temas, 0)) # Convertendo para dict (com índices enumerados)
  temas = {v:k for k,v in temas.items()}  # Trocando chaves e valores

  data['id_tema'] = data['Tema'].map(temas) # Inserindo coluna de índices dos temas no Dataframe
  
  ## Ajustando textos da coluna Corpo
  data['Corpo'] = data['Corpo'].apply(lambda text: re.sub('<[^<]+?>', '', text))  # Remove tags html
  # TODO: remover links
  # TODO: remover stop_words?

  # Shuffling the data
  data = data.sample(frac=1)

  # OUTPUTTING
  # Creating folder (if necessary) for train/dev/test (60%, 30%, 10%) files
  # TODO: Salvar os dados separados para validação cruzada?
  if os.path.isdir(args['dir-destination']) is False:
    os.mkdir(args['dir-destination'])
  
  dir_destin = args['dir-destination']
  dir_destin += '/' if dir_destin[-1] != '/' else '' 

  # Separating and saving data into files
  print(f'Saving spaCy files into: {dir_destin}')
  train = int((len(data) * 6) / 10)
  dev = int((len(data) * 3) / 10)

  # Retirar caso o spaCy não seja utilizado para treino
  to_spacy(data[0:train], dir_destin + 'train.spacy')
  to_spacy(data[train: train+dev], dir_destin + 'dev.spacy')
  to_spacy(data[train+dev:], dir_destin + 'test.spacy')


if __name__ == "__main__":
  args = arguments(sys.argv)
  main(args)