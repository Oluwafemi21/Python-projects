# This program converts minutes to years and days

minutes = int(input('Enter the number of minutes: '))
years = minutes // 525600
days = (minutes % 525600) // 1440
print(f'{minutes} minutes is approximately {years} years and {days} days.')