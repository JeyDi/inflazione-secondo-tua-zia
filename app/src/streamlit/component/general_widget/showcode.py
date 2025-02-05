import streamlit as st
import inspect
import textwrap


def show_code(demo):
    """Show code inside a Streamlit app using markdown and code widget"""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))
