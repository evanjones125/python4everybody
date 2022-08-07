import re

def haystack(file):
    handle = open(file)
    total = 0
    nums = []
    
    # add all numbers to list nums
    for line in handle:
        nums.append(re.findall('[0-9]+', line))

    # flatten nums and iterate through to add int value of i to total
    flatten_list = [element for sublist in nums for element in sublist]
    for i in flatten_list:
        total += int(i)

    return total

print(haystack('regex_sum_1585134.txt'))