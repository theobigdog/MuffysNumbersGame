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
            break
    return best

def check_factors(number : int, numbers_tracker: list, factors : dict) -> int:
    best = 0
    for factor in factors[f'{number}']:
        curr = try_factor(factor, numbers_tracker, factors)
        if curr > best and curr in numbers_tracker:
            best = curr
    return best

def check_multiples(number : int, numbers_tracker : list, multiples : dict) -> int:
    best = 0
    for multiple in multiples[f'{number}']:
        curr = try_multiple(multiple, numbers_tracker, multiples)
        if curr > best and curr in numbers_tracker:
            best = curr
            break
    return best

def update_lists(number : int, numbers_tracker : list, series : list) -> list and list:
    ind = numbers_tracker.index(number)
    numbers_tracker.pop(ind)
    series.append(number)
    return numbers_tracker, series

def next(best : int, numbers_tracker : list, factors : dict, multiples : dict, primes : list, no_primes : list, series : list) -> list and list:
    numbers_tracker, series = update_lists(best, numbers_tracker, series)
    numbers_tracker, series = series_generation(best, numbers_tracker, factors, multiples, primes, no_primes, series)
    return numbers_tracker, series

def series_generation(number : int, numbers_tracker : list, factors : dict, multiples : dict, primes : list, no_primes : list, series : list) -> list and list:
    try:
        median = st.median(numbers_tracker)
    except:
        median = number
    if number > median:
        best = check_factors(number, numbers_tracker, factors)
        if best != 0:
            numbers_tracker, series = next(best, numbers_tracker, factors, multiples, primes, no_primes, series)
        elif best == 0:
            best = check_multiples(number, numbers_tracker, multiples)
            if best != 0:
                numbers_tracker, series = next(best, numbers_tracker, factors, multiples, primes, no_primes, series)
    else:
        best = check_multiples(number, numbers_tracker, multiples)
        if best != 0:
            numbers_tracker, series = next(best, numbers_tracker, factors, multiples, primes, no_primes, series)
        elif best == 0:
            best = check_factors(number, numbers_tracker, factors)
            if best != 0:
                numbers_tracker, series = next(best, numbers_tracker, factors, multiples, primes, no_primes, series)
    return numbers_tracker, series
    
def best_series(numbers : list, factors : dict, multiples : dict, primes : list, no_primes : list) -> list:
    all_tracker = {}    
    for number in numbers:
        numbers_tracker = numbers.copy()
        ind = numbers_tracker.index(number)
        numbers_tracker.pop(ind)
        series = [number]
        dummy_holder, best = series_generation(number, numbers_tracker, factors, multiples, primes, no_primes, series)
        all_tracker[f'{number}'] = best
    return all_tracker

numbers = list(np.arange(1, max_cutoff + 1))

no_primes, primes = remove_primes(numbers)

print(f'Starting Numbers: {numbers}')

factors = get_factors(numbers)
multiples = get_multiples(numbers)
print('Factors: ', factors)
print('Multiples: ', multiples)

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
