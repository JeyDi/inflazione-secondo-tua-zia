from datetime import timedelta, date
from typing import Any, Optional
import numpy as np
import datetime as dt

import pandas as pd

# from typing import Any, Callable, TypeVar
# SF = TypeVar("SF", bound=Callable[..., Any])
# VF = TypeVar("VF", bound=Callable[..., np.array])

# vectorize: Callable[[SF], VF] = np.vectorize


@np.vectorize
def first_day_of_month(any_day: date) -> date:
    return any_day.replace(day=1)


@np.vectorize
def last_day_of_month(any_day: date) -> date:
    # this will never fail
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - timedelta(days=next_month.day)


@np.vectorize
def last_day_of_week(date: date) -> date:
    start = date - timedelta(days=date.weekday())
    end = start + timedelta(days=6)
    return end


# milliseconds


@np.vectorize
def ms_to_date(ms):
    return dt.datetime.fromtimestamp(ms / 1000.0) if pd.notnull(ms) else None


@np.vectorize
def date_to_ms(x):
    format = "%Y-%m-%d %H:%M:%S"
    return dt.datetime.strptime(x, format).timestamp() * 1000 if pd.notnull(x) else None


# Strings


@np.vectorize
def str_to_date(x: str, format="%Y-%m-%d"):
    return dt.datetime.strptime(x, format).date()


@np.vectorize
def date_to_str(x: date, format="%Y-%m-%d"):
    return x.strftime(format) if not pd.isnull(x) else np.nan


@np.vectorize
def str_to_datetime(x: str, format="%Y-%m-%d %H:%M:%S"):
    return dt.datetime.strptime(x, format)


@np.vectorize
def datetime_to_str(x: date, format="%Y-%m-%d %H:%M:%S"):
    return x.strftime(format) if not pd.isnull(x) else np.nan


# generic


@np.vectorize
def acquire_date(x: Optional[Any], format="%Y-%m-%d %H:%M:%S"):
    if isinstance(x, str):
        return dt.datetime.strptime(x, format).date() if not pd.isnull(x) else np.nan
    elif isinstance(x, dt.date):
        return x
    else:
        return np.nan
