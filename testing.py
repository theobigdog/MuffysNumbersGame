import math
import statistics as st

x = [1,2,3,4,4,5,6,7]
med = st.median(x)
print(med)

print('5' == 5)

my_dict = {'1' : 1, '2' : 2, '3' : 3}

print(my_dict['1'])
new_dict = my_dict
new_dict[f'4'] = 4

print(new_dict)

next_dict = {}
for number in x:
    next_dict[f'{number}'] = x[number]

print(next_dict)