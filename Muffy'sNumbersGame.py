import math
import statistics as st
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
            max_cutoff = get_max_cutoff(counter, input(f'That is below the lower threshhold.  Enter an integer from {low_cutoff} to {absolute_cutoff}:  '))
            return max_cutoff
        elif max_cutoff > absolute_cutoff:
            counter += 1
            max_cutoff = get_max_cutoff(counter, input(f'That is above the upper threshhold.  Enter an integer from {low_cutoff} to {absolute_cutoff}:  '))
            return max_cutoff
    except:
        counter += 1
        max_cutoff = get_max_cutoff(counter, input(f"That isn't even an integer.  Enter an integer from {low_cutoff} to {absolute_cutoff}:  "))
        return max_cutoff
    return max_cutoff

max_cutoff = get_max_cutoff(0,input(f"What is the upper limit you'd like to see?  "))

print(f'Max Cutoff:  {max_cutoff}')

def remove_primes(current_list : list) -> list:
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

    primes = []
    no_primes = []
    for x in current_list:
        if x in full_prime_nums:
            primes.append(x)
        else:
            no_primes.append(x)
    return no_primes, primes
'''
def top_half_bigger(the_list : list) -> bool:
    return st.median(the_list) > st.median(numbers)

def add_remove_next(starting : list, no_primes : list, primes : list) -> list:
    curr = starting[-1]
    finished = False
    counter = 1
    finishing = starting
    while counter <= len(starting) and finished == False:
        contender = starting[-counter]
        print(f'contender: {contender}, curr: {curr}')
        if curr != contender and curr % contender == 0 and not top_half_bigger(starting) and contender not in primes:
            print('yep')
            finishing.pop(-counter)
            finished = True
        counter += 1
    return finishing
'''

def get_factors(numbers : list) -> dict:
    factors = {}
    for number in numbers:
        factors[f'{number}'] = []
        for factor in range(1,number + 1):
            if number % factor == 0:
                factors[f'{number}'].append(factor)
    return factors

def get_multiples(numbers : list) -> dict:
    multiples = {}
    for number in numbers:
        multiples[f'{number}'] = []
        for multiple in range(1,len(numbers) + 1):
            if number * multiple <= len(numbers):
                multiples[f'{number}'].append(number * multiple)
    return multiples

def try_factor(number : int, numbers_tracker : list, factors : dict):
    best = 0
    for factor in factors[f'{number}']:
        if factor in numbers_tracker:
            best = factor
    return best

def try_multiple(number : int, numbers_tracker : list, multiples : dict):
    best = 0
    for multiple in multiples[f'{number}']:
        if multiple in numbers_tracker:
            best = multiple
    return best

def recursive_check(number : int, numbers_tracker : list, factors : dict, multiples : dict, primes : list, no_primes : list, series : list) -> dict and list:
    #median = st.median(numbers_tracker)
    #number_done = False
    best = 0
    for factor in factors[f'{number}']:
        curr = try_factor(factor, numbers_tracker, factors)
        print('factor', factor, 'curr', curr, 'num_tracker', numbers_tracker)
        if curr > best and curr in numbers_tracker:
            best = curr
    if best != 0:
        ind = numbers_tracker.index(best)
        numbers_tracker.pop(ind)
        #del(numbers_tracker[ind])
        series.append(best)
        print('factor del', 'best', best, 'series', series, 'num_tracker', numbers_tracker)
        recursive_check(best, numbers_tracker, factors, multiples, primes, no_primes, series)
    elif best == 0:
        for multiple in multiples[f'{number}']:
            curr = try_multiple(multiple, numbers_tracker, multiples)
            print('multiple', multiple, 'curr', curr, 'num_tracker', numbers_tracker)
            if curr > best and curr in numbers_tracker:
                best = curr
        if best != 0:
            ind = numbers_tracker.index(best)
            numbers_tracker.pop(ind)
            #del(numbers_tracker[ind])
            series.append(best)
            print('multiple del', 'best', best, 'series', series, 'num_tracker', numbers_tracker)
            recursive_check(best, numbers_tracker, factors, multiples, primes, no_primes, series)
    return numbers_tracker, series

def best_series(numbers : list, factors : dict, multiples : dict, primes : list, no_primes : list) -> list:
    #finished = False
    #counter = 0
    all_tracker = {}
    #current_best = []

    '''while counter <= len(numbers) and not finished:
        current = []
        number_best = []
        counter += 1'''
    
    '''series = {'9' : [1,9,3,6,2,8,4], }'''
    
    for number in numbers:
        numbers_tracker = numbers.copy()
        series = []
        tracker, best = recursive_check(number, numbers_tracker, factors, multiples, primes, no_primes, series)
        all_tracker[f'{number}'] = best
        print('Done with', number)
    return all_tracker

numbers = list(np.arange(1, max_cutoff + 1))

no_primes, primes = remove_primes(numbers)

print(f'Starting Numbers: {numbers}')
#print(f'No Primes: {no_primes} {len(no_primes)}')
#print(f'Primes: {primes} {len(primes)}')

'''
final = []
next_list = numbers.copy()
for track in range(max_cutoff):
    length_before = len(next_list)
    next_list = add_remove_next(next_list, no_primes, primes)
    length_after = len(next_list)
    if length_before == length_after:
        break
    
print(next_list)
'''
factors = get_factors(numbers)
multiples = get_multiples(numbers)
print('Factors: ', factors)
print('Multiples: ', multiples)

#number = random.randint(1,len(numbers))
summary = best_series(numbers, factors, multiples, primes, no_primes)
best_num = 0
best_series = []
length = len(best_series)
for number in summary:
    if len(summary[f'{number}']) > length:
        best_num = number
        best_series = summary[f'{number}']
        length = len(best_series)
print('Summary: ', summary)
print('Best Series:', best_num, ':', best_series, 'Length: ', length)

##################  Check for prime numbers, and account for them in the code 

##################  Also, make a "Set" out of the final array, convert back to array and make sure the length of the array is consistent
