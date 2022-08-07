import re

def haystack(file):
    handle = open(file)
    total = 0
    nums = []
    
    for line in handle:
        nums.append(re.findall('[0-9]+', line))

    flatten_list = [element for sublist in nums for element in sublist]

    for i in flatten_list:
        total += int(i)

    return total

print(haystack('regex_sum_42.txt'))