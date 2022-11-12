from pandas import DataFrame


def semi_join(
    left: DataFrame, right: DataFrame, left_on: str, right_on: str
) -> DataFrame:
    semi = right[right_on].drop_duplicates() if not right.empty else []
    is_in = left[left_on].isin(semi)
    return left[is_in]


def semi_join_if_any(
    left: DataFrame, right: DataFrame, left_on: str, right_on: str
) -> DataFrame:
    if right.empty:
        return left
    else:
        return semi_join(left, right, left_on, right_on)


def anti_join(
    left: DataFrame, right: DataFrame, left_on: str, right_on: str
) -> DataFrame:
    semi = right[right_on].drop_duplicates()
    is_in = left[left_on].isin(semi)
    return left[~is_in]


# def semi_join(
#     left: DataFrame, right: DataFrame, left_on: str, right_on: str
# ) -> DataFrame:
#     semi_table = left.merge(how="inner", right=right, left_on=left_on, right_on=right_on)
#     in_both = left[left_on].isin(semi_table[left_on])
#     return left[in_both]
