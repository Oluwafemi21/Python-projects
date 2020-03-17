#importing the maths module
import math

#asking user for the angle
angle = eval(input("Enter the value of the angle: "))

#invoking the radians function to convert the angle to radians
r = math.radians(angle)

#invoking the cosine function to return the cosine value for the radians
x = round(math.sin(r),4)


#finally print the value of x which is the desired value
print('The sine of angle', int(angle), 'is ', x, '.')

