import streamlit as st

st.set_page_config(
    page_title="risutati",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="auto",
)
# import time
# import numpy as np
# from app.src.lib import streamlit_utils
# from app.src.streamlit.component.general_widget.showcode import show_code


# def page_tempy():
#     st.title("")
#     st.subheader("")
#     streamlit_utils.hide_streamlit_menu()
#     st.sidebar.header("Tempy info page")
#     st.write(
#         """This demo illustrates a combination of plotting and animation with
#     Streamlit. We're generating a bunch of random numbers in a loop for around
#     5 seconds. Enjoy!"""
#     )

#     st.markdown(
#         """
#             This is a simple dashboard designed with the new version of streamlit.

#             **Streamlit** for the interactive HTML dashboards
#             - Streamlit webpage: https://blog.streamlit.io/
#             - Documentation: https://docs.streamlit.io/library/get-started

#             **Ag Grid** for interactive, paginated tables
#             - For Python: https://blog.ag-grid.com/pablo-fonseca-streamlit/
#             - For JS: https://www.ag-grid.com/

#             **Plotly Events** from streamlit
#             - https://github.com/null-jones/streamlit-plotly-events

#             **Multipage capabilities**
#             - https://docs.streamlit.io/library/get-started/multipage-apps

#         """
#     )

#     progress_bar = st.sidebar.progress(0)
#     status_text = st.sidebar.empty()
#     last_rows = np.random.randn(1, 1)
#     chart = st.line_chart(last_rows)

#     for i in range(1, 101):
#         new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#         status_text.text("%i%% Complete" % i)
#         chart.add_rows(new_rows)
#         progress_bar.progress(i)
#         last_rows = new_rows
#         time.sleep(0.05)

#     progress_bar.empty()

#     # Streamlit widgets automatically run the script from top to bottom. Since
#     # this button is not connected to any other logic, it just causes a plain
#     # rerun.
#     st.button("Re-run")

#     show_code(page_tempy)


# page_tempy()
