def collatz(num):
    try:
        num = int(num)
        count = 1
        new_str = 0
        print(num, end=", ")
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            elif num % 2 == 1:
                num = 3 * num + 1

            count += 1
            new_str += 1

            print(num, end=", ")
            if new_str == 25:
                new_str = 0
                print(end="\n")

        print(end='\n')
        return count
    except ValueError:
        print("number must be signed integer")

number = input("Eneter a number = ")

print("The sequence for " + str(number) + " takes " + str(collatz(number)) + " steps")
