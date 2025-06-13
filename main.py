import streamlit as st

st.set_page_config(page_title="VoltLynx", page_icon="⚡", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00ffff;'>⚡ VoltLynx ⚡</h1>", unsafe_allow_html=True)

tipo = st.selectbox("Selecciona el tipo de periodo:", ["Diario", "Quincenal", "Mensual", "Anual"])
cantidad = st.number_input(f"Ingrese el número de {tipo.lower()}s:", min_value=1, value=1)
monto = st.number_input("Ingresa el monto inicial ($):", min_value=0.0, value=1000.0)
interes_anual = st.number_input("Interés anual (%):", min_value=0.0, value=10.0)

periodos_por_año = {
    "Diario": 365,
    "Quincenal": 24,
    "Mensual": 12,
    "Anual": 1
}

r = interes_anual / 100 / periodos_por_año[tipo]
resultado = monto * (1 + r) ** cantidad

if st.button("Calcular"):
    st.success(f"🔹 Monto final después de {cantidad} {tipo.lower()}s: ${resultado:,.2f}")
