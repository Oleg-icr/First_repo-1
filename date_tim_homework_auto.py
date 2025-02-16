from datetime import datetime


def string_to_date(date_string):
    parced_date = datetime.strptime(date_string, "%Y.%m.%d").date()
    return parced_date


def date_to_string(date):
    return datetime.datetime(date)


print (string_to_date("2020.01.01"))