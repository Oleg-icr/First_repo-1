from datetime import datetime

print ("============part 1 ========================")
def string_to_date(date_string):
    parced_date = datetime.strptime(date_string, "%Y.%m.%d").date()
    return parced_date


def date_to_string(date):
    return datetime.datetime(date)


print (string_to_date("2020.01.01"))

print ("============part 2 ========================")

def prepare_user_list(user_data):
    for users in user_data:
        users["birthday"] = datetime.strptime(users["birthday"], "%Y.%m.%d").date()

    return user_data

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

prepared_users = prepare_user_list(users)
print(prepared_users)


