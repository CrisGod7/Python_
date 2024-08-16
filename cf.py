from functools import reduce

l = [i for i in range(1, 11)]
"""
map(function, iterable, iterable2, ...)
function: The function to apply to each item.
iterable: One or more iterables to apply the function to.
"""
squares = list(map(lambda x: x ** 2, l))
print(squares)
"""
Filter function
apply function to every single value
inside of list/iterable object.
"""
my_numbers_filter = list(filter(lambda x: x % 2 == 0, squares))
print(my_numbers_filter)

"""
fibonacci  with lambda function
"""
example_list = [i for i in range(1, 7)]
print(example_list)

fibonacci = reduce(lambda x, y: x * y, example_list)
print(fibonacci)