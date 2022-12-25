import math
import numpy as np
import pandas as pd
import random

max_number = 101

numbers = list(np.arange(1, max_number, 1))
garbage = []

'''starting_number = random.randint(0,max_number - 1)
print(numbers[starting_number], starting_number)#, numbers)
test = []
for i in range(2000):
    test.append(random.randint(0,max_number - 1))
print(max(test), min(test), len(test), len(set(test)))'''

numbers_copy = numbers.copy()
spent_numbers = []
count = 0
finished = False
while count < len(numbers) and finished == False:# and count < 20:
    starting_index = random.randint(0, len(numbers_copy) - 1)
    starting_value = numbers_copy[starting_index] ############ Maybe this line moves above the while loop block and an "active" value or something replaces it here?
    spent_numbers.append(numbers_copy.pop(starting_index))
    count += 1
    #finished = True

print(count, spent_numbers, numbers_copy, len(numbers_copy), numbers_copy.includes(89))