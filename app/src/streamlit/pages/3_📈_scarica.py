import streamlit as st

st.set_page_config(
    page_title="download",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="auto",
)
from app.src.lib import streamlit_utils
from app.src.core.datasets.download import download_data


def download_page():
    streamlit_utils.hide_streamlit_menu()
    st.title("Scarica i dati")
    st.markdown(
        """
        Per scaricare i dati da visualizzare puoi premere il seguente pulsante
        """
    )
    button_download = st.button("Scarica i dati", key="download_button")

    if button_download:
        download_data()
        st.markdown(
            "Download completato! I dati sono stati scaricati all'interno del progetto!"
        )


download_page()
