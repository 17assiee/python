#1
x=[2,3,4,5,6,88]
x.reverse()
print('new list: ', x)

#2
def change(x):
    x[0], x[-1] = x[-1], x[0]
    return x
print(change([2,4,6,7,88]))

#3
def to_list(*args):
    return list(args)
print(to_list(3,55,66,77))

#4
def useless(lst):
    return max(lst) / len(lst)
print(useless([4,77,88,99]))

#5
def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst
print(list_sort([44,55,66,77]))

#6
def all_eq(lst):
    max_i = max(lst, key=lambda x: len(x))
    max_l = len(max_i)
    return [item.ljust(max_l, '_') for item in lst]
print(all_eq(['fff', 'bear', 'lll']))
