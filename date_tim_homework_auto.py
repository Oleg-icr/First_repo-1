from datetime import datetime


def string_to_date(date_string):
    parced_date = datetime.strptime(date_string, "%Y.%m.%d")
    return parced_date.date


def date_to_string(date):
    return datetime.datetime(date)

