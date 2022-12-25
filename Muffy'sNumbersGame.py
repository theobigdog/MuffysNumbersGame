import math
import numpy as np
import pandas as pd
import random
import time

####  Manually set these if desired, but do not go lower than 1 for the low, nor above 1200 for the high
absolute_cutoff = 1200
high_cutoff = 101
low_cutoff = 1

def get_max_cutoff(counter : int, max_cutoff : int) -> int:  # Recursive function to get the max cutoff.  Accounts for shenanigans.
    if counter > 2:
        print('No.  You know what?  Nevermind.  One too many times.  You have lost choosing privileges.')
        time.sleep(2)
        print('...')
        time.sleep(3)
        max_cutoff = random.randint(1,high_cutoff)
        print(f'There, your choice is {max_cutoff}.  Enjoy!')
        time.sleep(1)
        return max_cutoff
    elif counter < 0:
        print('Uh, you actually coded this in?  What a waste of ti..... nevermind.  You probably need to fix your code.  Cya.')
        time.sleep(2)
        exit()
    try:
        max_cutoff = int(max_cutoff)
        if max_cutoff < low_cutoff:
            counter += 1
            max_cutoff = get_max_cutoff(counter, input(f'That is below the lower limit.  Enter an integer from {low_cutoff} to {absolute_cutoff}:  '))
            return max_cutoff
        elif max_cutoff > absolute_cutoff:
            counter += 1
            max_cutoff = get_max_cutoff(counter, input(f'That is above the upper limit.  Enter an integer from {low_cutoff} to {absolute_cutoff}:  '))
            return max_cutoff
    except:
        counter += 1
        max_cutoff = get_max_cutoff(counter, input(f"That isn't even an integer.  Enter an integer from {low_cutoff} to {absolute_cutoff}:  "))
        return max_cutoff
    return max_cutoff

max_cutoff = get_max_cutoff(0,input(f"What is the upper limit you'd like to see?  "))
#max_cutoff = 10
print(max_cutoff)

'''
full_prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, #### Just going through 1200.  Gets the point across!
31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 
353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 
419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 
547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 
607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 
661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 
739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 
811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 
877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 
947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 
1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 
1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 
1153, 1163, 1171, 1181, 1187, 1193] #, 1201, 1213, 1217, 1223     #### Just going through 1200.  Gets the point across!

prime_nums = [x for x in full_prime_nums if x < max_cutoff]
primes_cutoff_length = len(prime_nums)

numbers = list(np.arange(1, prime_nums + 1, 1))
print(numbers)

initial_list = numbers.copy()
spent_numbers = []

count = 0
current_index = -1 #len(initial_list) - 1
print(current_index)
current_value = initial_list[current_index]
current_comparison = 0

finished = False
cant_go_up = False
cant_go_down = False
temp = 'holder'
while count < len(numbers) and finished == False:
    print(f'pre-temp = {temp}')
    temp = initial_list.pop(current_index)
    print(f'Post-temp = {temp}')
    for i in range(len(initial_list)):
        print('1st for')
        if initial_list[-i - 1] < current_value:
            print(f'i = {-i}')
            for j in range(len(initial_list)):
                print('second for')
                current_comparison = initial_list[-j - 1]
                current_value = j
                print(current_comparison, initial_list, spent_numbers, current_value)
                spent_numbers.append(temp)
                if current_value % current_comparison == 0:
                    print(f'j = {-j}')
                    current_value = current_comparison
                    current_index = len(initial_list) - j - 1  # not sure about this "- 1"
                    break
                else:
                    print('pre current_value')
                    current_comparison = initial_list[current_index - 1]
                    print(current_comparison)
        elif initial_list[-i - 1] > current_value:
            for k in range(len(initial_list)):
                print('3rd for')
                current_comparison = initial_list[-k-1]
                spent_numbers.append(temp)
                if current_comparison % current_value == 0:
                    print(f'k = {-k}')
                    current_value = current_comparison
                    current_index = len(initial_list) - k - 1
                    break
        elif initial_list[-i - 1] == current_value:
            current_comparison = current_value #initial_list[current_index - 1]
            current_index = int([x for x in initial_list if x == 6][0])
            print('equality', current_comparison, current_value, current_index)
            spent_numbers.append(temp)
        else:
            finished = True
            print('finished')
            break
    count += 1

# Final Summary

print(count, spent_numbers, initial_list, len(initial_list)) ###, max_number in initial_list, max_number in spent_numbers) # This was for ealy testing to make sure the top number wasn't in the final array.  The cutoff will actually be one integer lower.  Saving just in case

'''
##################  Check for prime numbers, and account for them in the code 

##################  Also, make a "Set" out of the final array, convert back to array and make sure the lenth of the array is consistent
