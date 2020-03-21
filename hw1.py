from typing import List

import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

"""
When downloading data it's better to do it in a global scope instead of a function.
This speeds up the tests significantly
"""
confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    """
    Returns confirmed infection cases for country 'Poland' given a date.
    Ex.
    >>> poland_cases_by_date(7, 3, 2020)
    5
    >>> poland_cases_by_date(11, 3)
    31
    :param year: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param day: Day of month to get the cases for as an integer indexed from 1
    :param month: Month to get the cases for as an integer indexed from 1
    :return: Number of cases on a given date as an integer
    """
    year1=year-2000
    wynik=confirmed_cases.loc[confirmed_cases["Country/Region"]=="Poland"][f"{month}/{day}/{year1}"].values[0]
    return wynik


def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
    """
    Returns the top 5 infected countries given a date (confirmed cases).
    Ex.
    >>> top5_countries_by_date(27, 2, 2020)
    ['China', 'Korea, South', 'Cruise Ship', 'Italy', 'Iran']
    >>> top5_countries_by_date(12, 3)
    ['China', 'Italy', 'Iran', 'Korea, South', 'France']
    :param day: 4 digit integer representation of the year to get the countries for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: A list of strings with the names of the coutires
    """
    year=year-2000
    a=list(confirmed_cases[["Country/Region", f"{month}/{day}/{year}"]].groupby("Country/Region").sum().sort_values(by=f"{month}/{day}/{year}", ascending=False).head(5).index)
    return a

import datetime

def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    """
    Returns the number of countries/regions where the infection count in a given day was the same as the previous day.
    Ex.
    >>> no_new_cases_count(11, 2, 2020)
    35
    >>> no_new_cases_count(3, 3)
    57
    :param day: 4 digit integer representation of the year to get the cases for, defaults to 2020
    :param month: Day of month to get the countries for as an integer indexed from 1
    :param year: Month to get the countries for as an integer indexed from 1
    :return: Number of countries/regions where the count has not changed in a day
    """
    year=year-2000
    dzisiaj=datetime.date(year,month,day)
    wczoraj=dzisiaj-datetime.timedelta(days=1)
    wczoraj=wczoraj.strftime('%m/%d/%y').lstrip("0").replace("/0","/")
    dzisiaj=dzisiaj.strftime('%m/%d/%y').lstrip("0").replace("/0","/")
    new=confirmed_cases.loc[(confirmed_cases[dzisiaj]!=confirmed_cases[wczoraj])].count()[1]
    return int(new)
