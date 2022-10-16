# task_1
def find_odd_summ (a):
    summ = 0
    for i in range(len(a)):
        if i%2 == 1:
            summ+=a[i]
    return summ


some_list = [2, 3, 5, 9, 3]
print(find_odd_summ(some_list))

