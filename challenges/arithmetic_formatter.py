import re

def arithmetic_arranger(problems, display = False):
    # formatting checks:
    # check that input array is less than 6
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        # check that input array does not contain '*' or '/'
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."

        # check that input array does not contain non-digits
        if re.search('[^\s0-9.+-]', problem):
            return "Error: Numbers must only contain digits."

    # store line values
    line1, line2, line3, line4 = '', '', '', ''

    # find numbers and operation types in input array elements
    for problem in problems:
        first_num = problem.split(' ')[0]
        op_type = problem.split(' ')[1]
        second_num = problem.split(' ')[2]

        if int(first_num) > 9999 or int(second_num) > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        if op_type is '+':
            solution = int(first_num) + int(second_num)
        else:
            solution = int(first_num) - int(second_num)

        length = max(len(first_num), len(second_num)) + 2

        top = str(first_num).rjust(length)
        bottom = op_type + str(second_num).rjust(length - 1)

        if problem != problems[-1]:
            line1 += top + '    '
            line2 += bottom + '    '
            line3 += ('-' * length) + '    '
            line4 += str(solution).rjust(length) + '    '
        else:
            line1 += top
            line2 += bottom
            line3 += '-' * length
            line4 += str(solution).rjust(length)

    # add line breaks at the end of each line and return all the lines
    line1 += '\n'
    line2 += '\n'

    if display is True:
        line3 += '\n'
        output = line1 + line2 + line3 + line4
    if display is False:
        output = line1 + line2 + line3
    
    return output

# print(arithmetic_arranger(['3801 - 2', '123 + 49']))
# print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))