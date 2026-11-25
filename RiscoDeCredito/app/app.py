
import streamlit as st
import pandas as pd
import joblib

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title=" Análise de Crédito",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# 2. IDENTIDADE VISUAL
# ==========================================================

st.markdown("""
<style>

    /* Fundo principal */
    .stApp {
        background-color: #F4F7FB;
        color: #1E293B;
    }

    /* Área de conteúdo */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Título principal */
    .main-title {
        font-size: 32px;
        font-weight: 700;
        color: #17365D;
        margin-bottom: 5px;
    }

    /* Subtítulo */
    .subtitle {
        color: #64748B;
        font-size: 15px;
        margin-bottom: 25px;
    }

    /* Títulos das seções */
    .section-title {
        font-size: 19px;
        font-weight: 650;
        color: #17365D;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* Textos gerais */
    p, label {
        color: #334155;
    }

    /* Campos de entrada */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    div[data-baseweb="base-input"] {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 7px;
    }

    /* Texto dentro dos campos */
    div[data-baseweb="select"] *,
    div[data-baseweb="input"] input {
        color: #1E293B !important;
    }

    /* Labels */
    .stSelectbox label,
    .stNumberInput label {
        color: #334155 !important;
        font-weight: 600;
    }

    /* Botão principal */
    .stButton > button {
        background-color: #1D4ED8 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px;
        font-weight: 600;
        padding: 12px;
        transition: 0.2s;
    }

    /* Texto do botão */
    .stButton > button p,
    .stButton > button span {
        color: #FFFFFF !important;
    }

    /* Efeito ao passar o mouse */
    .stButton > button:hover {
        background-color: #1E40AF !important;
        color: #FFFFFF !important;
        border: none !important;
    }

    .stButton > button:hover p,
    .stButton > button:hover span {
        color: #FFFFFF !important;
    }

    /* Cartões dos indicadores */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        padding: 18px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(15, 23, 42, 0.04);
    }

    /* Título dos indicadores */
    div[data-testid="stMetricLabel"] {
        color: #64748B !important;
    }

    /* Valores dos indicadores */
    div[data-testid="stMetricValue"] {
        color: #17365D !important;
        font-weight: 700;
    }

    /* Resultado de risco elevado */
    .risk-high {
        color: #DC2626 !important;
        font-size: 25px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    /* Resultado de risco reduzido */
    .risk-low {
        color: #15803D !important;
        font-size: 25px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    /* Barra de progresso */
    div[data-testid="stProgress"] > div {
        background-color: #E2E8F0;
        border-radius: 10px;
    }

    div[data-testid="stProgress"] > div > div {
        background-color: #2563EB;
        border-radius: 10px;
    }

    /* Linhas divisórias */
    hr {
        border-color: #DCE4EE;
    }

</style>
""", unsafe_allow_html=True)


# ==========================================================
# 3. CARREGAMENTO DO MODELO E DO THRESHOLD
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"
ENCODERS_DIR = BASE_DIR / "encoders"


# ==========================================================
# 4. CARREGAMENTO DOS ENCODERS
# ==========================================================

# Carregar modelo e threshold
arquivo_modelo = MODELS_DIR / "Melhor_Modelo.pkl"

arquivo = joblib.load(arquivo_modelo)

model = arquivo["modelo"]
threshold = arquivo["threshold"]


# Carregar encoders
encoders = {
    col: joblib.load(ENCODERS_DIR / f"{col}_encoder.pkl")
    for col in [
        "Sex",
        "Housing",
        "Saving accounts",
        "Checking account"
    ]
}
# ==========================================================
# 5. CABEÇALHO
# ==========================================================

st.markdown(
    '<div class="main-title">Análise de Risco de Crédito</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Sistema de avaliação do perfil de crédito utilizando '
    'Machine Learning e algoritmo XGBoost.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ==========================================================
# 6. FORMULÁRIO DE ENTRADA
# ==========================================================

st.markdown(
    '<div class="section-title">01 | Perfil do solicitante</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Idade",
        min_value=18,
        max_value=80,
        value=30
    )

with col2:
    sex = st.selectbox(
        "Sexo",
        ["male", "female"],
        format_func=lambda x: {
            "male": "Masculino",
            "female": "Feminino"
        }[x]
    )

with col3:
    job = st.selectbox(
        "Categoria profissional",
        [0, 1, 2, 3],
        format_func=lambda x: f"Categoria {x}"
    )


st.markdown(
    '<div class="section-title">02 | Perfil financeiro</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    housing = st.selectbox(
        "Tipo de moradia",
        ["own", "rent", "free"],
        format_func=lambda x: {
            "own": "Própria",
            "rent": "Alugada",
            "free": "Cedida / Gratuita"
        }[x]
    )

with col2:
    saving_accounts = st.selectbox(
        "Saldo em conta poupança",
        ["little", "moderate", "rich", "quite rich"],
        format_func=lambda x: {
            "little": "Baixo",
            "moderate": "Moderado",
            "rich": "Alto",
            "quite rich": "Muito alto"
        }[x]
    )

checking_account = st.selectbox(
    "Saldo em conta corrente",
    ["little", "moderate", "rich"],
    format_func=lambda x: {
        "little": "Baixo",
        "moderate": "Moderado",
        "rich": "Alto"
    }[x]
)


st.markdown(
    '<div class="section-title">03 | Dados da operação de crédito</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    credit_amount = st.number_input(
        "Valor do crédito solicitado (R$)",
        min_value=0,
        max_value=100000,
        value=1000,
        step=100
    )

with col2:
    duration = st.number_input(
        "Prazo do empréstimo (meses)",
        min_value=1,
        max_value=120,
        value=12
    )


st.divider()


# ==========================================================
# 7. EXECUÇÃO DA PREVISÃO
# ==========================================================

if st.button(
    "REALIZAR ANÁLISE DE CRÉDITO",
    use_container_width=True,
    type="primary"
):

    # Codificação das variáveis categóricas
    input_df = pd.DataFrame({
        "Age": [age],
        "Sex": [encoders["Sex"].transform([sex])[0]],
        "Job": [job],
        "Housing": [encoders["Housing"].transform([housing])[0]],
        "Saving accounts": [
            encoders["Saving accounts"].transform([saving_accounts])[0]
        ],
        "Checking account": [
            encoders["Checking account"].transform([checking_account])[0]
        ],
        "Credit amount": [credit_amount],
        "Duration": [duration]
    })

    # Identificar a posição de cada classe
    indice_bad = list(model.classes_).index(0)
    indice_good = list(model.classes_).index(1)

    # Calcular probabilidades
    probabilidades = model.predict_proba(input_df)[0]

    prob_bad = probabilidades[indice_bad]
    prob_good = probabilidades[indice_good]

    # Aplicar threshold ajustado
    if prob_bad >= threshold:
        resultado = "RISCO DE CRÉDITO ELEVADO"
        classificacao = "Bad"
    else:
        resultado = "RISCO DE CRÉDITO REDUZIDO"
        classificacao = "Good"


    # ======================================================
    # 8. RESULTADO DA ANÁLISE
    # ======================================================

    st.divider()

    st.markdown(
        '<div class="section-title">Resultado da avaliação</div>',
        unsafe_allow_html=True
    )

    if classificacao == "Bad":

        st.markdown(
            '<div class="risk-high">'
            'RISCO DE CRÉDITO ELEVADO'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(
            "O modelo identificou uma probabilidade de crédito ruim "
            "igual ou superior ao limite de classificação estabelecido."
        )

    else:

        st.markdown(
            '<div class="risk-low">'
            'RISCO DE CRÉDITO REDUZIDO'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(
            "O modelo identificou uma probabilidade de crédito ruim "
            "inferior ao limite de classificação estabelecido."
        )


    # ======================================================
    # 9. INDICADORES PRINCIPAIS
    # ======================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Probabilidade de crédito ruim",
            f"{prob_bad:.2%}"
        )

    with col2:
        st.metric(
            "Probabilidade de crédito bom",
            f"{prob_good:.2%}"
        )

    with col3:
        st.metric(
            "Threshold utilizado",
            f"{threshold:.0%}"
        )


    # ======================================================
    # 10. INDICADOR VISUAL DE RISCO
    # ======================================================

    st.markdown("### Indicador de risco")

    st.progress(float(prob_bad))

    st.caption(
        f"Probabilidade estimada de crédito ruim: {prob_bad:.2%}"
    )


st.divider()
