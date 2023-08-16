import spacy
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier

propostas = pd.read_csv("pre-processamento/data/propostas.csv")

propostas = propostas[['Tema', 'Corpo']]

print(propostas.Tema.value_counts())

propostas['tema_num'] = propostas['Tema'].map({
    'Educação': 0,
    'Saúde': 1,
    'Direitos Humanos e Cidadania': 2,
    'Meio Ambiente e Mudança do Clima': 3,
    'Transportes': 4,
    'Trabalho e Emprego': 5,
    'Desenvolvimento e Assistência Social, Família e Combate à Fome': 6,
    'Desenvolvimento Agrário e Agricultura Familiar': 7,
    'Outros': 8,
    'Cidades': 9,
    'Justiça e Segurança Pública': 10,
    'Cultura': 11,
    'Gestão e Inovação em Serviços Públicos': 12,
    'Mulheres': 13,
    'Ciência, Tecnologia e Inovação': 14,
    'Turismo': 15,
    'Previdência Social': 16,
    'Fazenda': 17,
    'Planejamento e Orçamento': 18,
    'Integração e Desenvolvimento Regional': 19,
    'Agricultura e Pecuária': 20,
    'Igualdade Racial': 21,
    'Desenvolvimento, Indústria, Comércio e Serviços': 22,
    'Esporte': 23,
    'Minas e Energia': 24,
    'Infraestrutura': 25,
    'Casa Civil': 26,
    'Defesa': 27,
    'Comunicação Social': 28,
    'Povos Indígenas': 29,
    'Comunicações': 30,
    'Segurança Institucional': 31,
    'Secretaria Geral da Presidência da República': 32,
    'Controladoria-Geral da União': 33,
    'Banco Central': 34,
    'Portos e Aeroportos': 35,
    'Pesca e Aquicultura': 36,
    'Advocacia-Geral da União': 37,
    'Relações Institucionais': 38,
    'Presidência': 39,
    'Relações Exteriores': 40
})

nlp = spacy.load("pt_core_news_lg")

propostas['vector'] = propostas['Corpo'].apply(lambda text: nlp(text).vector)


print(propostas.head())

if propostas['tema_num'].isnull().any():
    propostas.dropna(subset=['tema_num'], inplace=True)

X_train, X_test, y_train, y_test = train_test_split(
    propostas.vector.values,
    propostas.tema_num,
    test_size=0.2,
    random_state=2022
)

X_train_2d = np.stack(X_train)
X_test_2d = np.stack(X_test)

scaler = MinMaxScaler()
scaled_train_embed = scaler.fit_transform(X_train_2d)
scaled_test_embed = scaler.transform(X_test_2d)

clf = MultinomialNB()
clf.fit(scaled_train_embed, y_train)

y_pred = clf.predict(scaled_test_embed)

print(classification_report(y_test, y_pred))

clf = KNeighborsClassifier(n_neighbors = 5, metric= 'euclidean')
clf.fit(X_train_2d, y_train)

y_pred = clf.predict(X_test_2d)

print(classification_report(y_test, y_pred))