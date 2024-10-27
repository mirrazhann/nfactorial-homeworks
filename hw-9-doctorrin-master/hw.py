"""
Exercise-1: Find missing elements
Write a function "missing_elements(my_list: list) -> list" that takes a
sorted list of integers and returns a list of missing integers in the range of the list.

Example:
missing_elements([1, 2, 4, 6, 7]) -> [3, 5]
"""

def missing_elements(my_list: list) -> list:
    if len(my_list) == 0: return []
    new_list = []
    
    for i, v in enumerate(my_list):
        if i < len(my_list)-1 and my_list[i+1] - v != 1:
            print(v, my_list[i+1])
            new_list.append(v+1)

    return new_list


# print(missing_elements([1, 2, 4, 6, 7]), [3, 5])
# print(missing_elements([]), [])
# print(missing_elements([1, 2, 3]), [])
# print(missing_elements([1] + [2, 3] + [10**6]), list(range(4, 10**6)))
# print(missing_elements(list(range(1, 10**6+2))), [])
"""
Exercise-2: Count occurrences
Write a function "count_occurrences(my_list: list) -> dict" that takes a
list of integers and returns a dictionary where keys are unique integers
from the list and values are their counts in the list.

Example:
count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]) -> {1: 2, 2: 2, 3: 1, 4: 2, 5: 1}
"""

def count_occurrences(my_list: list) -> dict:
    co = {}
    for i in my_list:
        if i not in co.keys():
            co[i] = 1
        else:
            co[i] +=1
    return co

# print(count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]), {1: 2, 2: 2, 3: 1, 4: 2, 5: 1})
# print(count_occurrences([]), {})
# print(count_occurrences([1]*10**6 + [2]*10**6), {1: 10**6, 2: 10**6})
# print(count_occurrences([1, 1, 2, 2, 3, 3]), {1: 2, 2: 2, 3: 2})
# print(count_occurrences([1]), {1: 1})
"""
Exercise-3: Common elements
Write a function "common_elements(list1: list, list2: list) -> list" that takes two
lists of integers and returns a list of unique common elements.

Example:
common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""

def common_elements(list1: list, list2: list) -> list:
    list3 = []
    for i in list1:
        if i in list2 and i not in list3:
            list3.append(i)
    return list3


# print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])
# print(common_elements([1, 2, 3], [4, 5, 6]), [])
# print(common_elements([], [1, 2, 3]), [])
# # print(common_elements(list(range(1, 10**6+1)), list(range(500000, 10**6+2))), list(range(500000, 10**6+1)))
# print(common_elements([1, 2, 3], [1, 2, 3]), [1, 2, 3])
    

"""
Exercise-4: Character frequency
Write a function "char_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each character in the string.

Example:
char_frequency('hello world') -> {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""

def char_frequency(my_string: str) -> dict:
    d = {}
    for i in my_string:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] +=1
    return d

# print(char_frequency('hello world'), {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# print(char_frequency(''), {})
# print(char_frequency('a'*10**1 + 'b' + 'a'*10**1), {'a': 2*10**1, 'b': 1})
# print(char_frequency('abcabc'), {'a': 2, 'b': 2, 'c': 2})
# print(char_frequency('abcdefg'), {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1})


"""
Exercise-5: Unique words
Write a function "unique_words(my_string: str) -> int" that takes a
string and returns the number of unique words in the string.

Example:
unique_words('hello world hello') -> 2
"""

def unique_words(my_string: str) -> int:
    if len(my_string) == 0:
        return 0
    my_list = my_string.split(' ')
    new_list = []
    for i in my_list:
        if i != '':
            new_list.append(i)
    count_words = len(set(new_list))
    # print(set(my_string.split(' ')))
    return count_words


# print(unique_words('hello world hello'), 2)
# print(unique_words(''), 0)
# print(unique_words('a '*10**2), 1)
# print(unique_words('hello hello world world'), 2)
# print(unique_words('hello world hello world'), 2)
    
"""
Exercise-6: Word frequency
Write a function "word_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each word in the string.

Example:
word_frequency('hello world hello') -> {'hello': 2, 'world': 1}
"""

def word_frequency(my_string: str) -> dict:
    if len(my_string) == 0:
        return {}
    my_list = my_string.split(' ')
    new_dict = {}
    for i in my_list:
        if i != '' and i not in new_dict.keys():
            new_dict[i] = 1
        elif i != '' and i in new_dict.keys():
            new_dict[i] += 1
        else:
            pass
    return new_dict


# print(word_frequency('hello world hello'), {'hello': 2, 'world': 1})
# print(word_frequency(''), {})
# print(word_frequency('a '*10**2), {'a': 10**2})
# print(word_frequency('hello hello world world'), {'hello': 2, 'world': 2})
# print(word_frequency('hello world hello world'), {'hello': 2, 'world': 2})
    
"""
Exercise-7: Count elements in range
Write a function "count_in_range(my_list: list, start: int, end: int) -> int" that
takes a list of integers and two integers as range boundaries and
returns the count of unique elements within that range in the list.

Example:
count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4) -> 3
"""

def count_in_range(my_list: list, start: int, end: int) -> int:
    unique_count = 0
    for i in range(start, end+1):
        # print(i)
        if i in my_list:
            unique_count +=1
    return unique_count


# print(count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4), 3)
# print(count_in_range([], 2, 4), 0)
# print(count_in_range(list(range(1, 10**2+1)), 2, 4), 3)
# print(count_in_range(list(range(1, 10**3+1)), 500, 10**3), 501)
# print(count_in_range([1, 2, 3, 4, 5], 6, 10), 0)
    

"""
Exercise-8: Swap dictionary keys and values
Write a function "swap_dict(d: dict) -> dict" that takes a dictionary
and returns a new dictionary where keys become values and values become keys.
if you face duplicates, the first key should be saved.

Example:
swap_dict({1: 'a', 2: 'b', 3: 'c'}) -> {'a': 1, 'b': 2, 'c': 3}
"""

def swap_dict(d: dict) -> dict:
    new_d = {}
    for key, value in d.items():
        if value not in new_d.keys():
            new_d[value] = key
    return new_d


# print(swap_dict({1: 'a', 2: 'b', 3: 'c'}), {'a': 1, 'b': 2, 'c': 3})
# print(swap_dict({}), {})
# print(swap_dict({i: str(i) for i in range(1, 10**1+1)}), {str(i): i for i in range(1, 10**1+1)})
# print(swap_dict({'a': 1, 'b': 1}), {1: 'a'})
# print(swap_dict({'a': 1, 'b': 2, 'c': 3}), {1: 'a', 2: 'b', 3: 'c'})
    
"""
Exercise-9: Subset check
Write a function "is_subset(set1: set, set2: set) -> bool" that takes two
sets and returns True if set2 is a subset of set1, and False otherwise.

Example:
is_subset({1, 2, 3, 4, 5}, {3, 4, 5}) -> True
"""

def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)


# print(is_subset({1, 2, 3, 4, 5}, {3, 4, 5}), True)
# print(is_subset({1, 2, 3}, {4, 5, 6}), False)
# print(is_subset(set(), {1, 2, 3}), False)
# print(is_subset({i for i in range(1, 10**6+1)}, {i for i in range(500000, 10**6+1)}), True)
# print(is_subset({1, 2, 3}, {1, 2, 3}), True)
    

"""
Exercise-11: Intersection of lists
Write a function "list_intersection(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in both lists.

Example:
list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""

def list_intersection(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    # print(list1, list2)
    # print(set1, set2)
    set3 = set1&set2
    return list(set3)


# print(list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])
# print(list_intersection([1, 2, 3], [4, 5, 6]), [])
# print(list_intersection([], [1, 2, 3]), [])
# print(list_intersection(list(range(1, 10**1+1)), list(range(50, 10**1+2))), list(range(50, 10**1+1)))
# print(list_intersection([1, 2, 3], [1, 2, 3]), [1, 2, 3])



"""
Exercise-11: Union of lists
Write a function "list_union(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in either of the lists.

Example:
list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [1, 2, 3, 4, 5, 6, 7]
"""

def list_union(list1: list, list2: list) -> list:
    return list(set(list1)|set(list2))


# print(list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
# print(list_union([1, 2, 3], []), [1, 2, 3])
# print(list_union([], [1, 2, 3]), [1, 2, 3])
# print(list_union(list(range(1, 10**1+1)), list(range(5, 10**1+2))), list(range(1, 10**1+2)))
# print(list_union([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
    


"""
Exercise-12: Most frequent element
Write a function "most_frequent(my_list: list) -> int" that takes a
list of integers and returns the most frequent element in the list.

Example:
most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 1
"""

def most_frequent(my_list: list) -> int:
    f = 0
    number = 0
    temp = set(my_list)

    for i in temp:
        if my_list.count(i) > f:
            f = my_list.count(i)
            number = i
    return number


# print(most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]), 1)
# print(most_frequent([1, 2, 3]), 1)  # in case of tie, return the one that appears first
# print(most_frequent([1]*10**6 + [2]*10**6 + [3]), 1)
# print(most_frequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*10**5 + [11]), 1)
# print(most_frequent([1]), 1)
    

"""
Exercise-13: Least frequent element
Write a function "least_frequent(my_list: list) -> int" that takes a
list of integers and returns the least frequent element in the list.

Example:
least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 3
"""

def least_frequent(my_list: list) -> int:
    if len(my_list) == 0:
        return None
    temp = {}

    for i in my_list:
        # print(i)
        if i in temp.keys():
            temp[i] += 1
        else: temp[i] = 1

    max_key = min(temp, key=temp.get)
    return max_key
    

# print(least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]), 3)
# print(least_frequent([1, 2, 3]), 1)  # in case of tie, return the one that appears first
# print(least_frequent([1]*10**6 + [2]*10**6 + [3]), 3)
# print(least_frequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*10**5 + [11]), 11)
# print(least_frequent([1]), 1)