import pandas as pd

from newscraping.application.scraping import after_date, latest


def test_after_date():
    o = after_date("2020-12-25", "reuters")
    assert isinstance(o, pd.DataFrame)


def test_latest():
    o = latest(5, "reuters")
    assert isinstance(o, pd.DataFrame)
