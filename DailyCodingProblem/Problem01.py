# Problem 1

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.



def check_addup(k, numbers):
    # build touple list of combinations, this is in 0(n²)
    combos = [(num, other_num) for i, num in enumerate(numbers) for other_num in numbers[i + 1:]]
    # check sums
    for i in combos:
        if sum(i) == k:
            addup = True
            break
        else:
            addup = False
    return addup

def check_addup_faster(k, numbers):
    # calculate the k - number list adn check if it is in numbers
    addup = False
    if k != []:
        set_diffs = set()
        for i in range(len(numbers)): # this is in O(n)
            diff = k - numbers[i]
            if numbers[i] in set_diffs: # and numbers.index(diff) != i: # this is in O(logn)
                addup = True
                break
            else:
               set_diffs.add(diff)
    return addup

# this is know in  O(nlogn)

# How can I do this in one pass? --> in O(n)

# What are potential corner cases?, lets test different inputs
k = 17
numbers = [ 10, 15, 3, 7 ]

k_1 = -20
k_2 = 0
k_3 = []

n_1 = [0, -3, 5, 10, 4, -17, 8,12]
n_2 = [0, 1, 0, 4, 7]
n_3 = [0, 5, -5]
n_4 = []

# start testing
test0 = check_addup_faster(k, numbers) 
print('test0 should be True--', test0)

test1 = check_addup_faster(k_1, n_1)
print('test1 should be True--', test1)

test2 = check_addup_faster(k_2, n_1)
print('test2 should be False--', test2)

test3 = check_addup_faster(k_2, n_2)
print('test3 should be True--', test3)

test4 = check_addup_faster(k_3, numbers)
print('test4 should be False--', test4)

test5 = check_addup_faster(k_3, n_3)
print('test5 should be False--', test5)

test6 = check_addup_faster(k, n_4)
print('test6 should be False--', test6)

test7 = check_addup_faster(k_2, n_3)
print('test7 should be True--', test7)
