import streamlit as st
import random as rd
import extra_streamlit_components as stx
import datetime


## This module can be imported to get the cookie_manager instance used to manage the user cookies.
@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def get_manager():
    return stx.CookieManager()


cookie = get_manager()


def set_user_tag():
    if cookie.get("user_tag") is None:
        cookie.set(
            "user_tag",
            f"{rd.randint(1111, 9999)}-{rd.randint(1111, 9999)}-{rd.randint(1111, 9999)}-{rd.randint(1111, 9999)}",
            expires_at=datetime.datetime.now() + datetime.timedelta(days=365),
        )
