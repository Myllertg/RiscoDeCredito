
import streamlit as st
import pandas as pd
import joblib

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Nexus | Análise de Crédito",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# 2. IDENTIDADE VISUAL
# ==========================================================

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .main-title {
        font-size: 32px;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #64748B;
        font-size: 15px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 19px;
        font-weight: 600;
        color: #1E293B;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .result-card {
        padding: 22px;
        border-radius: 12px;
        background-color: #F1F5F9;
        border: 1px solid #E2E8F0;
        margin-top: 15px;
    }

    .risk-high {
        color: #DC2626;
        font-size: 25px;
        font-weight: 700;
    }

    .risk-low {
        color: #15803D;
        font-size: 25px;
        font-weight: 700;
    }

    .small-text {
        color: #64748B;
        font-size: 13px;
    }

    div[data-testid="stMetric"] {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        padding: 15px;
        border-radius: 10px;
    }

</style>
""", unsafe_allow_html=True)


# ==========================================================
# 3. CARREGAMENTO DO MODELO E DO THRESHOLD
# ==========================================================

arquivo = joblib.load("Melhor_Modelo.pkl")

model = arquivo["modelo"]
threshold = arquivo["threshold"]


# ==========================================================
# 4. CARREGAMENTO DOS ENCODERS
# ==========================================================

encoders = {
    col: joblib.load(f"{col}_encoder.pkl")
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
        st.error(resultado)
        st.write(
            "O modelo identificou uma probabilidade de crédito ruim "
            "igual ou superior ao limite de classificação estabelecido."
        )
    else:
        st.success(resultado)
        st.write(
            "O modelo identificou uma probabilidade de crédito ruim "
            "inferior ao limite de classificação estabelecido."
        )

    # Indicadores principais
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
    # 9. INDICADOR VISUAL DE RISCO
    # ======================================================

    st.markdown("### Indicador de risco")

    st.progress(float(prob_bad))

    st.caption(
        f"Probabilidade estimada de crédito ruim: {prob_bad:.2%}"
    )

    # ======================================================
    # 10. RESUMO DA ANÁLISE
    # ======================================================

    with st.expander("Visualizar dados analisados"):

        resumo = pd.DataFrame({
            "Informação": [
                "Idade",
                "Sexo",
                "Categoria profissional",
                "Tipo de moradia",
                "Poupança",
                "Conta corrente",
                "Valor do crédito",
                "Prazo"
            ],
            "Valor informado": [
                f"{age} anos",
                "Masculino" if sex == "male" else "Feminino",
                f"Categoria {job}",
                housing,
                saving_accounts,
                checking_account,
                f"R$ {credit_amount:,.2f}",
                f"{duration} meses"
            ]
        })

        st.dataframe(
            resumo,
            use_container_width=True,
            hide_index=True
        )

    # ======================================================
    # 11. AVISO
    # ======================================================

    st.info(
        "Esta avaliação é uma estimativa produzida por um modelo "
        "experimental de Machine Learning. O resultado não representa "
        "uma decisão definitiva de concessão ou recusa de crédito."
    )


# ==========================================================
# 12. RODAPÉ
# ==========================================================

st.divider()

st.markdown(
    '<div style="text-align:center; color:#94A3B8; font-size:12px;">'
    'Sistema demonstrativo de análise de risco de crédito | '
    'Machine Learning com XGBoost'
    '</div>',
    unsafe_allow_html=True
)
