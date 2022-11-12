from typing import Any, Dict, Generic, List, TypeVar
from pydantic import BaseModel
from streamlit_plotly_events import plotly_events


X = TypeVar("X")
Y = TypeVar("Y")


class TsSelection(BaseModel, Generic[X, Y]):
    """Class representing the plotly user selection, which is the dictionary
    returned by the function `plotly_events`.

    See `plotly_events` return value for more information.

    Args:
        x (X): x quantity of the plot

        y (Y): y quantity of the plot

        curveNumber (int): position index of the curve

        pointNumber (int): position index of the point??

        pointIndex (int): position index of the point??
    """

    x: X
    y: Y
    curveNumber: int
    pointNumber: int
    pointIndex: int


def plotly_selection(
    plot_df,
    plot_fun,
    click_event=True,
    select_event=False,
    hover_event=False,
    override_height=450,
    override_width="100%",
    key=None,
):
    """This function creates an interactive plot for streamlit and returns the selected dataframe.

    Args:
        plot_df (DataFrame): the exact data used by plotly to create the plot.
        plot_fun (Call[[Dataframe], plotly figure]): unary function to create the plot.
        click_event (bool, optional): "plotly_events" argument. Defaults to True.
        select_event (bool, optional): "plotly_events" argument. Defaults to False.
        hover_event (bool, optional): "plotly_events" argument. Defaults to False.
        override_height (int, optional): "plotly_events" argument. Defaults to 450.
        override_width (str, optional): "plotly_events" argument. Defaults to "100%".
        key (str, optional): "plotly_events" argument. Defaults to None.

    Returns:
        DataFrame:
    """
    ts_selection_raw_ls: List[Dict[str, Any]] = plotly_events(
        plot_fig=plot_fun(plot_df),
        click_event=click_event,
        select_event=select_event,
        hover_event=hover_event,
        override_height=override_height,
        override_width=override_width,
        key=key,
    )
    ts_selection_ls: List[TsSelection] = [
        TsSelection.parse_obj(ts_selection) for ts_selection in ts_selection_raw_ls
    ]
    index_ls = [x.pointIndex for x in ts_selection_ls]
    flight_n_tbl_selection = plot_df.iloc[index_ls]
    # st.markdown("Click on the time series to see the coordinates:")
    # st.write(str(ts_selection_ls))
    return flight_n_tbl_selection
