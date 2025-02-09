from datetime import datetime, timezone, timedelta

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

utc_time = datetime.now(timezone.utc)
print (utc_time)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)

print("===================================================")

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
print (timezone_offset)
print (timezone_datetime)
# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)

print("===================================================")

import time

current_time = time.time()
print(f"Поточний час: {current_time}")

print("===================================================")

current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

print("===================================================")

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

print("===================================================")

# Записуємо час на початку виконання
start_time = time.perf_counter()
print (start_time)

# Виконуємо якусь операцію
for _ in range(1000000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()
print (end_time)
# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

