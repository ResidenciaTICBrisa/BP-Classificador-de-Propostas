# Processamento de Linguagem Natural 

<br/>
<div align="center">
  <a href="https://github.com/ResidenciaTICBrisa/07_ProcessamentoLinguagemNatural/tree/main">
    <img src="https://residenciaticbrisa.github.io/07_ProcessamentoLinguagemNatural/assets/img/logo.png" width="300" height="300">
  </a>
</div>

<p align="left"><a href="https://residenciaticbrisa.github.io/07_ProcessamentoLinguagemNatural/"><strong>Visualizar documentação online</strong></a></p>

## Descrição
[Brasil Participativo](https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/) é a nova plataforma digital do governo federal, software livre Decidim, um espaço para que a população possa contribuir com a criação e melhoria das políticas públicas. Com uma semana no ar, a plataforma já tem 1000 propostas feitas pelos cidadãos. A plataforma, porém, não possui indexação ou processamento de linguagem natural para categorizar de forma automatizada as propostas. A ideia da proposta é fazer análise das propostas por meio de processamento de linguagem natural (PLN).

**Mentores:** Laila, Secretaria de Participação Social

## 💻 Tecnologias

**Tecnologias utilizadas neste projeto:**

### Apache Airflow

O Apache e responsavel pela atualização e o treinamento diario do modelo em conjunto com os dados da plataforma do brasil participativo.

[Repositorio Airflow]()

![Apache Airflow](https://airflow.apache.org/images/feature-image.png)

### Modelo de Classificação 

![Scikit Learn](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png)

O python foi responsavel pela instanciação do modelo de classificação de propostas, entretanto para seu uso  e necessario algumas dependencias como: 

 - [python 3.12.0](https://www.python.org/downloads/release/python-3120/) 

Gerenciador de pacotes, no caso o utilizado no desenvolvimento do projeto, *pip*

 - ```sudo apt install pip```

Apos termos o pip instalado podemos preparar nosso ambiente para as bibliotecas necessarias para, treinarmos nosso modelo:

- NumPy: ``` pip install numpy ```

- Pandas: ``` pip install pandas ```

- NLTK: ``` pip install nltk ```

- Scikit-learn: ``` pip install scikit-learn ```

- Plotly: ``` pip install plotly ```

- Skops: ``` pip install skops ```

- Unidecode: ``` pip install unidecode ```

- Pathlib: ``` pip install pathlib ```

Desse modo apos termos nosso ambiente configurado podemos partir para a execução do modelo que pode ser encontrado em [opt_10](https://github.com/ResidenciaTICBrisa/07_ProcessamentoLinguagemNatural/blob/main/production/otimizacoes_classifier/opt_10/v10.ipynb),que corresponde a versão com mais otimizações do modelo.Ou atraves do [processo de desenvolvimento](https://residenciaticbrisa.github.io/07_ProcessamentoLinguagemNatural/processo_de_desenvolvimento/) encontrado em nosso GitPages.

### RubyGem

![Ruby Gem](https://sempreupdate.com.br/wp-content/uploads/2017/08/rubygems.png)

Por fim esta disponibilizado a gem em Ruby e o repositorio da mesma para utilização do modelo dentro de plataformas web afim de ser integrado a plataforma do Brasil Participativo.

## 🤖 Funcionalidade

## 🛞 Como executar/rodar

### **- 👩‍🦰 Usuário**

1. **Abra seu terminal e digite o comando para instalar o Certifik8 do Pypi:**
```
gem install proposal-classifier
```

## Desenvolvedores

<center>
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <td align="center">
            <a href="https://github.com/LexTOliver">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/27731119?v=4" width="150px;"/>
                <h5 class="text-center">Alexandre Oliveira</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/jpanacleto2">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/56097889?v=4" width="150px;"/>
                <h5 class="text-center">João Anacleto</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/chaydson">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/90580219?v=4" width="150px;"/>
                <h5 class="text-center">Chaydson Ferreira</h5>
            </a>
        </td>
        </td>
        <td align="center">
            <a href="https://github.com/Leanddro13">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/86811628?v=4" width="150px;"/>
                <h5 class="text-center">Leandro Silva</h5>
            </a>
        </td>
</table>
</center>
