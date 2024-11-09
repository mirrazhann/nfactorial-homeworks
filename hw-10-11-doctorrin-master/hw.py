import time
from datetime import datetime
from functools import reduce

"""
Exercise-1: First-class Function Operation
Write a function "operation(func, x: int, y: int) -> int" that takes in a function 'func' and two integers, 'x' and 'y'. Apply the function to the two numbers and return the result. 

Example:
def multiply(a, b):
    return a * b
operation(multiply, 5, 3) -> 15
"""

def operation(func, x: int, y: int) -> int:
    z = func(x,y)
    return z

def add(x: int, y: int):
    return x+y


# print(operation(add, 2, 3), 5)
# print(operation(add, -1, 1), 0)
# print(operation(add, 0, 0), 0)

"""
Exercise-2: Implement Map Function
Write a function "my_map(func, my_list: list) -> list" that mimics the built-in Python 'map' function. It should take a function and a list as input, applying the function to each element of the list.

Example:
my_map(lambda x: x**2, [1, 2, 3, 4]) -> [1, 4, 9, 16]
"""

def my_map(func, my_list: list) -> list:
    new_list = []
    for i in my_list:
        new_list.append(func(i))
    return new_list


# print(my_map(lambda x: x**3, [1, 2, 3, 4]), [1, 8, 27, 64])
# print(my_map(lambda x: x+2, [1, 2, 3, 4]), [3, 4, 5, 6])

"""
Exercise-3: Lambda Function with Filter
Write a function "filter_even_numbers(numbers: list) -> list" that uses 'filter' and a lambda function to filter out all even numbers from the list.

Example:
filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]) -> [1, 3, 5, 7]
"""

def filter_even_numbers(numbers: list) -> list:
    new_list = list(filter(lambda x: x%2!=0, numbers))
    return new_list

# print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])
# print(filter_even_numbers([11, 12, 13, 14, 15]), [11, 13, 15])


"""
Exercise-4: Recursive Factorial
Write a function "recursive_factorial(n: int) -> int" that calculates the factorial of a number recursively.

Example:
recursive_factorial(5) -> 120
"""

def recursive_factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return  n*recursive_factorial(n-1)
    
        


# print(recursive_factorial(3), 6)
# print(recursive_factorial(4), 24)
# print(recursive_factorial(1), 1)


"""
Exercise-5: Decorator for Timing
Write a decorator function "timeit_decorator(func)" that prints the time taken by the function to execute.

Example:
@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]
"""

def timeit_decorator(func): #func
    time_start= datetime.now()
    print(f'func start: {time_start}')
    func()
    time_end = datetime.now()
    print(F'func end: {time_end}')
    time_diff = time_end - time_start
    print(f'execute time: {time_diff}')

@timeit_decorator
def sample_func():
    return [i**2 for i in range(10**6)]


"""
Exercise-6: Function Composition
Write a function "compose(*funcs)" that takes a series of functions and returns a new function that composes them. The returned function should take an input and apply each function to the result of the previous function.

Example:
def double(x):
    return 2 * x
def square(x):
    return x ** 2
new_func = compose(double, square)
new_func(3) -> 36
"""

def compose(*funcs):
    def total_func(x):
        for func in funcs:
            x = func(x)
        return x
    return total_func

# def plus_one(x):
#     return x + 1

# def double(x):
#     return x * 2

# def square(x):
#     return x ** 2

# new_func = compose(plus_one, double, square)
# print(new_func(3), 8)
# print(new_func(0), 2)


"""
Exercise-7: Partial Application
Write a function "partial(func, *args)" that implements partial application. The function should return a new function that when called will return the result of applying the input function to the provided arguments, followed by the new arguments.

Example:
def add_three_numbers(a, b, c):
    return a + b + c
add_five_and_six = partial(add_three_numbers, 5, 6)
add_five_and_six(7) -> 18
"""

def partial(func, *args):
    def new_func(x):
        return func(x, *args)
    return new_func

# def multiply_three_numbers(a, b, c):
#     return a * b * c

# def add_three_numbers(a, b, c):
#     return a + b + c

# add_five_and_six = partial(add_three_numbers, 5, 6)
# print(add_five_and_six(7), 18)

# multiply_by_two_and_three = partial(multiply_three_numbers, 2, 3)
# print(multiply_by_two_and_three(4), 24)
# print(multiply_by_two_and_three(1), 6)
# print(multiply_by_two_and_three(15), 90)
    
"""
Exercise-8: Reduce to Compute Factorial
Write a function "factorial_reduce(n: int) -> int" that uses `reduce` to compute the factorial of an integer.

Example:
factorial_reduce(5) -> 120
"""

def factorial_reduce(n: int) -> int:   
    if n == 0: return 1
    return reduce(lambda x, y: y*x, reversed(range(1, n+1)))


# print(factorial_reduce(3), 6)
# print(factorial_reduce(4), 24)
# print(factorial_reduce(1), 1)



"""
Exercise-9: Function Memoization
Write a function "memoize(func)" that takes a function and returns a memoized version of the function. The memoized version should cache the results of the function so that the next time it's called with the same arguments, it returns the cached value instead of calculating the result again.

Example:
def expensive_function(x):
    return x ** x  # expensive calculation
memoized_function = memoize(expensive_function)
memoized_function(5)  # -> This will take some time to compute
memoized_function(5)  # -> This will return the cached result
"""

def memoize(func):
    my_cache = {}    
    
    def check_cache(*arg):
        if arg in my_cache:
            # print('my_cache')
            return my_cache[arg]
            
        else:
            my_cache[arg] = func(*arg)
            # print(my_cache[arg])
            # print('function')
            return my_cache[arg]
        
    return check_cache
    
def expensive_function(num: int):
        return num ** num

# memoized_function = memoize(expensive_function)
# print(memoized_function(5))  # -> This will take some time to compute
# print(memoized_function(5))  # -> This will return the cached result
# print(memoized_function(8))  # -> This will return the cached result
# print(memoized_function(5))  # -> This will return the cached result
# print(memoized_function(8))  # -> This will return the cached result
# print(memoized_function(2))  # -> This will return the cached result

"""
Exercise-10: Custom Reduce Function
Implement your own version of Python's 'reduce' function "my_reduce(func, iterable, initializer=None)".

Example:
my_reduce(lambda x, y: x*y, [1, 2, 3, 4]) -> 24
"""

def my_reduce(func, iterable, initializer=None):
    if len(iterable) <= 0:
        return 0
    if initializer != None and initializer >= len(iterable):
        return 0
    if initializer != None:
        x = iterable[initializer]
        initializer += 1
    else:
        x = iterable[0]
        initializer = 1
    for i in iterable[initializer:]:
        x = func(x,i)
    return x

# reduce(lambda x, y: y*x, reversed(range(1, n+1)))


# print(my_reduce(lambda x, y: x+y, [1, 2, 3, 4]), 10)
# print(my_reduce(lambda x, y: x*y, [1, 2, 3, 4]), 24)

"""
Exercise-11: Lambda Function Sort
Write a function "sort_by_last_letter(words: list) -> list" that sorts a list of words in ascending order based on the last letter of each word. Use a lambda function.

Example:
sort_by_last_letter(['apple', 'banana', 'cherry', 'date']) -> ['banana', 'apple', 'date', 'cherry']
"""

def sort_by_last_letter(words: list) -> list:
    return sorted(words, key=lambda word: word[-1])


# print(sort_by_last_letter(['apple', 'banana', 'cherry', 'date', 'grape']), ['banana', 'apple', 'date', 'grape', 'cherry'])
        

"""
Exercise-12: Recursive List Reversal
Write a function "recursive_reverse(my_list: list) -> list" that reverses a list using recursion.

Example:
recursive_reverse([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def recursive_reverse(my_list: list) -> list:
    last_el = len(my_list)
    if not my_list:
        return my_list
    else:
        return  [my_list[last_el-1]] + recursive_reverse(my_list[0:last_el-1])
    
# print(recursive_reverse([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])
# print(recursive_reverse(['a', 'b', 'c']), ['c', 'b', 'a'])
# print(recursive_reverse([]), [])
# print(recursive_reverse(['222']), ['222'])
    

"""
Exercise-13: Decorator for Function Counting
Write a decorator function "count_calls(func)" that counts the number of times a function is called.

Example:
@count_calls
def test_function():
    return

test_function()
test_function()
# Output: 'test_function' was called 2 times.
"""

def count_calls(func):
    count = 0
    def wraper(*args, **kwargs):
        nonlocal count
        count+=1
        print(f"'{func.__name__}' was called {count} times")
        return func(*args, **kwargs)

    return wraper

@count_calls
def test_function():
    return


test_function()
test_function()
test_function()
test_function()



"""
Exercise-14: Use reduce to Find the Maximum Number
Write a function "find_max(numbers: list) -> int" that uses reduce to find the maximum number in a list.

Example:
find_max([1, 2, 3, 4, 5]) -> 5
"""

def find_max(numbers: list) -> int:
    return reduce(lambda x, y: x if x > y else y, numbers)


# print(find_max([1, 2, 3, 4, 5]), 5)
# print(find_max([-1, -2, -3, -4, -5]), -1)
# print(find_max([1]), 1)
    

"""
Exercise-15: Use filter and lambda to Remove Elements
Write a function "remove_elements(my_list: list, element) -> list" that uses filter and a lambda function to remove all instances of a specific element from a list.

Example:
remove_elements([1, 2, 3, 2, 4, 2, 5], 2) -> [1, 3, 4, 5]
"""

def remove_elements(my_list: list, element):
    return list(filter(lambda x: x != element, my_list))

# print(remove_elements([1, 2, 3, 2, 4, 2, 5], 2), [1, 3, 4, 5])
# print(remove_elements([1, 1, 1, 1, 1], 1), [])
# print(remove_elements([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])
    
"""
Exercise-16: Higher-Order Function for Repeats
Write a function "repeat(n: int)" that returns a function. The returned function should take a string input and repeat it `n` times.

Example:
repeat_three_times = repeat(3)
repeat_three_times('hello') -> 'hellohellohello'
"""

def repeat(n: int):
    def repeat_three_times(word):
        return word * n
    return repeat_three_times


    
# repeat_three_times = repeat(3)    
# print(repeat_three_times('hello'), 'hellohellohello')
# print(repeat_three_times(''), '')
# print(repeat_three_times('123'), '123123123')
    
"""
Exercise-17: Recursive List Sum
Write a function "recursive_sum(my_list: list) -> int" that recursively computes the sum of a list of integers.

Example:
recursive_sum([1, 2, 3, 4, 5]) -> 15
"""

def recursive_sum(my_list: list) -> int:
    last_el = len(my_list)
    if not my_list:
        return 0
    else:
        return my_list[last_el-1] + recursive_sum(my_list[0:last_el-1])


# print(recursive_sum([1, 2, 3, 4, 5]), 15)
# print(recursive_sum([-1, -2, -3, -4, -5]), -15)
# print(recursive_sum([1]), 1)
    

"""
Exercise-18: Map with Multiple Lists
Write a function "add_two_lists(list1: list, list2: list) -> list" that uses `map` and `lambda` to add together corresponding elements of two lists.

Example:
add_two_lists([1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
"""

def add_two_lists(list1: list, list2: list) -> list:
    return list(map(lambda x, y: x + y, list1, list2))

# print(add_two_lists([1, 2, 3], [4, 5, 6]), [5, 7, 9])
# print(add_two_lists([0, 0, 0], [4, 5, 6]), [4, 5, 6])
# print(add_two_lists([1, 2, 3], [1, 2, 3]), [2, 4, 6])