import streamlit as st

st.set_page_config(
    page_title="Note",
    page_icon="🤠",
    layout="wide",
    initial_sidebar_state="auto",
)
from app.src.lib import streamlit_utils

## This page is used to provide an interface to give text feedbacks


def comments_page():
    streamlit_utils.hide_streamlit_menu()
    st.title("Note e informazioni")
    st.markdown(
        """
        Ti è piaciuta la nostra dashboard?
        * Collabora e tieniti in contatto con noi
        * Facci sapere come la pensi
        * Proponi dei suggerimenti o delle modifiche
        * Segnala qualche problema
        
        Trovi tutto qui!
        
        [Github](https://github.com/pieroit)
        """
    )


comments_page()
