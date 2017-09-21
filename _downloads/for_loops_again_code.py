""" For loops again
"""
#: Doing something N times
N = 4   # or whatever number you like
for i in range(N):
    # Do something
    print('i is set equal to', i)


#: Collecting the values in range(N)
#: Remember N == 4
list(range(N))

#: The exact equivalent of the loop above
i = 0
print('i is set equal to', i)
i = 1
print('i is set equal to', i)
i = 2
print('i is set equal to', i)
i = 3
print('i is set equal to', i)

#: we can use any list on the right hand side
my_list = [0, 9, 1, 8]
for i in my_list:
    print('i is set equal to', i)


#: Your list
the_list = [12, 4, 3, 1, 5]

#: the result you want
12 * 4 * 3 * 1 * 5

#- Make a for loop to calculate product of all elements in the_list
#- You are going to start off with something like:
#-
#- product = 1
#- for i in <something you put here>:
