# Análise de Risco de Crédito | Machine Learning
[🇧🇷 Português](./README.md) | [🇺🇸 English](./README.en.md)

## Sobre o projeto

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de identificar clientes com maior risco de crédito, contribuindo para uma tomada de decisão mais fundamentada na concessão de crédito.

Utilizando a base de dados **German Credit Risk**, foi desenvolvido um processo de análise de dados que abrange desde a exploração e preparação das informações até o treinamento, comparação e avaliação de modelos preditivos.

Além da construção do modelo, o projeto apresenta uma análise de como suas previsões podem apoiar decisões de negócio, identificando clientes com maior risco e avaliando os valores de crédito associados às classificações realizadas.

## Acesse o projeto

| Recurso | Descrição |
|---|---|
| [Notebook principal](https://github.com/Myllertg/RiscoDeCredito/blob/main/RiscoDeCredito.ipynb) | Código completo da análise, preparação dos dados, treinamento, avaliação dos modelos e análise de impacto financeiro. |
| [Aplicação Streamlit](https://riscodecredito-3inb5j7f9veoqr49r5tc6y.streamlit.app/) | Interface interativa para realizar análises de risco de crédito utilizando o modelo desenvolvido. |
| [Apresentação do projeto](./Projeto_Risco_de_Credito_Machine_Learning.pptx) | Apresentação com a estrutura, metodologia e principais resultados do projeto. |

## Etapas do projeto

1. **Entendimento do negócio:** definição do problema e dos objetivos da análise de risco de crédito.
2. **Entendimento dos dados:** investigação da estrutura, características e qualidade da base de dados.
3. **Análise Exploratória de Dados (EDA):** identificação de padrões, distribuição das variáveis e relações entre características dos clientes e classificação de risco.
4. **Preparação dos dados:** tratamento das informações, codificação das variáveis categóricas e organização dos dados para modelagem.
5. **Modelagem preditiva:** treinamento e comparação de cinco algoritmos de Machine Learning.
6. **Avaliação dos modelos:** comparação de métricas como Accuracy, Precision, Recall, F1-Score, ROC-AUC e Average Precision.
7. **Ajuste do Threshold:** definição de um limiar de classificação considerando a necessidade de identificar clientes com maior risco.
8. **Análise de impacto financeiro:** avaliação dos valores de crédito associados aos clientes classificados pelo modelo.
9. **Aplicação interativa:** desenvolvimento de uma interface com Streamlit para demonstrar a utilização do modelo em novas análises.

## Modelos avaliados

Foram desenvolvidos e comparados os seguintes algoritmos:

- Regressão Logística
- Árvore de Decisão
- Random Forest
- Extra Trees
- XGBoost

O **XGBoost** foi selecionado por apresentar o melhor resultado de ROC-AUC entre os modelos avaliados.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Streamlit
- Jupyter Notebook
- Google Colab

## Estrutura do repositório

```text
RiscoDeCredito/
│
├── README.md
├── RiscoDeCredito.ipynb
├── Projeto_Risco_de_Credito_Machine_Learning.pptx
│
└── RiscoDeCredito/
    │
    ├── app/
    │   ├── app.py
    │   └── requirements.txt
    │
    ├── models/
    │   └── Melhor_Modelo.pkl
    │
    └── encoders/
        ├── Sex_encoder.pkl
        ├── Housing_encoder.pkl
        ├── Saving accounts_encoder.pkl
        └── Checking account_encoder.pkl
```

### Organização dos arquivos

| Arquivo ou pasta | Finalidade |
|---|---|
| `RiscoDeCredito.ipynb` | Notebook principal com o desenvolvimento completo da análise e dos modelos. |
| `Projeto_Risco_de_Credito_Machine_Learning.pptx` | Apresentação dos objetivos, metodologia e resultados. |
| `app/app.py` | Código da aplicação interativa desenvolvida com Streamlit. |
| `app/requirements.txt` | Dependências necessárias para executar a aplicação. |
| `models/Melhor_Modelo.pkl` | Arquivo contendo o modelo selecionado e o threshold definido. |
| `encoders/` | Arquivos utilizados para codificar as variáveis categóricas na aplicação. |

## Objetivo de negócio

Demonstrar como a Ciência de Dados e o Machine Learning podem ser aplicados à gestão de risco de crédito, transformando dados históricos em informações que auxiliam na identificação de clientes com maior exposição ao risco.

A proposta é utilizar as previsões como ferramenta de apoio à análise de crédito, contribuindo para decisões mais criteriosas e para uma melhor avaliação dos riscos envolvidos na concessão de empréstimos.

**Importante:** este é um projeto demonstrativo, desenvolvido com uma base histórica pública. Os resultados não representam uma redução comprovada da inadimplência nem substituem uma política real de concessão de crédito.

## Autor

**Myller Teixeira Gomes**

Projeto desenvolvido como parte do portfólio de Ciência de Dados.

[GitHub](https://github.com/Myllertg)
