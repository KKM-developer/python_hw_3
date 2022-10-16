# task_1
def find_odd_sum(a):
    sum = 0
    for i in range(len(a)):
        if i % 2 == 1:
            sum += a[i]
    return sum


some_list = [2, 3, 5, 9, 3]
print(find_odd_sum(some_list))


# task_2
def find_elem_mult(a):
    new_list = []
    first_elem = 0
    last_elem = -1
    len_new_list = len(a) / 2
    if len(a) % 2 == 1:
        len_new_list += 0.5
    for i in range(int(len_new_list)):
        new_list.append(a[first_elem] * a[last_elem])
        first_elem += 1
        last_elem -= 1
    return new_list


some_list1 = [2, 3, 4, 5, 6]
some_list2 = [2, 3, 5, 6]
print(find_elem_mult(some_list1))
print(find_elem_mult(some_list2))

# task_3
from math import modf


def find_diff(a):
    max_elem = modf(a[0])[0]
    min_elem = modf(a[0])[0]
    for elem in a:
        if modf(elem)[0] > max_elem:
            max_elem = modf(elem)[0]
        elif modf(elem)[0] < min_elem:
            min_elem = modf(elem)[0]
    return round((max_elem - min_elem), 2)


some_list = [1.1, 1.2, 3.1, 5, 10.01]
print(find_diff(some_list))

