# polzovatel podaet na vhod maksimum
# vyvodit w file txt zadania
# X + y = z; x - y = z;
# x + y + z = w; x - y - z = w; x - y + z = w; kol-vo neizvestnych = 2;
# x + y + z + w = u; x - y - z - w = u; if max > 10; kol-vo neizvestnych = 2;
import random


def get_random_digit(begin=0, end=1):
    return random.randint(begin, end)


def make_string_old(lst, act):
    res_str = str.format("{} ")


def make_string(lst, act):
    result = ""
    index_lst = 0
    index_act = 0
    for l in lst:
        result += str(l)
        if index_lst % 2 == 0 and index_act < len(act):
            result += act[index_act]
            index_act += 1
    result += "; "
    return result


def get_list(lst):
    index = random.randint(1, len(lst))-1
    elm = lst[index]
    if elm >= 10:
        lst[index] = "  "
    else:
        lst[index] = " "
    return lst

xyz = []
xyz_debug = []

max_num = int(input("Введи максимальное число = "))

max_symb_three = 95
max_symb_four = 87

list_xyz = []
list_xyz_debug = []

i = 0
x = 0
y = 0
z = 0
string = ""
string_debug = ""

while i < 36:
    # z = random.randint(0, max_num)
    z = get_random_digit(end=max_num)

    if z != 0:
        if random.choice([True, False]):
            x = get_random_digit(end=z)
            y = z - x
            xyz = get_list([x, y, z])
            string = make_string(xyz, [" + ", " = "])
            string_debug = make_string([x, y, z], [" + ", " = "])
        else:
            x = get_random_digit(end=max_num)
            if z > x:
                t = x
                x = z
                z = t
            y = x - z
            xyz = get_list([x, y, z])

            string = make_string(xyz, [" - ", " = "])
            string_debug = make_string([x, y, z], [" - ", " = "])
    else:
        x = get_random_digit(1, max_num)
        xyz = get_list([x, x, z])
        string = make_string(xyz, [" - ", " = "])
        string_debug = make_string([x, x, z], [" - ", " = "])

    list_xyz.append(string)
    list_xyz_debug.append(string_debug)

    i += 1

#with open("ex.txt", "w") as out_file:
#    out_file.write("x + y = z")

print(list_xyz)
print(list_xyz_debug)

count = 0

# "00 + 00 = 00; "
ls_str = []
tmp_str = ""
i = 0
for ls in list_xyz:
    if i == 2:
        tmp_str += ls+  "\n"
        i = 0
        ls_str.append(tmp_str)
        tmp_str = ""
    else:
        tmp_str += ls
        i += 1


with open("ex1.txt", "w") as out_file:
    for ls in ls_str:
    #    count += len(ls)
    #    if count >= max_symb_three-10:
    #        out_file.write(ls + "\n")
    #        count = 0
        out_file.write(ls)
    #out_file.write(ls_str)
out_file.close()