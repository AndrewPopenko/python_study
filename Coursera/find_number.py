import random


number = random.randint(0,100)

while True:
    answer = input("Enter a number: ")

    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Enter only digits")
        continue

    answer = int(answer)

    if(answer < number):
        print("Your number less than the quiz number")
    elif answer > number:
        print("Your number greater than the quiz number")
    else:
        print("You won!!! quiz number is = " + str(number))
        break
