import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos de la encuesta
data = pd.read_csv('encuesta.csv')

# Función para generar el informe numérico
def generate_numeric_report():
    st.title('Informe Numérico')
    st.write('---')
    st.write('**Total de respuestas:**', len(data))
    st.write('---')
    st.write('**Preguntas y respuestas:**')
    for column in data.columns:
        st.write(f'**{column}:**')
        st.write(data[column].value_counts())
        st.write('---')

# Función para generar el informe gráfico
def generate_visual_report():
    st.title('Informe Gráfico')
    st.write('---')
    st.write('**Gráfico de barras:**')
    for column in data.columns:
        if data[column].dtype == 'object':
            plt.figure(figsize=(10, 6))
            sns.countplot(data[column])
            plt.xticks(rotation=45)
            st.pyplot()
            st.write('---')

# Configurar la interfaz de Streamlit
st.title('Análisis de Resultados de Encuesta')

# Mostrar las opciones de informe
report_type = st.radio('Selecciona el tipo de informe:', ('Numérico', 'Gráfico'))

# Generar el informe seleccionado
if report_type == 'Numérico':
    generate_numeric_report()
elif report_type == 'Gráfico':
    generate_visual_report()
