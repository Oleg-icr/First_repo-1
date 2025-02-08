from datetime import datetime, timezone

# Створення об'єкта datetime
now = datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7,

print("===================================================")

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print("Local time now:" ,local_now)
print("UTC now       :" , utc_now)  # Виведе поточний час в UTC

print("===================================================")

from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)
print (utc_time)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)

