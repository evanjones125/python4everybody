import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for i in kwargs.items():
            for j in range(i[-1]):
                self.contents.append(i[0])
    
    def draw(self, num):
        # if the draw number exceeds the length of contents, return all balls
        if num > len(self.contents): return self.contents

        # remove elements from contents list at random and place in output
        output = []
        for i in range(num):
            output.append(random.choice(self.contents))
            
            # iterate through contents and remove the first element that
            # has the same name as the last element of output
            for j in self.contents:
                if j == output[-1]:
                    self.contents.remove(j)
                    break

        return output
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # keep track of number of times expected_balls is reached
    count = 0

    # perform num_experiments draws on the input hat
    for i in range(num_experiments):
        # restore hat to original contents
        hat_copy = copy.deepcopy(hat)
        
        # make list with current draw
        current = hat_copy.draw(num_balls_drawn)

        # create shallow copy of expected_balls
        color_list = copy.copy(expected_balls)

        # create dict with values decremented from expected_balls
        for j in current:
            if j in color_list:
                if color_list[j] > 0: color_list[j] -= 1

        # if each key in color_list has no value, increment m
        if all(value == 0 for value in color_list.values()):
            count += 1

    # return the probability through num_experiments tests
    return count / num_experiments

# hat1 = Hat(yellow = 3, blue = 2, green = 6)
# hat2 = Hat(red = 5, orange = 4)
# hat3 = Hat(red = 5, orange = 4, black = 1, blue = 0, pink = 2, striped = 9)
# print(hat1.draw(5))

hat = Hat(black = 6, red = 4, green = 3)
probability = experiment(hat = hat,
    expected_balls = {"red": 2, "green": 1},
    num_balls_drawn = 5,
    num_experiments = 2000)
print(probability)