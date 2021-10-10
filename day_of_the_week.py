# This code uses Zeller congruence to determine the day of the week

# day=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
""" h is the day of the week
q is the day of the month
m is the month
j is the century (year / 100)
k is the year of the century (year % 100) """

days = {0: 'Saturday', 1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
          8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def get_key(val):
    for key, value in months.items():
        if val == value:
            return key
    return "Key Doesn't Exist"


year = int(input("Enter year (e.g., 2008): "))
month = input("Enter the month: (e.g., January): ").title()
q = int(input("Enter the day of the month: (e.g., 1-31): "))

m = get_key(month)

if month not in months.values():
    print(f"Check your spelling {month}")
elif month == 'January':
    m = 13
    year -= 1
elif month == 'February':
    m = 14
    year -= 1

j = year // 100
k = year % 100

if q in range(1, 32):
    h = (q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7
    h = h // 1
    print(f'The day of the week of {q}/{month}/{year} is {days.get(h)}')
else:
    print(f'A month does not have {q} days')
