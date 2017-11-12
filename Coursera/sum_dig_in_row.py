import sys


digits = sys.argv[1]

summ = 0

for ch in digits:
    if not ch.isdigit():
        print("use only digits")
        break

    summ += int(ch)

print(summ)
