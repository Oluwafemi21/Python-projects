## This program is to recommend to people
age = eval(input("How old are you :"))
if age >= 16:
    print("Welcome to FILMHOUSE CINEMA UNILAG.")
    list1 = ["Jexi" , "Gemini man", "The Witcher", "Silencer", "Dark room", "Mayhem in Mumbai"]
    print("The following are the movies showing this week:\n ",list1)
    s1 = input("Which movie would you like to watch? ").title()
    if s1 in list1:
        p1 = input("The price of the movie is #1000.")
        print("Ticket successfully purchased. Cashier would direct you to the theatre. \n Thank you")
    else:
        print("The movie is not available. ")
else:
    print("You are not eligible to use this platform. Thank you")
              
