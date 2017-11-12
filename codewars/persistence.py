# Write a function, persistence, that takes in a positive parameter
# num and returns its multiplicative persistence, which is the number
# of times you must multiply the digits in num until you reach a single digit.

# For example:
# persistence(39) => 3 Because 3*9 = 27, 2*7 = 14, 1*4=4 and 4 has only one digit.

# persistence(999) => 4 Because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2.

# persistence(4) => 0   Because 4 is already a one-digit number.


def persistence(n):
    if n <= 10:
        return 0
    else:
        x = str(n)
        count = 0
        while int(x) >= 10:
            mul = 1
            for ch in x:
                mul *= int(ch)
            x = str(mul)
            count += 1

        return count


# Test
print(persistence(39))
print(persistence(999))
print(persistence(4))
print(persistence(25))

print(persistence(167778))
