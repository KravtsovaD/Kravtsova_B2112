# import math
from operator import index
from random import randint
#
# lst = []
# print(lst)
# lst.append(math.pi)
# lst.append(math.e)
# print(lst)
# lst.clear()
# print(lst)
#
# size = int(input())
# for i in range(size):
#     lst.append(randint(-10, 10))
# print(lst)
#
# print(lst[3])
#
# lst2 =[randint(-10,10) for i in range(10)]
# print(lst2)
#
# lstNum = [i for i in range(10)]
# print(lstNum)
#
# lst_even = [i for i in range(10) if i % 2 == 0]
# print(lst_even)
#
# lst_odd = [i for i in range(10) if i % 2 != 0]
# print(lst_odd)
#
# lst_mult_square = [i**2 for i in range(10)]
# print(lst_mult_square)
#
# for i in lst_mult_square:
#     print(i)

lst = [randint(-10,10)for i in range(20)]
print(lst)

sum_negative = 0

for num in lst:
    if num < 0: sum_negative += num
print("Sum negative item list: ", sum_negative)

sum_even = 0

for num in lst:
    if num % 2 == 0: sum_even +=num
print("Sum even item list: ", sum_even)

sum_odd = 0

for num in lst:
    if num % 2 != 0: sum_odd +=num
print("Sum odd item list: ", sum_odd)

sum_mult3 = 1

for i in range(len(lst)):
    if i % 3 == 0: sum_mult3 *= lst[i]
print("Sum mult item list: ", sum_mult3)

mult_range = 1
min_val_lst = min(lst)
max_val_lst = max(lst)
index_min = lst.index(min_val_lst)
index_max = lst.index(max_val_lst)
for value in range(index_min, index_max):
   if index_max < index_min: index_max, index_min =  index_min, index_max
for i in range(index_min,index_max,1):
    mult_range *= lst[i]
print("Multiply between minimum and maximum element: ", mult_range)
