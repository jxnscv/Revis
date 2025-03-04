import json
import pandas as pd
import streamlit as st
import requests

# Función para cargar datos desde un archivo JSON en una URL
def cargar_datos_instagram(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        st.error("Error al cargar los datos.")
        return {}

# Función para convertir los datos a un DataFrame
def convertir_a_dataframe(datos):
    seguidores = datos.get('followers', [])  # Cambia 'followers' según la estructura de tu JSON
    siguiendo = datos.get('following', [])    # Cambia 'following' según la estructura de tu JSON
    
    # Encontrar cuentas que no te siguen de vuelta
    no_me_siguen = [usuario for usuario in siguiendo if usuario not in seguidores]
    
    # Crear un DataFrame
    df = pd.DataFrame(no_me_siguen, columns=['Cuentas a dejar de seguir'])
    return df

# URL del archivo JSON
url_archivo = 'https://raw.githubusercontent.com/jxnscv/Revis/main/debug_output.json'

# Cargar los datos
datos_instagram = cargar_datos_instagram(url_archivo)

# Convertir a DataFrame
df = convertir_a_dataframe(datos_instagram)

# Mostrar el DataFrame en Streamlit
st.title("Análisis de Seguidores de Instagram")
st.write("Cuentas a las que deberías dejar de seguir porque no te siguen:")
st.write(df)
