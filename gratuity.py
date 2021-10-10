# This program calculates the tips
subtotal,gratuity_rate = eval(input('Enter the subtotal and gratuity rate: '))
gratuity = ( gratuity_rate / 100 ) * subtotal
total = gratuity + subtotal
print(f'The gratuity is {round(gratuity,2)} and the total is {round(total,2)}.')