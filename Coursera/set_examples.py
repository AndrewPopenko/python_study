odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print("odd set: " + str(odd_set))
print("even set: " + str(even_set))

union_set = odd_set | even_set
print("union_set: " + str(union_set))

union_set = odd_set.union(even_set)
print("union_set: " + str(union_set))

intersection_set = odd_set & even_set
print("intersection_set: " + str(intersection_set))

intersection_set = odd_set.intersection(even_set)
print("intersection_set: " + str(intersection_set))

difference_set = odd_set - even_set
print("difference_set" + str(difference_set))

difference_set = odd_set.difference(even_set)
print("difference_set" + str(difference_set))

symmetric_difference_set = odd_set ^ even_set
print("symmetric_difference_set :" + str(symmetric_difference_set))

symmetric_difference_set = odd_set.symmetric_difference(even_set)
print("symmetric_difference_set :" + str(symmetric_difference_set))

even_set.remove(2)
print("even set : " + str(even_set))
