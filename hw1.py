from typing import List

import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "


confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    
    year1=year-2000
    wynik=confirmed_cases.loc[confirmed_cases["Country/Region"]=="Poland"][f"{month}/{day}/{year1}"].values[0]
    return wynik


def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
   
    year=year-2000
    a=list(confirmed_cases[["Country/Region", f"{month}/{day}/{year}"]].groupby("Country/Region").sum().sort_values(by=f"{month}/{day}/{year}", ascending=False).head(5).index)
    return a

import datetime

def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    
    year=year-2000
    dzisiaj=datetime.date(year,month,day)
    wczoraj=dzisiaj-datetime.timedelta(days=1)
    wczoraj=wczoraj.strftime('%m/%d/%y').lstrip("0").replace("/0","/")
    dzisiaj=dzisiaj.strftime('%m/%d/%y').lstrip("0").replace("/0","/")
    new=confirmed_cases.loc[(confirmed_cases[dzisiaj]!=confirmed_cases[wczoraj])].count()[1]
    return int(new)
