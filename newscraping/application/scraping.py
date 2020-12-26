"""This module provides functions for web scraping. 

Functions
-------
after_date
latest

"""

import click
import pandas as pd

import newscraping.settings.base as stg
from newscraping.infrastructure.infra import WebScraper


@click.command()
@click.argument("early_date")
@click.argument("newspaper")
def after_date(early_date: str, newspaper: str):
    """Scrape all headlines published after a user-specified date from a newspaper website,
    starting with the most recent ones.

    \b
    Parameters
    ----------
    early_date : str
        Start of the period to scrape headlines from. Ex: "2020-12-25"
    newspaper : str
        Name of the newspaper to scrape headlines from. Ex: "reuters"

    \b
    Returns
    -------
    DataFrame
        Headlines with dates and newspaper name
    """
    if newspaper in stg.PARAMS_NEWSPAPER.keys():
        params = stg.PARAMS_NEWSPAPER[newspaper]
        params["early_date"] = early_date
        headlines = WebScraper(**params).get_headlines()

        print(headlines.head())
        return headlines

    else:
        print(f"The newspaper {newspaper} is not available.")


@click.command()
@click.argument("n_articles", type=int)
@click.argument("newspaper")
# @click.option("--newspaper", type=click.Choice(stg.SCRAPING_WEBSITES, case_sensitive=False))
def latest(n_articles: int, newspaper: str):
    """
    Scrape a user-specified number of headlines from a newspaper website,
    starting with the most recent ones.

    \b
    Parameters
    ----------
    n_articles : int
        Number of headlines to scrape. Ex: 5
    newspaper : str
        Name of the newspaper to scrape headlines from. Ex: "reuters"

    \b
    Returns
    -------
    DataFrame
        Headlines with dates and newspaper name
    """
    if newspaper in stg.PARAMS_NEWSPAPER.keys():
        params = stg.PARAMS_NEWSPAPER[newspaper]
        params["n_articles"] = n_articles
        print(params)
        headlines = WebScraper(**params).get_headlines()

        print(headlines.head(min(5, n_articles)))
        return headlines

    else:
        print(f"The newspaper {newspaper} is not available.")


if __name__ == "__main__":
    pass
