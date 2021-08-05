import random

# We want the computer to guess our number
print('WELCOME TO GUESSER 2.0!!')
print('INSTRUCTION: \nThe computer will make an attempt to guess your number. \nFollow the prompt by inputing if it is correct or not. \nHave Fun!!')

def computer_guess(x):
    low = 1
    
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C): ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed your number, {guess}, correctly!.')

computer_guess()