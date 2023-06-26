import pandas as pd

# Carregando o pipeline pelo módulo do Spacy
# import spacy
# nlp = spacy.load('pt_core_news_sm')
# nlp = spacy.load('pt_core_news_lg')

# Carregando o pipeline como módulo
import pt_core_news_sm as pt_model
# import pt_core_news_lg as pt_model
nlp = pt_model.load()

# Exemplo Básico
# doc = nlp("Apresento-lhes a frase-exemplo. Esta é uma sra. frase como exemplo para vocês.")
# print('\n'.join([f'Texto: {w.text}\tLemma: {w.lemma_}\tPos: {w.pos_}' for w in doc]))

# Exemplo de Proposta
propostas = pd.read_csv('./spacy/propostas.csv')
docTitle = nlp(propostas['Título'].iloc[0])
docDesc = nlp(propostas['Descrição'].iloc[0])

print(f'TÍTULO: {docTitle}\n')
print('\n'.join([f'Texto: {w.text:<15}Lemma: {w.lemma_:<15}Pos: {w.pos_:<10}' for w in docTitle]))
print('\n---------------------------------------------------------------------------------\n')
print(f'DESCRIÇÃO: {docDesc}\n')
print('\n'.join([f'Texto: {w.text:<15}Lemma: {w.lemma_:<15}Pos: {w.pos_:<10}' for w in docDesc]))
