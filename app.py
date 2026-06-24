import streamlit as st
import math

def calcular_pg(a1, an, q, n):
    passos = []
    # 1. Encontrar a variável que falta
    if an is None:
        # Calcular an = a1 * q^(n-1)
        an = a1 * (q ** (n - 1))
        passos.append(f"**Cálculo do $a_n$:** $a_n = a_1 \cdot q^{{n-1}} \Rightarrow a_n = {a1} \cdot {q}^{{{n}-1}} = {an:.4f}$")
    
    elif a1 is None:
        # Calcular a1 = an / q^(n-1)
        a1 = an / (q ** (n - 1))
        passos.append(f"**Cálculo do $a_1$:** $a_1 = \\frac{{a_n}}{{q^{{n-1}}}} \Rightarrow a_1 = \\frac{{{an}}}{{{q}^{{{n}-1}}}} = {a1:.4f}$")
    
    elif q is None:
        # Calcular q = (an / a1) ^ (1 / (n-1))
        q = (an / a1) ** (1 / (n - 1))
        passos.append(f"**Cálculo da razão ($q$):** $q = \\sqrt[n-1]{{\\frac{{a_n}}{{a_1}}}} \Rightarrow q = \\sqrt[{(n-1)}]{{\\frac{{{an}}}{{{a1}}}}} = {q:.4f}$")
    
    elif n is None:
        # Calcular n = 1 + log(an / a1) / log(q)
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

# --- INTERFACE DO USUÁRIO (STREAMLIT) ---
st.title("🔢 Calculadora Inteligente de Progressão Geométrica")
st.write("Deixe **apenas um** campo em branco (ou igual a zero) para o app descobrir o valor e calcular a soma.")

# Inputs
col1, col2 = st.columns(2)
with col1:
    input_a1 = st.number_input("Primeiro termo (a1):", value=0.0, step=1.0, format="%.2f")
    input_q = st.number_input("Razão (q):", value=0.0, step=1.0, format="%.2f")
with col2:
    input_an = st.number_input("Último termo (an):", value=0.0, step=1.0, format="%.2f")
    input_n = st.number_input("Número de termos (n):", value=0, step=1)

if st.button("Calcular PG e Soma", type="primary"):
    # Mapeia inputs (0 ou 0.0 é considerado o valor a ser descoberto)
    a1 = None if input_a1 == 0 else input_a1
    an = None if input_an == 0 else input_an
    q = None if input_q == 0 else input_q
    n = None if input_n == 0 else input_n

    # Validação: contar quantos campos nulos existem
    nulos = [a1, an, q, n].count(None)

    if nulos != 1:
        st.error("Erro: Você deve preencher exatamente **3 campos** e deixar apenas 1 em branco para a descoberta.")
    else:
        try:
            res_a1, res_an, res_q, res_n, res_sn, passos = calcular_pg(a1, an, q, n)
            
            st.success("### 🎉 Resultados Encontrados")
            
            # Exibição dos valores finais
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.metric("Primeiro Termo ($a_1$)", f"{res_a1:.4f}")
                st.metric("Razão ($q$)", f"{res_q:.4f}")
            with res_col2:
                st.metric("Termo Geral ($a_n$)", f"{res_an:.4f}")
                st.metric("Nº de Termos ($n$)", f"{res_n}")
            
            st.metric("Soma dos Termos ($S_n$)", f"{res_sn:.4f}")
            
            # Demonstração do passo a passo
            st.write("---")
            st.subheader("📝 Resolução Passo a Passo")
            for passo in passos:
                st.write(passo)
                
        except Exception as e:
            st.error(f"Erro matemático: Verifique se os dados inseridos formam uma PG real (ex: evitar logaritmo de números negativos ou divisão por zero).")
