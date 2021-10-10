# This program sums up the digits in an integer

integer = eval(input('Enter a number between 0 - 1000: '))
last_digit = integer % 10
digit = integer // 10
second_digit = digit % 10
first_digit = digit // 10
result = first_digit + second_digit + last_digit
print(f'The sum of {integer} is {result}.')

