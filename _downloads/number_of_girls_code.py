""" Three girls in a family of four
"""
#: We need the random module
import random

#: A function for a single coin toss
def coin_toss():
    random_no = random.random()
    if random_no < 0.5:
        our_result = 0
    else:
        our_result = 1
    return our_result


#- Test the coin toss a few times

#- Make a list, and collect four coin tosses

#- Sum the list to give the number of girls in this family

#- Make a family from coin tosses, using a while loop.

#- Make a list to store the number of girls in each family
#- Use a while loop to make 1000 families.
#- For each family, calculate the number of girls
#- Store in the list
#- Count the number of families with 3 girls

#- divide the number of familes with 3 girls by the number of families
