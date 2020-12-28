import pandas as pd

from newscraping.application.scraping import news


def test_news_return_type():
    df = news(newspaper="reuters", n_articles=-1, early_date="2020-01-01")
    assert isinstance(df, pd.DataFrame)


def test_news_shape_1():
    df = news(newspaper="reuters", n_articles=-1, early_date="2020-01-01")
    assert df.shape[0] == 1


def test_news_shape_5():
    df = news(newspaper="reuters", n_articles=5)
    assert df.shape[0] == 5


def test_news_early_date():
    early_date = "2020-12-23"
    df = news(newspaper="reuters", early_date=early_date)
    assert df.iloc[-1, 1] == early_date
