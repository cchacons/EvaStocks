"""
Download and save S&P 500 company names, ticker symbols, and industry sectors as a csv file.
Source from Wikipedia page: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies.
Requires beautiful-soup4, html5lib and lxml.
"""

import pandas as pd
from pandas import DataFrame, read_html


def stock_downloader(source):
    # read company info into a list
    companies_list = read_html(source)
    companies = companies_list[0]

    # deal with header
    columns = companies.ix[0]
    companies.columns = columns.values
    companies = companies.drop(0)

    # only include Security, Ticker symbol and GICS Sector
    companies_dframe = DataFrame(companies, columns=["Security", "Ticker symbol", "GICS Sector"])

    return companies_dframe


def stock_saver(source, filename):
    companies_dframe = stock_downloader(source)

    # save as a csv file
    companies_dframe.to_csv(filename)


if __name__ == "__main__":
    source = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    filename = "sp500.csv"

    stock_saver(source, filename)

    # read data from csv file
    companies_dframe = pd.read_csv(filename)
    print companies_dframe.info()
