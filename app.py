import streamlit as st
import math

def calcular_pg(a1, an, q, n):
    passos = []
    # 1. Encontrar a variável que falta
    if an is None:
        an = a1 * (q ** (n - 1))
        passos.append(f"**Cálculo do $a_n$:** $a_n = a_1 \cdot q^{{n-1}} \Rightarrow a_n = {a1} \cdot {q}^{{{n}-1}} = {an:.4f}$")
    
    elif a1 is None:
        a1 = an / (q ** (n - 1))
        passos.append(f"**Cálculo do $a_1$:** $a_1 = \\frac{{a_n}}{{q^{{n-1}}}} \Rightarrow a_1 = \\frac{{{an}}}{{{q}^{{{n}-1}}}} = {a1:.4f}$")
    
    elif q is None:
        q = (an / a1) ** (1 / (n - 1))
        passos.append(f"**Cálculo da razão ($q$):** $q = \\sqrt[n-1]{{\\frac{{a_n}}{{a_1}}}} \Rightarrow q = \\sqrt[{(n-1)}]{{\\frac{{{an}}}{{{a1}}}}} = {q:.4f}$")
    
    elif n is None:
        n = 1 + (math.log(an / a1) / math.log(q))
        passos.append(f"**Cálculo do número de termos ($n$):** $n = 1 + \\frac{{\\log(a_n / a_1)}}{{\\log(q)}} = {n:.2f}$ (Arredondado: {round(n)})")
        n = round(n)

    # 2. Calcular a Soma dos Termos (Sn)
    if q == 1:
        sn = n * a1
        passos.append(f"**Cálculo da Soma ($S_n$) para $q=1$:** $S_n = n \cdot a_1 \Rightarrow S_n = {n} \cdot {a1} = {sn:.4f}$")
    else:
        sn = a1 * ((q ** n) - 1) / (q - 1)
        passos.append(f"**Cálculo da Soma ($S_n$):** $S_n = \\frac{{a_1 \cdot (q^n - 1)}}{{q - 1}} \Rightarrow S_n = \\frac{{{a1} \cdot ({q}^{{{n}}} - 1)}}{{{q} - 1}} = {sn:.4f}$")

    return a1, an, q, n, sn, passos

# --- CONFIGURAÇÃO DA INTERFACE ---
st.set_page_config(page_title="Calculadora PG", layout="centered")

st.title("🔢 Calculadora de PG")
st.write("Deixe apenas **um** campo zerado para descobrir seu valor.")

# Inputs com ID único (key) para estabilidade no mobile
input_a1 = st.number_input("Primeiro termo (a1):", value=0.0, step=1.0, format="%.2f", key="a1_input")
input_q = st.number_input("Razão (q):", value=0.0, step=1.0, format="%.2f", key="q_input")
input_an = st.number_input("Último termo (an):", value=0.0, step=1.0, format="%.2f", key="an_input")
input_n = st.number_input("Número de termos (n):", value=0, step=1, key="n_input")

if st.button("Calcular PG e Soma", type="primary", key="btn_calcular"):
    a1 = None if input_a1 == 0 else input_a1
    an = None if input_an == 0 else input_an
    q = None if input_q == 0 else input_q
    n = None if input_n == 0 else input_n

    nulos = [a1, an, q, n].count(None)

    if nulos != 1:
        st.error("Erro: Preencha exatamente **3 campos** e deixe apenas 1 zerado.")
    else:
        try:
            res_a1, res_an, res_q, res_n, res_sn, passos = calcular_pg(a1, an, q, n)
            
            st.success("### 🎉 Resultados")
            st.write(f"**Primeiro Termo ($a_1$):** {res_a1:.4f}")
            st.write(f"**Razão ($q$):** {res_q:.4f}")
            st.write(f"**Termo Geral ($a_n$):** {res_an:.4f}")
            st.write(f"**Nº de Termos ($n$):** {res_n}")
            st.write(f"**Soma dos Termos ($S_n$):** {res_sn:.4f}")
            
            st.write("---")
            st.subheader("📝 Passo a Passo")
            for passo in passos:
                st.write(passo)
                
        except Exception as e:
            st.error("Erro matemático: Verifique se os dados fazem sentido para uma PG real.")
