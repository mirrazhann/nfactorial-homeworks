"""
Exercise-1: Count unique elements
Write a function "count_unique_elements(my_list: list) -> int" that takes a 
list of integers and returns the number of unique elements in the list.

Example:
count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]) -> 5
"""

def count_unique_elements(my_list: list) -> int:
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    return len(unique_list)

# print(count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]), 5)
# print(count_unique_elements([]), 0)
# print(count_unique_elements([1, 1, 1, 1]), 1)
# print(count_unique_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
# print(count_unique_elements([1, 1, 2, 2, 3, 3, 4, 4]), 4)

"""
Exercise-2: Remove duplicates
Write a function "remove_duplicates(my_list: list) -> list" that takes a list of integers and 
removes all duplicates, returning the new list with unique elements in their original order.

Example:
remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]) -> [1, 2, 3, 4, 5]
"""

def remove_duplicates(my_list: list) -> list:
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

# print(remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]), [1, 2, 3, 4, 5])
# print(remove_duplicates([]), [])
# print(remove_duplicates([1, 1, 1, 1]), [1])
# print(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]), [1, 2, 3, 4])
    
"""
Exercise-3: Reverse a list
Write a function "reverse_list(my_list: list) -> list" that takes a list of integers and 
returns a new list with the elements in reverse order.

Example:
reverse_list([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def reverse_list(my_list: list) -> list:
    new_list = []
    i = 0
    end_list = len(my_list)-1
    while i <= end_list:
        new_list.append(my_list[end_list-i])
        i += 1
    return new_list

# print(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
# print(reverse_list([]), [])
# print(reverse_list([1]), [1])
# print(reverse_list([1, 2]), [2, 1])
# print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

"""
Exercise-4: Find the maximum value in a list
Write a function "max_value(my_list: list) -> int" that takes a 
list of integers and returns the maximum value in the list.

Example:
max_value([1, 2, 3, 4, 5]) -> 5
"""

def max_value(my_list: list) -> int:
    max_number = None
    for i, v in enumerate(my_list):
        if i == 0:
            max_number = v
        else:
            if max_number <= v:
                max_number = v
    return max_number

# print(max_value([1, 2, 3, 4, 5]), 5)
# print(max_value([1]), 1)
# print(max_value([-1, -2, -3, -4, -5]), -1)
# print(max_value([1, 1, 1, 1]), 1)
# print(max_value([10**6]*10), 10**6)
    

"""
Exercise-5: Find the minimum value in a list
Write a function "min_value(my_list: list) -> int" that takes a 
list of integers and returns the minimum value in the list.

Example:
min_value([1, 2, 3, 4, 5]) -> 1
"""

def min_value(my_list: list) -> int:
    min_number = None
    for i, v in enumerate(my_list):
        if i == 0:
           min_number = v
        else:
            if min_number >=v:
                min_number = v
    return min_number

# print(min_value([1, 2, 3, 4, 5]), 1)
# print(min_value([1]), 1)
# print(min_value([-1, -2, -3, -4, -5]), -5)


"""
Exercise-6: Sum all values in a list
Write a function "sum_values(my_list: list) -> int" that takes a 
list of integers and returns the sum of all values in the list.

Example:
sum_values([1, 2, 3, 4, 5]) -> 15
"""

def sum_values(my_list: list) -> int:
    s = 0
    for i, v in enumerate(my_list):
        s+=v
    return s

# print(sum_values([1, 2, 3, 4, 5]), 15)
# print(sum_values([1]), 1)
# print(sum_values([-1, -2, -3, -4, -5]), -15)
# print(sum_values([1, 1, 1, 1]), 4)
# print(sum_values([10**6]*10**6), 10**12)
    
"""
Exercise-7: Find the average of a list
Write a function "average(my_list: list) -> float" that takes a 
list of integers and returns the average value of the list.

Example:
average([1, 2, 3, 4, 5]) -> 3.0
"""

def average(my_list: list) -> float:
    len_list = len(my_list)
    s = 0
    for i, v in enumerate(my_list):
        s += v
    average = s/len_list
    return average

# print(average([1, 2, 3, 4, 5]), 3.0)
# print(average([1]), 1.0)
# print(average([-1, -2, -3, -4, -5]), -3.0)
# print(average([1, 1, 1, 1]), 1.0)
# print(average([10**6]*10**6), 10**6)

"""
Exercise-8: Find the index of an element in a list
Write a function "find_index(my_list: list, element: int) -> int" that takes a 
list of integers and an element, and returns the index of the first occurrence of 
the element in the list. If the element is not in the list, return -1.

Example:
find_index([1, 2, 3, 4, 5], 3) -> 2
find_index([1, 2, 3, 4, 5], 6) -> -1
"""

def find_index(my_list: list, element: int) -> int:
    for i, v in enumerate(my_list):
        if v == element:
            return i
    return -1

# print(find_index([1, 2, 3, 4, 5], 3), 2)
# print(find_index([1, 2, 3, 4, 5], 6), -1)
# print(find_index([], 1), -1)
# print(find_index([1, 1, 1, 1], 1), 0)
# print(find_index([1, 2, 3, 4, 5], 1), 0)

"""
Exercise-9: Check if a list is sorted
Write a function "is_sorted(my_list: list) -> bool" that takes a list
of integers and returns True if the list is sorted in non-descending 
order (i.e., each element is greater than or equal to the previous element), 
False otherwise.

Example:
is_sorted([1, 2, 3, 4, 5]) -> True
is_sorted([1, 3, 2, 4, 5]) -> False
"""

def is_sorted(my_list: list) -> bool:
    number = None
    for i, v in enumerate(my_list):
        if i == 0:
            number = v
        else:
            if v < my_list[i-1]:
                return False
    return True

# print(is_sorted([1, 2, 3, 4, 5]))
# print(is_sorted([1, 3, 2, 4, 5]))
# print(is_sorted([]))
# print(is_sorted([1]))
# print(is_sorted([-1, -1, 0, 1, 2]))


"""
Exercise-10: Count the frequency of an element in a list
Write a function "count_frequency(my_list: list, element: int) -> int" that 
takes a list of integers and an element, and returns the number of 
times the element appears in the list.

Example:
count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3) -> 2
"""

def count_frequency(my_list: list, element: int) -> int:
    e = 0
    for i, v in enumerate(my_list):
        if v == element:
            e += 1
    return e

# print(count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3), 2)
# print(count_frequency([1, 2, 3, 4, 5], 6), 0)
# print(count_frequency([], 1), 0)
# print(count_frequency([1, 1, 1, 1], 1), 4)
# print(count_frequency([1, 2, 3, 4, 5], 1), 1)

"""
Exercise-11: Find the mode of a list
Write a function "find_mode(my_list: list) -> int" that takes a list of 
integers and returns the mode (i.e., the value that appears most frequently) 
of the list. If there are multiple modes, return any of them.

Example:
find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]) -> 2
"""

def find_mode(my_list: list) -> int:
    if not my_list:
        return None  

    max_count = 0
    mode = my_list[0]

    for number in my_list:
        count = 0
        
        for item in my_list:
            if item == number:
                count += 1

        if count > max_count:
            max_count = count
            mode = number

    return mode

# print(find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]), 2)
# print(find_mode([1]), 1)
# print(find_mode([]), None)
# print(find_mode([1, 2, 3]), 1)
# print(find_mode([1, 1, 1, 2, 2]), 1)

"""
Exercise-12: Remove all occurrences of an element in a list
Write a function "remove_all(my_list: list, element: int) -> list" 
that takes a list of integers and an element, and returns a new list 
with all occurrences of the element removed.

Example:
remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3) -> [1, 2, 4, 5, 1, 2]
"""

def remove_all(my_list: list, element: int) -> list:
    new_list = []
    for i in my_list:
        if i != element:
            new_list.append(i)
    return new_list

# print(remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3), [1, 2, 4, 5, 1, 2])
# print(remove_all([], 1), [])
# print(remove_all([1, 1, 1, 1], 1), [])
# print(remove_all([1, 2, 3], 4), [1, 2, 3])

"""
Exercise-13: Rotate a list to the left by k positions
Write a function "rotate_left(my_list: list, k: int) -> list" that takes a 
list of integers and an integer k, and returns a new list with the elements rotated k positions to the left.

Example:
rotate_left([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
"""

def rotate_left(my_list: list, k: int) -> list:
    
    new_list = my_list[k:] + my_list[:k]
    return new_list

# print(rotate_left([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
# print(rotate_left([], 1), [])
# print(rotate_left([1], 1), [1])
# print(rotate_left([1, 2], 1), [2, 1])
# print(rotate_left([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
    
"""
Exercise-14: Rotate a list to the right by k positions
Write a function "rotate_right(my_list: list, k: int) -> list" that 
takes a list of integers and an integer k, and returns a new list 
with the elements rotated k positions to the right.

Example:
rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
"""

def rotate_right(my_list: list, k: int) -> list:
    new_list = my_list[-k:] + my_list[:-k]
    return new_list

# print(rotate_right([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
# print(rotate_right([], 1), [])
# print(rotate_right([1], 1), [1])
# print(rotate_right([1, 2], 1), [2, 1])
# print(rotate_right([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
    
"""
Exercise-15: Find the intersection of two lists
Write a function "find_intersection(list1: list, list2: list) -> list" that 
takes two lists of integers and returns a new list with the elements that are present in both lists.

Example:
find_intersection([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
"""

def find_intersection(list1: list, list2: list) -> list:
    new_list = []
    for i in list1:
        if i in list2:
            new_list.append(i)
    return new_list

# print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
# print(find_intersection([], []), [])
# print(find_intersection([1], [2]), [])
# print(find_intersection([1, 2, 3], [3, 4, 5]), [3])
# print(find_intersection([1, 1, 1, 1], [1, 1, 1, 1]), [1])
    
"""
Exercise-16: Find the union of two lists
Write a function "find_union(list1: list, list2: list) -> list" that takes 
two lists of integers and returns a new list with the elements that are 
present in either list (i.e., the union of the lists).

Example:
find_union([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2, 3, 4, 5, 6]
"""

def find_union(list1: list, list2: list) -> list:
    new_list = []

    for i in list1:
        if i in list1 and i not in new_list:
            new_list.append(i)
    for i in list2:
        if i in list2 and i not in new_list:
            new_list.append(i)
    return new_list

# print(find_union([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
# print(find_union([], []), [])
# print(find_union([1], [2]), [1, 2])
# print(find_union([1, 2, 3], [3, 4, 5]), [1, 2, 3, 4, 5])
# print(find_union([1, 1, 1, 1], [1, 1, 1, 1]), [1])
    
"""
Exercise-17: Find the difference of two lists
Write a function "find_difference(list1: list, list2: list) -> list" that takes 
two lists of integers and returns a new list with the elements that are 
present in the first list but not the second list.
Assume that list does not contain duplicates.

Example:
find_difference([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2]
"""

def find_difference(list1: list, list2: list) -> list:
    new_list = []
    for i in list1:
        if i not in list2:
            new_list.append(i)
    return new_list

# print(find_difference([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2])
# print(find_difference([], []), [])
# print(find_difference([1], [2]), [1])
# print(find_difference([1, 2, 3], [3, 4, 5]), [1, 2])


