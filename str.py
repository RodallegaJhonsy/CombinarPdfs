import streamlit as st
from PyPDF2 import PdfMerger
import os

# Función para combinar PDFs
def combinar_pdfs(archivos):
    merger = PdfMerger()
    for archivo in archivos:
        merger.append(archivo)
    merger.write("pdf_combinado.pdf")
    merger.close()

# Título de la aplicación
st.title('Combinador de PDFs')

# Widget para cargar archivos PDF
archivos = st.file_uploader('Cargar archivos PDF', accept_multiple_files=True)

# Botón para combinar PDFs
if st.button('Combinar PDFs'):
    if archivos:
        combinar_pdfs(archivos)
        st.success('PDFs combinados exitosamente en "pdf_combinado.pdf"')
    else:
        st.warning('Por favor, carga al menos un archivo PDF')

# Botón de descarga del PDF combinado
if os.path.exists("pdf_combinado.pdf"):
    with open("pdf_combinado.pdf", "rb") as f:
        st.download_button(label="Descargar PDF Combinado", data=f, file_name="pdf_combinado.pdf", mime="application/pdf")
