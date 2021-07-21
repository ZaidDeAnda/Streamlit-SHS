
# ==============================================================
# Author: Zaid De Anda
# Twitter: @ndaZaid
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np

#Funciones de filtrado de datos
from filtering import load_data
from filtering import save_data
from filtering import apply_filter

file="100-0.txt"
with open(file, 'rt') as f:
            data = f.read().split('\n')[:-1]
            data = np.array(data).astype(np.float32)

# Sidebar
st.sidebar.title("Selección de modelo")
st.sidebar.markdown(
    """
    Esta barra se puede usar para cambiar el modelo el cuál realizará
    la predicción de la cadena de datos introducida.
    """
)

modelos = ['modelo 1', 'modelo 2', 'modelo 3']
selector_modelos = st.sidebar.selectbox(
    "Selecciona el modelo que se usará:",
    modelos
)

uploaded_file = st.file_uploader("Escoge el archivo")
if uploaded_file is not None:
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    # Can be used wherever a "file-like" object is accepted:
    data = load_data(uploaded_file)
    st.write(data)
    
st.plotly_chart(data)