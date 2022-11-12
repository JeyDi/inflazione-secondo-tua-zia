import streamlit as st

st.set_page_config(
    page_title="Benvenuto", page_icon="👋", layout="wide", initial_sidebar_state="auto"
)
# from streamlit_option_menu import option_menu
# from app.src.lib import streamlit_utils


def run():
    """
    Main run function for the homepage
    """
    # streamlit_utils.hide_streamlit_menu()

    # streamlit_utils.add_clickable_logo_to_side_menu()

    # with st.sidebar:
    #     option_menu(
    #         "Example",
    #         ["Example 1", "Example 2"],
    #         icons=["house", "cloud-upload"],
    #         menu_icon="cast",
    #         default_index=0,
    #         orientation="horizontal",
    #     )

    st.write("# InflaZia: L'inflazione spiegata alla zia! 👋")

    st.sidebar.success("Seleziona una pagina a sinistra per utilizzare la dashboard")

    st.markdown(
        """
        Questa dashboard nasce con l'idea di dimostrare quanto sia effettivamente reale l'inflazione in Italia in modo da spiegarla in maniera semplice.
        **👈 Seleziona le pagine a sinistra** per interagire con l'applicazione
        ### Vuoi saperne di più?
        - Fai un salto a trovare [Pollo Watzlawick](https://www.youtube.com/channel/UCD-HLhRV_4Z3sYGkgqAnIJw)
        ### Vuoi contribuire?
        Guarda il [codice sulla repository](https://github.com/pieroit/inflazione-secondo-tua-zia) e manda le tue pull request!
        ### Qualche feedback?
        Se trovi degli errori o vuoi proporre qualche modifica puoi aprire una issue [qui](https://github.com/pieroit/inflazione-secondo-tua-zia/issues)
    """
    )
    # page_names_to_funcs = {
    #     "Main Page": run,
    #     "Tempy": page_tempy,
    #     "Table customizable": table_customizable_page,
    #     "Drill down table": drill_down_table_page,
    #     "Drill module table": drill_module_table_page,
    #     "Selectable table": selectable_table_page,
    #     "Comments": comments_page,
    # }

    # selected_page = st.sidebar.selectbox(
    #     "Select a page", page_names_to_funcs.keys(), key="multipage"
    # )
    # page_names_to_funcs[selected_page]()


if __name__ == "__main__":
    run()
