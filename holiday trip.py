##This program is to book a holiday trip
print('Welcome to WAKANOW.NG')
location = input("Where would you like to spend your summer?: ").title()
countries = ['America', 'United Kingdom', 'Canada', 'Germany', 'Spain', 'Italy', 'Brazil', 'Dubai']
airlines = ['Emirates', 'Peace','Qatar airways','Ethopian airlines']
if location == 'America':
    state = input('Which state in America do you wish to go: ').title()
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 650,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 4am, 6:45am, 10am, 3pm')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', state , 'which will take about \n 13 hours and your time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
elif location == 'United Kingdom':
    state = input('Which state in the United Kingdom do you wish to go: ')
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 550,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 5am, 7:45am, 11am, 4pm, 7pm, 10:30pm')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', state , 'which will take about \n8 hours time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
elif location == 'Canada':
    state = input('Which state in the Canada do you wish to go: ')
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 600,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 4am,7:45am, 11am, 3pm, 6pm.')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', state , 'which will take about \n10 hours time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
elif location == 'Germany':
    state = input('Which state in the Germany do you wish to go: ')
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 400,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 4am,7:45am, 11am, 3pm, 6pm.')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', state , 'which will take about \n16 hours time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
elif location == 'Brazil':
    state = input('Which state in the Brazil do you wish to go: ')
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 350,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 4am,7:45am, 11am, 3pm, 6pm.')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', state , 'which will take about \n9 hours time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
elif location == 'Spain':
    state = input('Which state in the Spain do you wish to go: ')
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 550,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 4am,7:45am, 11am, 3pm, 6pm.')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', state , 'which will take about \n11 hours time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
elif location == 'Italy':
    state = input('Which state in the Italy do you wish to go: ')
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 480,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 4am,7:45am, 11am, 3pm, 6pm.')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', state , 'which will take about \n9 hours time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
elif location == 'France':
    state = input('Which state in the France do you wish to go: ')
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 550,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 4am,7:45am, 11am, 3pm, 6pm.')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', state , 'which will take about \n9 hours time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
elif location == 'Dubai':
    ai = input('Which airline do you wish to use: ').title()
    if ai in airlines:
        print('The ticket fee is 380,000 naira')
    else:
        print('Thank you.')
    ans = input('Do you wish to continue: ').title()
    if ans == 'Yes':
        print('The flight times available are: \n1am, 4am,7:45am, 11am, 3pm, 6pm.')
        time_of_flight = input("Enter the time suitable for you: ")
        print('You have successfully booked a flight to', location , 'which will take about \n7 hours time of departure is', time_of_flight)
        print("Have a nice summer.")
    else:
        print("Thank you.")
else:
    print('Thank you for visiting our page.')
        
    
    



