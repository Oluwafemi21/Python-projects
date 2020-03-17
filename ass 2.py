#defining a function sum with a parameter x
def sum(i):

#this line is initialized to 0 so we can do the addition operation    
    m = 0

#this line defines a for loop for the summation series of m
    for x in range(0,i+1):

        m += x/(x+1)

    return m

def main():
    #this line gets the value of i

    i = eval(input("Enter the value of i :"))
#rounding off the value of m to 4 decimal places
    print(round(sum(i),4))

main()

