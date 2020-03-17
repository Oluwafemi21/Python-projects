print("         Sum Series Table")
#Display the headers
print("    i         |          m(i)  ")
print("______________|____________________")
#Display table body
for i in range(1,10):
    m = 0
    #the formula to get respective values of m 
    for x in range(1,i+1):
          m += x/(x+1)
    print("  ",i , "         |", '  ',round(m,4))
     
for i in range(10,21):
    m = 0
    for x in range(1,i+1):
          m += x/(x+1)
    print(" ",i , "         |", '  ',round(m,4))
     
    


