import streamlit as st


def add_clickable_logo_to_side_menu(
    link="https://github.com/pieroit",
    path: str = "https://avatars.githubusercontent.com/u/6328377?v=4",
):
    with st.sidebar:
        _, col2, _ = st.columns([1, 4, 1])
        col2.markdown(
            f"""
            <a href="{link}">
                <img alt="link to github" src="{path}" id="logo_clickable" width="100%">
            </a>""",
            unsafe_allow_html=True,
        )


def initialize_session_variables(variables_to_set={"example": 0}):
    """Initialize the session variables if they don't already exist"""
    for variable, value in variables_to_set.items():
        if st.session_state.get(variable) is None:
            st.session_state[variable] = value


def hide_streamlit_menu():
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)


def initialize_or_update_session_variables(variables_to_set={}, allow_update=False):
    """
    Provide a dictionary of variables to set and their values.
    By default it will only allow initialization of variables that don't already exist.

    Args:
        variables_to_set (dict): dictionary of variables to set and their values
        allow_update (bool): if True, will allow updating of existing variables. Defaults to False.
    Returns:
        None

    """
    for key, value in variables_to_set.items():
        if st.session_state.get(key) is None:
            st.session_state[key] = value
        else:
            if allow_update:
                st.session_state[key] = value


def force_non_empty(field, name_field: str):
    """Force a field to be non-empty in a form"""
    if field == "":
        st.error(f"{name_field} cannot be empty")
        st.stop()
