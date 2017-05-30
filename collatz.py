def collatz(num):
    temp_num = num
    count = 1
    new_str = 0
    print(temp_num, end=", ")
    while temp_num != 1:
        if temp_num % 2 == 0:
            temp_num = temp_num // 2
        elif temp_num % 2 == 1:
            temp_num = 3 * temp_num + 1

        count += 1
        new_str += 1

        print(temp_num, end=", ")
        if new_str == 25:
            new_str = 0
            print(end="\n")

    print(end='\n')
    return count

number = int(input("Eneter a number = "))

print("The sequence for " + str(number) + " takes " + str(collatz(number)) + " steps")
