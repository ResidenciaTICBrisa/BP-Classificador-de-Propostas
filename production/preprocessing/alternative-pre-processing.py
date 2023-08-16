import pandas as pd
import spacy
from spacy.tokens import DocBin
from spacy.lang.pt.stop_words import STOP_WORDS
import re
import sys, getopt, os

REGX_URL = r"https?://[A-Za-z0-9./]+" # Regex for URLs
REGX_HTML = r"<[^<]+?>" # Regex for HTML tags

# nlp = spacy.blank('pt')
nlp = spacy.load('pt_core_news_sm') # Testar para comparar

def preprocessing(text):
  text = text.lower()

  text = re.sub(REGX_HTML, '', text)  # Removendo tags HTML
  text = re.sub(REGX_URL, '', text) # Revomendo URLs

  tokens = [t.text for t in nlp(text) if t not in STOP_WORDS and not t.is_punct]

  return ' '.join(tokens)

def to_spacy(df, outfile):
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
  #  Info: O dataset tem 3519 propostas. A quantidade de propostas com temas não-nulos são 3241.
  try:
    data = pd.read_csv(args['file'])
  except:
    print('You must pass the source file for the preparation! More info, run the script with "-help".')
    sys.exit(2)

  #  A coluna de Ministérios tem info semelhante à coluna Tema, porém com mais valores nulos 
  # data_minis = data[['Ministério', 'Corpo']]
  data = data[['Tema', 'Corpo']]


  # PREPROCESSING
  #  Ajustando coluna Tema
  data.dropna(subset=['Tema'], inplace=True)  # Removendo colunas nulas
  data.drop(data[data['Tema'] == 'Tema '].index, inplace=True)  # Removendo coluna "Tema "

  #  Criando índices para temas
  temas = data['Tema'].unique() # Pegando valores únicos
  temas = dict(enumerate(temas, 0)) # Convertendo para dict (com índices enumerados)
  temas = {v:k for k,v in temas.items()}  # Trocando chaves e valores

  data['id_tema'] = data['Tema'].map(temas) # Inserindo coluna de índices dos temas no Dataframe
  
  #  Ajustando textos da coluna Corpo
  data['Corpo'] = data['Corpo'].apply(preprocessing)

  #  Representações vetoriais do texto
  data['Vector'] = data['Corpo'].apply(lambda text: nlp(text).vector)

  #  Embaralhando dados
  data = data.sample(frac=1)

  # OUTPUTTING (experimental; testing training for spaCy)
  # Criando diretórios para arquivos de  train/dev/test (60%, 30%, 10%)
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


# INFO PARA TREINAMENTO COM SPACY
#   A função to_spacy pega cada texto, processa com NLP, insere em um
# DocBin definindo as categorias à qual o texto pertence e, por último,
# exporta para um arquivo serializado (extensão .spacy).
#   No caso, estou separando os dados em 60% para treinamento, 30% para
# validação (dev), e 10% para teste. 
#   Para treinar um modelo de classificação (textcat) com o spaCy, é preciso um
# arquivo `config.cfg`. Para isso, usa-se o seguinte comando pelo terminal:
# python -m spacy init config  --lang pt --pipeline textcat --optimize efficiency --force config.cfg
#   Em seguida, com o arquivo de configuração, podemos realizar o treinamento:
# python -m spacy train config.cfg --paths.train <path>/train.spacy --paths.dev <path>/dev.spacy --output model --verbose
#   Para avaliar/testar o modelo nos dados de teste:
# python -m spacy evaluate ./model/model-best/ ./test.spacy
#   Para usar o modelo, pode-se carregá-lo com `spacy.load`:
# nlp = spacy.load("./model/model-best")
# for text in texts:
#   doc = nlp(preprocessing(text))
#   print(doc.cats,  "-",  text)




if __name__ == "__main__":
  args = arguments(sys.argv)
  main(args)