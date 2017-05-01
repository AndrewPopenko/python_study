ls = []
sum = 0
min_d = None
max_d = None

while True:
    try:
        d = input("enter a number or Enter to finish: ")

        if not d:
            break

        d = int(d)
        sum += d
        ls += [d] #ls.append(d)

        if min_d is None or d < min_d:
            min_d = d

        if max_d is None or d > max_d:
            max_d = d

    except ValueError as err:
        print(err)

print("numbers: ", ls)
print("[ count = ", len(ls), "] [ sum = ", sum, "] [ lowest = ", min_d, "] [ highest = ", max_d, "]", "[ mean = ", sum / len(ls), "]")