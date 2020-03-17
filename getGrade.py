def getGrade(score):
    if score >= 70:
        result = 'A'
    elif score >= 60:
        result = 'B'
    elif score >= 50:
        result = 'C'
    elif score >= 40:
        result = 'D'
    elif score >= 30:
        result = 'E'
    else:
        result = 'F'

    return result
def main():
    x = eval(input('What is your score? '))
    print("Your grade is ", getGrade(x),'.')

main()
