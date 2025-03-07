import streamlit as st
import json
import requests

# Función para cargar datos desde una URL
def load_data(url):
    response = requests.get(url)
    return json.loads(response.text)

# URLs de los archivos JSON
following_url = "https://raw.githubusercontent.com/jxnscv/Revis/main/following.json"
followers_url = "https://raw.githubusercontent.com/jxnscv/Revis/main/followers_1.json"

# Cargar los datos
following_data = load_data(following_url)
followers_data = load_data(followers_url)

# Asegurarse de que los datos son listas de nombres
if isinstance(following_data, list):
    following_set = set(following_data)
else:
    st.error("El archivo 'following.json' no contiene una lista de nombres.")

if isinstance(followers_data, list):
    followers_set = set(followers_data)
else:
    st.error("El archivo 'followers_1.json' no contiene una lista de nombres.")

# Encontrar nombres que faltan en cada conjunto
faltan_en_following = followers_set - following_set
faltan_en_followers = following_set - followers_set

# Título de la aplicación
st.title("Comparación de Following y Followers")

# Mostrar resultados
st.subheader("Nombres que faltan en 'following':")
if faltan_en_following:
    st.write(", ".join(faltan_en_following))
else:
    st.write("No faltan nombres en 'following'.")

st.subheader("Nombres que faltan en 'followers':")
if faltan_en_followers:
    st.write(", ".join(faltan_en_followers))
else:
    st.write("No faltan nombres en 'followers'.")
