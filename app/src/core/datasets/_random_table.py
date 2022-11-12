import streamlit as st
import pandas as pd
import numpy as np
from itertools import cycle
from app.src.lib.logger import logger

np.random.seed(42)


@st.cache(allow_output_mutation=True)
def fetch_data(samples):
    logger.info("fetching data...")

    cycle(
        [
            pd.Timedelta(weeks=-2),
            pd.Timedelta(days=-1),
            pd.Timedelta(hours=-1),
            pd.Timedelta(0),
            pd.Timedelta(minutes=5),
            pd.Timedelta(seconds=10),
            pd.Timedelta(microseconds=50),
            pd.Timedelta(microseconds=10),
        ]
    )
    dummy_data = {
        "date_time_naive": pd.date_range("2021-01-01", periods=samples),
        "apple": np.random.randint(0, 100, samples) / 3.0,
        "banana": np.random.randint(0, 100, samples) / 5.0,
        "chocolate": np.random.randint(0, 100, samples),
        "group": np.random.choice(["A", "B"], size=samples),
        "date_only": pd.date_range("2020-01-01", periods=samples).date,
        # "timedelta": [next(deltas) for i in range(samples)],
        "date_tz_aware": pd.date_range(
            "2022-01-01", periods=samples, tz="Asia/Katmandu"
        ),
    }
    return pd.DataFrame(dummy_data)
