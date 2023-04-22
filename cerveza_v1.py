import streamlit as st
import datetime

def sumar_tiempo(hora, minutos):
    return (hora + datetime.timedelta(minutes=minutos)).strftime('%H:%M')

def convertir_hora(hora_str):
    return datetime.datetime.strptime(hora_str, '%H:%M')

def css_personalizado(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

css = """
.respuesta {
    font-size: 15px;
}
"""
css_personalizado(css)
css_personalizado(css)

st.title("Calculadora de tiempos de macerado y hervor de cerveza")

st.header("Macerado del mosto")
hora_inicio_macerado = st.text_input("Hora de inicio del macerado (formato 24h, ej. 14:30):")
if hora_inicio_macerado:
    try:
        hora_inicio_macerado = convertir_hora(hora_inicio_macerado)
        hora_encender_q1 = sumar_tiempo(hora_inicio_macerado, 30)
        hora_fin_macerado = sumar_tiempo(hora_inicio_macerado, 60)
        st.markdown(f"<div class='respuesta'>Hora para encender Q1: {hora_encender_q1}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='respuesta'>Hora de finalización del macerado: {hora_fin_macerado}</div>", unsafe_allow_html=True)
    except ValueError:
        st.error("Por favor, ingrese una hora válida en formato 24h (ej. 14:30).")

st.header("Hervor del mosto")
hora_inicio_hervor = st.text_input("Hora de inicio del hervor (formato 24h, ej. 16:00):")
if hora_inicio_hervor:
    try:
        hora_inicio_hervor = convertir_hora(hora_inicio_hervor)
        min_55 = sumar_tiempo(hora_inicio_hervor, 5)
        min_21 = sumar_tiempo(hora_inicio_hervor, 39)
        min_7 = sumar_tiempo(hora_inicio_hervor, 53)
        min_0 = sumar_tiempo(hora_inicio_hervor, 60)
        st.markdown(f"<div class='respuesta'>Minuto 55: {min_55}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='respuesta'>Minuto 21: {min_21}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='respuesta'>Minuto 7: {min_7}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='respuesta'>Minuto 0: {min_0}</div>", unsafe_allow_html=True)
    except ValueError:
        st.error("Por favor, ingrese una hora válida en formato 24h (ej. 16:00).")

