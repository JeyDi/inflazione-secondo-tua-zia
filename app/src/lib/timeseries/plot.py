from typing import List
import plotly.express as px
from plotly.graph_objs._figure import Figure
import pandas as pd


def timeseries_pl(df: pd.DataFrame, x: str, y: List[str], title: str) -> Figure:
    fig = px.line(df, x=x, y=y, title=title)
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
    )
    return fig


def timeseries_color_pl(
    df: pd.DataFrame, x: str, y: str, color: str, title: str
) -> Figure:
    fig = px.line(df, x=x, y=y, color=color, title=title)
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
    )
    return fig
