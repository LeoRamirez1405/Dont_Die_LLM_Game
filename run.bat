@echo off
REM Cambia al directorio donde se encuentra el .bat
cd /d %~dp0

REM Ejecutar Streamlit
streamlit run Home.py

