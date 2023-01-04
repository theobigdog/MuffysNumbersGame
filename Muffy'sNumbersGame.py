'''The goal of this script is to input an integer, 1 - 1200, and produce a list of factors and multiples of each integer from the list.
As each successive factor/multiple is calculated, this integer is removed from the original list, until there are no more factors
or multiples of the current number that fit the criteria of being in the current version of the original list.
The longest string of numbers wins!

For example, for 4, the best series is a tie for multiple iteration of this process.  Because of the way things are calculated, only 
the very first series that is tied for the "longest length" will be selected:

Number:  Best(Longest) String:  Length:
5           [2,4,1,3]               4
10          [4,8,2,6,3,9,1,5,10]    9
100         [many]                  77 (at 68 right now)

The current state of this code (12/30/22, 12:41pm) works perfectly up until about 30, when some longer series are somehow skipped, or
never even evaluated in the first place.  In the case of the initial goal of evaluating 100, and getting the number 77, I currently get
a series of 68 numbers, starting with 18.
'''

import statistics as st
import numpy as np
import random
import time

####  Manually set these if desired, but do not go lower than 1 for the low, nor above 1200 for the high
absolute_cutoff = 1200
high_cutoff = 101
low_cutoff = 1

'''
Recursive function designed to get the max cutoff as an input (with given limits of 1 min and 1200 max)  Accounts for shenanigans
@params
@counter: Counts how many times this function has cycled, enabling snarky responses
@max_cutoff: This is the high-end cutoff, with an absolute max (above)
'''
def get_max_cutoff(counter : int, max_cutoff : int) -> int:
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

'''
Establishes all prime numbers, 1 - 1200; the list of numbers, 1 - max_cutoff,
is used to split the number list into two returned lists of primes and non-primes, for later work
@params
@current_list: list of all integers from 1 to max_cutoff, inclusive
'''
def remove_primes(current_list : list) -> list and list:
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
        1153, 1163, 1171, 1181, 1187, 1193]  #### Just going through 1200.  Gets the point across!

    primes = []
    no_primes = []
    for x in current_list:
        if x in full_prime_nums:
            primes.append(x)
        else:
            no_primes.append(x)
    return no_primes, primes

'''
Takes all integers from the numbers list and calculates all factors for each number, returning them in a dictionary
@params
@numbers: the list of numbers being evaluated, from 1 - max_cutoff
'''
def get_factors(numbers : list) -> dict:
    factors = {}
    for number in numbers:
        factors[f'{number}'] = []
        for factor in range(1,number + 1):
            if number % factor == 0:
                factors[f'{number}'].append(factor)
    return factors

'''
Calculates all multiples of all numbers from the list of 1 - max_cutoff,
with only multiples <= max_cutoff being included
@params
@numbers: the list of numbers being evaluated, from 1 - max_cutoff
'''
def get_multiples(numbers : list) -> dict:
    multiples = {}
    for number in numbers:
        multiples[f'{number}'] = []
        for multiple in range(1,len(numbers) + 1):
            if number * multiple <= len(numbers):
                multiples[f'{number}'].append(number * multiple)
    return multiples

'''
Takes a given number, then from factors, searches for all factors of the number,
comparing them to A) the numbers_tracker, to see if they should even be evaluated,
and B) saving the factor as the "best" value; being in a loop, the function returns
the HIGHEST FACTOR from the list given, that is also in the numbers_tracker
@params
@number: current integer being evaluated
@numbers_tracker: tracks all numbers, and determines if the current factor should be skipped or evaluated
@factors: dictionary of all factors, for all numbers in the original, given list
'''
def try_factor(number : int, numbers_tracker : list, factors : dict) -> int:
    best = 0
    for factor in factors[f'{number}']:
        if factor in numbers_tracker:
            best = factor
    return best

'''
Similarly to the above, takes the given number, uses the multiples dictionary to
determine all potential multiples, then compares each multiple to the provided
numbers_tracker to determine if the number should even be evaluated, with the very
acceptable multiple being returned - the "break" makes it so that the LOWEST MULTIPLE
will be the returned value
@params
@number: the current number being evaluated
@numbers_tracker: the list of integers that are still available
@multiples: dictionary of all acceptable multiples for all numbers in the initial list
'''
def try_multiple(number : int, numbers_tracker : list, multiples : dict) -> int:
    best = 0
    for multiple in multiples[f'{number}']:
        if multiple in numbers_tracker:
            best = multiple
            break
    return best

'''
Establishes the best factor for the current number being evaluated, returning that value - since
the loop begins with the best factor as 0, any factor that fits the bill will be chosen, and due
to the loop, it will always be the HIGHEST FACTOR that is returned as best
@params
@number: the current number being evaluated
@numbers_tracker: the list tracking numbers that are still available
@factors: the dictionary of all numbers from the orginal list, as well as all factors of those numbers
'''
def check_factors(number : int, numbers_tracker: list, factors : dict) -> int:
    best = 0
    for factor in factors[f'{number}']:
        curr = try_factor(factor, numbers_tracker, factors)
        if curr > best and curr in numbers_tracker:
            best = curr
    return best

'''
Establishes the best multiple for the given number, relative to the numbers_tracker - any
multiple that fits the bill will immediately be selected, and due to the break in the loop,
once a multiple is chosen, it is always the LOWEST MULTIPLE that is returned
@params
@number: the current number being evaluated
@numbers_tracker: list to track the available numbers
@multiples: dictionary of all values from the initial list, as well as all multiples that are below max_cutoff
'''
def check_multiples(number : int, numbers_tracker : list, multiples : dict) -> int:
    best = 0
    for multiple in multiples[f'{number}']:
        curr = try_multiple(multiple, numbers_tracker, multiples)
        if curr > best and curr in numbers_tracker:
            best = curr
            break
    return best

'''
Once the next official number is selected, this function will remove that value from
the numbers_tracker, and add it to the series, which represents the final result, once finished
@params
@number: the current value being evaluated
@numbers_tracker: the list of all available numbers
@series: the final list of factors/multiples for each number
'''
def update_lists(number : int, numbers_tracker : list, series : list) -> list and list:
    ind = numbers_tracker.index(number)
    numbers_tracker.pop(ind)
    series.append(number)
    return numbers_tracker, series

'''
Takes the provided best factor/multiple, sending associated lists/dicts to appropriate
functions to A) update the lists to what they will now contain, then B) the lists are recursively
returned to the series_generation function to look for the next factor/multiple, if one is available
@params
@best: the next factor/multiple chosen for the list of values for each number in the original list
@numbers_tracker: tracks which numbers are still available
@factors: contains all factors for all integers in the original list
@multiples: contains all multiples for all integers in the original list, with maxes being the max_cutoff
@primes: contains all prime numbers from the original list
@no_primes: contains all non-prime numbers from the original list
@series: the final list of values associated with each number from the original list
'''
def next(best : int, numbers_tracker : list, factors : dict, multiples : dict, primes : list, no_primes : list, series : list) -> list and list:
    numbers_tracker, series = update_lists(best, numbers_tracker, series)
    numbers_tracker, series = series_generation(best, numbers_tracker, factors, multiples, primes, no_primes, series)
    return numbers_tracker, series

'''
Recursive function to determine the "best" series of numbers for each of the values in the
original list, returning this list as series
@params
@number: the current number being evaluated
@numbers_tracker: list to track the currently-available numbers from the original list
@factors: dictionary of all the factors of every number from the original list
@multiples: dictionary of all the multiples of every number from the original list, with max_cutoff being the highest multiple allowed
@primes: list of all the prime numbers from the original list
@no-primes: list of all the non-prime numbers from the original list
@series: list of the current "best" series for the current number being evaluated
'''
def series_generation(number : int, numbers_tracker : list, factors : dict, multiples : dict, primes : list, no_primes : list, series : list) -> list and list:
    try:
        median = st.median(numbers_tracker)
        print(f'{number} peep')
    except:
        median = number
        print('growl')
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

'''
Cycles through each number from the original list, sending them to the appropriate functions to
determine the best series of numbers for each one.  This list of dictionaries is returned
@params
@numbers: the original list of numbers
@factors: the dictionary of factors for all numbers from the original list
@multiples: the dictionary of all multiples for all numbers from the original list which are lower than max_cutoff
@primes: list of all prime numbers from the original list of numbers
@no_primes: list of all non-prime numbers from the original list of numbers
'''    
def best_series(numbers : list, factors : dict, multiples : dict, primes : list, no_primes : list) -> dict:
    all_tracker = {}    
    for number in numbers:
        numbers_tracker = numbers.copy()
        ind = numbers_tracker.index(number)
        numbers_tracker.pop(ind)
        series = [number]
        dummy_holder, best = series_generation(number, numbers_tracker, factors, multiples, primes, no_primes, series)
        all_tracker[f'{number}'] = best
    return all_tracker

max_cutoff = get_max_cutoff(0,input(f"What is the upper limit you'd like to see?  "))
print(f'Max Cutoff:  {max_cutoff}')

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
