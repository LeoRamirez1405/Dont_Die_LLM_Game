import streamlit as st
from Game import Game

def run():
    import streamlit as st

    # Configuración inicial de la página
    st.set_page_config(page_title="Don't Die", page_icon="👻")

    # Título centrado y con un tamaño específico
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Don't Die 👻: Sobrevive o Muere Intentando</h1>", unsafe_allow_html=True)

    # Subtítulo opcionalmente centrado y con un tamaño diferente
    st.markdown("<h2 style='text-align: center; font-size: 20px;'>Un Juego de Aventura en el Umbral de la Muerte</h2>", unsafe_allow_html=True)
    
    game = Game()

    msg = st.chat_input()

    if not msg:
        st.stop()

    with st.chat_message("user"):
        st.write(msg)

    with st.chat_message("assistant"):
        # st.write_stream(bot.submit(msg, context=5))
        st.write('Hello')