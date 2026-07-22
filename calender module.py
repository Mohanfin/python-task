import calendar

# 1. Whole year calendar
print("1. calendar(year)")
print(calendar.calendar(2026))

# 2. Particular month
print("2. month(year, month)")
print(calendar.month(2026, 6))

# 3. First weekday and number of days
print("3. monthrange(year, month)")
print(calendar.monthrange(2026, 6))

# 4. Leap year check
print("4. isleap(year)")
print(calendar.isleap(2024))

# 5. Count leap years
print("5. leapdays(y1, y2)")
print(calendar.leapdays(2000, 2026))

# 6. Weekday number
print("6. weekday(year, month, day)")
print(calendar.weekday(2026, 6, 5))

# 7. Month name
print("7. month_name[index]")
print(calendar.month_name[6])

# 8. Day name
print("8. day_name[index]")
print(calendar.day_name[4])

# 9. Month calendar as nested list
print("9. monthcalendar(year, month)")
print(calendar.monthcalendar(2026, 6))

# 10. Set first weekday as Sunday
print("10. setfirstweekday(day)")
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2026, 6))