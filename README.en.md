# Credit Risk Analysis | Machine Learning
[🇧🇷 Português](./README.md) | [🇺🇸 English](./README.en.md)

## About the Project

This project aims to develop a Machine Learning model capable of identifying customers with a higher credit risk, supporting more informed decision-making in the credit approval process.

Using the **German Credit Risk** dataset, the project follows a data analysis workflow that covers data exploration and preparation, model training, comparison, and evaluation.

In addition to building the predictive model, the project includes a business impact analysis to demonstrate how its predictions can support decision-making by identifying higher-risk customers and evaluating the credit amounts associated with the model's classifications.

## Access the Project

| Resource | Description |
|---|---|
| [Main Notebook](https://github.com/Myllertg/RiscoDeCredito/blob/main/RiscoDeCredito.ipynb) | Complete code covering data analysis, preparation, model training, evaluation, and financial impact analysis. |
| [Streamlit Application](https://riscodecredito-3inb5j7f9veoqr49r5tc6y.streamlit.app/) | Interactive interface for performing credit risk assessments using the developed model. |
| [Project Presentation](./Projeto_Risco_de_Credito_Machine_Learning.pptx) | Presentation covering the project's structure, methodology, and main results. |

## Project Workflow

1. **Business Understanding:** definition of the problem and objectives of the credit risk analysis.
2. **Data Understanding:** investigation of the dataset structure, characteristics, and quality.
3. **Exploratory Data Analysis (EDA):** identification of patterns, variable distributions, and relationships between customer characteristics and risk classifications.
4. **Data Preparation:** data cleaning, categorical variable encoding, and dataset preparation for modeling.
5. **Predictive Modeling:** training and comparison of five Machine Learning algorithms.
6. **Model Evaluation:** comparison using metrics such as Accuracy, Precision, Recall, F1-Score, ROC-AUC, and Average Precision.
7. **Threshold Tuning:** selection of a classification threshold based on the need to identify customers with higher credit risk.
8. **Financial Impact Analysis:** evaluation of credit amounts associated with customers classified by the model.
9. **Interactive Application:** development of a Streamlit interface to demonstrate how the model can be used for new credit risk assessments.

## Models Evaluated

The following algorithms were developed and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- Extra Trees
- XGBoost

**XGBoost** was selected because it achieved the highest ROC-AUC score among the evaluated models.

## Technologies Used

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

## Repository Structure

```text
RiscoDeCredito/
│
├── README.md
├── README.en.md
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

### File Organization

| File or Folder | Purpose |
|---|---|
| `RiscoDeCredito.ipynb` | Main notebook containing the complete analysis and model development. |
| `Projeto_Risco_de_Credito_Machine_Learning.pptx` | Presentation of the project's objectives, methodology, and results. |
| `app/app.py` | Source code for the interactive Streamlit application. |
| `app/requirements.txt` | Dependencies required to run the application. |
| `models/Melhor_Modelo.pkl` | File containing the selected model and its classification threshold. |
| `encoders/` | Files used to encode categorical variables in the application. |

## Business Objective

Demonstrate how Data Science and Machine Learning can be applied to credit risk management by transforming historical data into insights that help identify customers with higher risk exposure.

The goal is to use model predictions as a decision-support tool for credit assessment, contributing to more informed decisions and a better evaluation of the risks involved in lending.

**Disclaimer:** This is a demonstration project developed using a public historical dataset. The results do not represent a proven reduction in default rates and should not replace a real-world credit approval policy.

## Author

**Myller Teixeira Gomes**

Project developed as part of a Data Science portfolio.

[GitHub](https://github.com/Myllertg)

---

[🇧🇷 Read this project in Portuguese](./README.md)
