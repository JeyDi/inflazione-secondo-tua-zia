from typing import Any, Dict, Optional
from pandas import DataFrame
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


def ag_grid_selection(
    table_df: DataFrame,
    grid_build: GridOptionsBuilder,
    height: int = 400,
    width: Optional[Any] = None,
) -> DataFrame:
    response = AgGrid(
        dataframe=table_df,
        editable=False,
        fit_columns_on_grid_load=True,
        gridOptions=grid_build.build(),
        height=height,
        width=width,
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode=GridUpdateMode.FILTERING_CHANGED
        | GridUpdateMode.SELECTION_CHANGED,  # GridUpdateMode.__members__.get("FILTERING_CHANGED"),
        allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
        enable_enterprise_modules=True,
    )
    return DataFrame(response["selected_rows"])


def ag_grid_selection_simplified(
    table_df: DataFrame,
    visible_columns: Optional[Dict[str, Optional[str]]] = None,
    height: int = 400,
    width: Optional[Any] = None,
) -> DataFrame:
    visible_columns_some = (
        visible_columns
        if visible_columns is not None
        else _all_columns_without_renaming(table_df)
    )
    grid_build = default_grid_build(table_df, visible_columns_some)
    return ag_grid_selection(table_df, grid_build, height, width)


def _all_columns_without_renaming(table_df: DataFrame) -> Dict[str, Optional[str]]:
    return dict(zip(table_df.columns, [None] * len(table_df.columns)))


def default_grid_build(
    df: DataFrame,
    visible_columns: Dict[str, Optional[str]],
    page_size: Optional[int] = None,
) -> GridOptionsBuilder:
    gb = GridOptionsBuilder.from_dataframe(df)
    # Selection rows
    # gb.configure_selection(["single", "multiple"][1])
    gb.configure_selection(
        selection_mode=["single", "multiple"][1],
        use_checkbox=False,
        groupSelectsChildren=True,
        rowMultiSelectWithClick=False,
        suppressRowDeselection=False,
    )
    if page_size:
        gb.configure_pagination(
            paginationAutoPageSize=False, paginationPageSize=page_size
        )
    else:
        gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_default_column(
        groupable=True,
        value=True,
        enableRowGroup=True,
        aggFunc="sum",
        editable=False,
        hide=True,
    )
    for col_name, col_label in visible_columns.items():
        gb.configure_column(col_name, header_name=col_label, hide=False)
    return gb
