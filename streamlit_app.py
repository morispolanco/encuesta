import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Configurar la interfaz de Streamlit
    st.title('Análisis de Resultados de Encuesta')

    # Widget para cargar el archivo CSV
    uploaded_file = st.file_uploader('Cargar archivo CSV de encuesta', type='csv')

    # Verificar si se ha cargado un archivo
    if uploaded_file is not None:
        # Leer el archivo CSV
        data = pd.read_csv(uploaded_file)

        # Mostrar los datos de la encuesta
        st.write('**Datos de la encuesta:**')
        st.write(data)

        # Realizar análisis numérico
        st.write('**Análisis numérico de la encuesta:**')
        st.write(data.describe())

        # Realizar análisis gráfico
        st.write('**Análisis gráfico de la encuesta:**')
        for column in data.columns:
            if data[column].dtype == 'object':
                # Gráfico de barras para variables categóricas
                plt.figure(figsize=(10, 6))
                sns.countplot(data=data, x=column)
                plt.xticks(rotation=45)
                st.pyplot()

            else:
                # Histograma para variables numéricas
                plt.figure(figsize=(10, 6))
                sns.histplot(data=data, x=column, kde=True)
                st.pyplot()

    else:
        st.write('Esperando a que se cargue un archivo...')

if __name__ == '__main__':
    main()
