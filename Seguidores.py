{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMeWwD1rGAuGS86Smfh+DJX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jxnscv/Revis/blob/main/Seguidores.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Comprobador de seguidores"
      ],
      "metadata": {
        "id": "V9Dso8ZVnfXw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "import pandas as pd\n",
        "import streamlit as st\n",
        "import requests\n",
        "\n",
        "# Función para cargar datos desde un archivo JSON en una URL\n",
        "def cargar_datos_instagram(url):\n",
        "    respuesta = requests.get(url)\n",
        "    if respuesta.status_code == 200:\n",
        "        return respuesta.json()\n",
        "    else:\n",
        "        st.error(\"Error al cargar los datos.\")\n",
        "        return {}\n",
        "\n",
        "# Función para convertir los datos a un DataFrame\n",
        "def convertir_a_dataframe(datos):\n",
        "    seguidores = datos.get('followers', [])  # Cambia 'followers' según la estructura de tu JSON\n",
        "    siguiendo = datos.get('following', [])    # Cambia 'following' según la estructura de tu JSON\n",
        "\n",
        "    # Encontrar cuentas que no te siguen de vuelta\n",
        "    no_me_siguen = [usuario for usuario in siguiendo if usuario not in seguidores]\n",
        "\n",
        "    # Crear un DataFrame\n",
        "    df = pd.DataFrame(no_me_siguen, columns=['Cuentas a dejar de seguir'])\n",
        "    return df\n",
        "\n",
        "# URL del archivo JSON\n",
        "url_archivo = 'https://raw.githubusercontent.com/jxnscv/Revis/main/debug_output.json'\n",
        "\n",
        "# Cargar los datos\n",
        "datos_instagram = cargar_datos_instagram(url_archivo)\n",
        "\n",
        "# Convertir a DataFrame\n",
        "df = convertir_a_dataframe(datos_instagram)\n",
        "\n",
        "# Mostrar el DataFrame en Streamlit\n",
        "st.title(\"Análisis de Seguidores de Instagram\")\n",
        "st.write(\"Cuentas a las que deberías dejar de seguir porque no te siguen:\")\n",
        "st.write(df)"
      ],
      "metadata": {
        "id": "Pi-AzUnnqPhG"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
