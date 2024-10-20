"""
Exercise-1: is_prime
Write a function "is_prime(n: int) -> bool" that takes an integer 'n' 
and checks whether it is prime. Function should return a boolean value.

Example:
is_prime(7) -> True
is_prime(10) -> False
"""

def is_prime(n: int) -> bool:
    for i in range(2, 9):
        if n % i == 0 and n != i:
            return False
    # write your code here
    return True

# print(is_prime(7))

"""
Exercise-2: nth_fibonacci
Write a function "nth_fibonacci(n: int) -> int" that 
takes an integer 'n' and returns the nth number in the Fibonacci sequence.

Example:
nth_fibonacci(6) -> 5
nth_fibonacci(9) -> 21
"""

def nth_fibonacci(n: int) -> int: 
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f1 = 0
        f2 = 1
        i = 2
        while i < n:
            f_temp = f1 + f2
            f1, f2 =  f2, f_temp
            i += 1

    return f2

# print(nth_fibonacci(1))
# print(nth_fibonacci(2))
# print(nth_fibonacci(3))
# print(nth_fibonacci(4))
# print(nth_fibonacci(5))
# print(nth_fibonacci(6))
# print(nth_fibonacci(20))

"""
Exercise-3: factorial
Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.

Example:
factorial(5) -> 120
factorial(6) -> 720
"""

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n+1):
            f = f*i
        return f

# print(factorial(0))
# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
# print(factorial(10))



"""
Exercise-4: count_vowels
Write a function "count_vowels(s: str) -> int" that 
takes a string 's' and returns the number of vowels in the string.

Example:
count_vowels("hello") -> 2
count_vowels("world") -> 1
"""

def count_vowels(s: str) -> int:
    count = 0
    for char in s:
        match char:
            case "a" | "e" | "i" | "o" | "u":
                count += 1
            case "A" | "E" | "I" | "O" | "U":
                count +=1
            case _:
                pass

    return count

# print(count_vowels('hello'))
# print(count_vowels('world'))
# print(count_vowels('apple'))
# print(count_vowels('Python'))
# print(count_vowels(''))
# print(count_vowels('AEIOU'))
# print(count_vowels("a" * 1000))

"""
Exercise-5: sum_of_digits
Write a function "sum_of_digits(n: int) -> int" that 
takes an integer 'n' and returns the sum of its digits.

Example:
sum_of_digits(12345) -> 15
sum_of_digits(98765) -> 35
"""

def sum_of_digits(n: int) -> int:
    n = abs(n)
    s = 0
    while n > 0:
        s += n%10
        n = n//10
    #12345
    return s

# print(sum_of_digits(12345))
# print(sum_of_digits(98765))
# print(sum_of_digits(0))
# print(sum_of_digits(-12345))
# print(sum_of_digits(10000))
# print(sum_of_digits(10 ** 1000 - 1))



"""
Exercise-6: reverse_string
Write a function "reverse_string(s: str) -> str" that takes a string 's' and returns the string reversed.

Example:
reverse_string("hello") -> "olleh"
reverse_string("world") -> "dlrow"
"""

def reverse_string(s: str) -> str:
    str_len = len(s)-1
    new_str = ''
    while str_len >= 0:
        new_str += s[str_len]
        str_len -=1
    return new_str

# print(reverse_string('hello'))

"""
Exercise-7: sum_of_squares
Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and 
returns the sum of squares of all integers from 1 to 'n'.

Example:
sum_of_squares(4) -> 30
sum_of_squares(5) -> 55
"""

def sum_of_squares(n: int):
    s = 0
    i = 1
    while i <= n:
        s += i**2
        i +=1
    return s
    # write your code here
    

# print(sum_of_squares(1))
# print(sum_of_squares(2))
# print(sum_of_squares(3))
# print(sum_of_squares(4))
# print(sum_of_squares(5))

"""
Exercise-8: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes an 
integer 'n' and returns the length of the Collatz sequence starting with 'n'.

Example:
collatz_sequence_length(6) -> 9
collatz_sequence_length(27) -> 112
"""

def collatz_sequence_length(n: int) -> int:
    count = 1
    while n > 1:
        if n%2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        count += 1
    # write your code here

    return count

# print(collatz_sequence_length(6))
# print(collatz_sequence_length(27))
# print(collatz_sequence_length(1))
# print(collatz_sequence_length(2))
# print(collatz_sequence_length(10000))

"""
Exercise-9: is_leap_year
Write a function "is_leap_year(year: int) -> bool" that takes an 
integer 'year' and returns True if 'year' is a leap year, and False otherwise.

Example:
is_leap_year(2000) -> True
is_leap_year(1900) -> False
"""

def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        elif year % 100 == 0 and year % 400 == 0:
            return True
        return True
    else:
        return False
    
# print(is_leap_year(2000))
# print(is_leap_year(1900))
# print(is_leap_year(2020))
# print(is_leap_year(2021))
# print(is_leap_year(10000))


"""
Exercise-10: count_words
Write a function "count_words(s: str) -> int" that takes a string 's' and 
returns the number of words in the string. Assume words are separated by spaces.

Example:
count_words("Hello world") -> 2
count_words("This is a test") -> 4
"""

def count_words(s: str) -> int:
    words = 0
    is_word = False

    for char in s:
        if char != ' ' and is_word == False:
            is_word = True
            words +=1
        elif char == ' ':
            is_word = False

    return words

# print(count_words("Hello world"))
# print(count_words("This is   a test"))
# print(count_words(""))
# print(count_words("a"))
# print(count_words("word " * 10))

    
"""
Exercise-11: is_palindrome
Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and 
checks if the string is a palindrome. The function should return True if the 
string is a palindrome, and False otherwise.

Example:
is_palindrome("racecar") -> True
is_palindrome("hello") -> False
"""

def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    
    middle = len(s) // 2

    for i in range(middle):
        if s[i] != s[len(s)-1-i]:
            return False
    
    return True


"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that 
takes three integers 'n', 'x', and 'y', and returns the sum of all the 
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.

Example:
sum_of_multiples(10, 3, 5) -> 33
sum_of_multiples(20, 7, 11) -> 168
"""

def sum_of_multiples(n: int, x: int, y: int) -> int:
    s = 0
    for i in range(1, n+1):
        # print(i)
        if i % x == 0 or i % y == 0:
            s += i
    return s       
# print(sum_of_multiples(10, 3, 5))
# print(sum_of_multiples(20, 7, 11))
# print(sum_of_multiples(1, 1, 1))
# print(sum_of_multiples(0, 1, 1))
# print(sum_of_multiples(1000, 3, 5))


"""
Exercise-13: gcd
Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their greatest common divisor (GCD).

Example:
gcd(56, 98) -> 14
gcd(27, 15) -> 3
"""

def gcd(a: int, b: int) -> int:
    if a == b:
        return a
    min_number = a if a < b else b
    max_number = a if a > b else b
    if a == b:
        min_number, max_number = a
        
    while max_number - min_number != 0:
        temp_a, temp_b = min_number, max_number - min_number
        min_number = temp_a if temp_a < temp_b else temp_b
        max_number = temp_a if temp_a > temp_b else temp_b
        # print(max_number, min_number)
    
    return min_number
    # write your code here

# print(gcd(56, 98))
# print(gcd(27, 15))
# print(gcd(0, 0))
# print(gcd(1, 1))
# print(gcd(1000000, 500000))

"""
Exercise-14: lcm
Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their least common multiple (LCM).

Example:
lcm(5, 7) -> 35
lcm(6, 8) -> 24
"""

def lcm(a: int, b: int) -> int:
    if a == b:
        if a == 0:
            return 0
        min_number = a
    else:
        min_number = a if a < b else b
        max_number = a if a > b else b

        
        while max_number - min_number != 0:
            temp_a, temp_b = min_number, max_number - min_number
            min_number = temp_a if temp_a < temp_b else temp_b
            max_number = temp_a if temp_a > temp_b else temp_b
        # print(max_number, min_number)
    
    lcm = int(a * b / min_number)
    return lcm

# print(lcm(5, 7), 35)
# print(lcm(6, 8), 24)
# print(lcm(1, 1), 1)
# print(lcm(0, 0), 0)
# print(lcm(1000, 500), 1000)
"""
Exercise-15: count_characters
Write a function "count_characters(s: str, c: str) -> int" that 
takes a string 's' and a character 'c', and returns the number of occurrences of 'c' in 's'.

Example:
count_characters("hello world", "l") -> 3
count_characters("apple", "p") -> 2


"""

def count_characters(s: str, c: str) -> int:
    count_char = 0
    for char in s:
        if char == c:
            count_char +=1
    # write your code here
    return count_char

# print(count_characters("hello world", "l"), 3)
# print(count_characters("apple", "p"), 2)
# print(count_characters("", "a"), 0)
# print(count_characters("a", "a"), 1)
# print(count_characters("ab", "a"), 1)
# print(count_characters("a" * 1000, "a"), 1000)

"""
Exercise-16: digit_count
Write a function "digit_count(n: int) -> int" that takes an 
integer 'n' and returns the number of digits in 'n'.

Example:
digit_count(123) -> 3
digit_count(4567) -> 4
"""

def digit_count(n: int) -> int:
    n = abs(n)
    count_digit = 0
    if n == 0:
        return 1
    while n > 0:
        count_digit += 1
        n = n//10
    return count_digit

# print(digit_count(123), 3)
# print(digit_count(4567), 4)
# print(digit_count(0), 1)
# print(digit_count(1), 1)
# print(digit_count(1000000), 7)

"""
Exercise-17: is_power_of_two
Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n' 
and returns True if 'n' is a power of 2, and False otherwise.

Example:
is_power_of_two(8) -> True
is_power_of_two(10) -> False
"""

def is_power_of_two(n: int) -> bool:
    if n < 0:
        return False
    
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        return True
    else:
        return False

# print(is_power_of_two(8), True)
# print(is_power_of_two(10), False)
# print(is_power_of_two(1), True)
# print(is_power_of_two(2), True)
# print(is_power_of_two(1024), True)

"""
Exercise-18: sum_of_cubes
Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n' 
and returns the sum of the cubes of all numbers from 1 to 'n'.

Example:
sum_of_cubes(3) -> 36
sum_of_cubes(4) -> 100
"""

def sum_of_cubes(n: int) -> int:
    # write your code here
    s = 0
    for i in range(1, n + 1):
        s += i**3
    return s

# print(sum_of_cubes(3), 36)
# print(sum_of_cubes(4), 100)
# print(sum_of_cubes(1), 1)
# print(sum_of_cubes(2), 9)
# print(sum_of_cubes(20), 44100)

"""
Exercise-19: is_perfect_square
Write a function "is_perfect_square(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is a perfect square, and False otherwise.

Example:
is_perfect_square(9) -> True
is_perfect_square(10) -> False
"""

def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

# print(is_perfect_square(9), True)
# print(is_perfect_square(10), False)
# print(is_perfect_square(1), True)
# print(is_perfect_square(4), True)
# print(is_perfect_square(1000000), True)
    
"""
Exercise-20: is_armstrong_number
Write a function "is_armstrong_number(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.

Example:
is_armstrong_number(153) -> True
is_armstrong_number(370) -> True
"""

def is_armstrong_number(n: int) -> bool:
    st = 0
    n_temp = abs(n)
    n_temp_2 = n_temp
    s = 0
    while n_temp > 0:
        st += 1
        n_temp = n_temp//10
    s = 0

    while n_temp_2 > 0:
        s += (n_temp_2%10) ** st
        n_temp_2 = n_temp_2//10

    if s == n:
        return True
    else:
        return False


# print(is_armstrong_number(153), True)
# print(is_armstrong_number(370), True)
# print(is_armstrong_number(371), True)
# print(is_armstrong_number(9474), True)
# print(is_armstrong_number(9475), False)