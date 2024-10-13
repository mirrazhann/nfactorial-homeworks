def line():
    print('\n\n===============================================================================\n\n')
    
def twoSum():
    print ('Exercise 1: two-sum')
    print ('Declare 2 numbers and calculate their sum\n')

    a = 10
    b = 15

    sum = a + b
    print(f'{a} + {b} = {sum}')



def reverseString():
    print('''Exercise 2: reverse-string\n
Declare a string
Reverse the string
Print the reversed string\n''')
    
    string = "Alice's Adventures in Wonderland"
    print(f'Original:\n{string}')
    print(f'Reverse:\n{string[::-1]}')



def stringLength():
    print('''Exercise 3: string-length\n
Declare a string
Calculate the length of the string
Print the length\n''')
    
    string = "Alice's Adventures in Wonderland"
    print(f'Original:\n{string}')
    print(f'lenght: {string.__len__()}')



def concatenateString():
    print('''Exercise 4: concatenate-string
Declare 2 strings
Concatenate the strings
Print the concatenated string\n''')
    
    string1 = "Alice's Adventures "
    string2 = "in Wonderland"
    string3 = string1 + string2
    print(f'string1:\n{string1}')
    print(f'string2:\n{string2}')
    print(f'concatenate-string: {string3}')



def isVowel():
    print('''Exercise 5: is-vowel
Declare a character
Check if the character is a vowel
Print the result\n''')
    
    chr = "e"
    if (chr == 'e' or chr == 'u' or chr == 'Y' or chr == 'o' or chr == 'a'):
        print(f'"{chr}" is vowel')
    elif (chr == 'E' or chr == 'U' or chr == 'Y' or chr == 'O' or chr == 'A'):
        print(f'"{chr}" is vowel')
    else :
        print(f'"{chr}" is constant')



def swapFirstLast():
    print('''Exercise 6: swap-first-last
Declare a string
Swap the first and last characters of the string
Print the modified string\n''')

    string = 'Adventures'
    
    print(f'Original: {string}')
    print(f'Modified: {string[-1:] + string[1:-1] + string[:1]}')



def toUppercase():
    print('''Exercise 7: to-uppercase
Declare a string
Convert the string to uppercase
Print the uppercase string\n''')

    string = 'Alice\'s Adventures in Wonderland'

    print(f'Original: {string}')
    print(f'To uppercase: {string.upper()}')



def rectangleArea():
    print('''Exercise 8: rectangle-area
Declare the length and width of a rectangle
Calculate the area of the rectangle
Print the area\n''')

    a = 5
    b = 8
    S = a*b

    print(f'a = {a}')
    print(f'b = {b}')
    print(f'{S} = {a} * {b}')


    
def isEven():
    print('''Exercise 9: is-even
Declare a number
Check if the number is even
Print the result\n''')

    a = 48
    if a % 2 == 0:
        print(f'{a} is even')
    else:
        print(f'{a} is not even')

         
def extractFirstThree():
    print('''Exercise 10: extract-first-three
Declare a string
Extract the first three characters of the string
Print the extracted characters\n''')
    
    string = 'Wonderland'
    new_string = string[0:3]

    print(f'Original: {string}')
    print(f'New string: {new_string}')



def stringInterpolation():
    print('''Exercise 11: string-interpolation
Declare 2 variables, name and age
Use string interpolation to create a message
Print the message\n''')

    name = 'Ann'
    age = 23
    user_info = f'''Name: {name}
Age: {age}'''

    print(user_info)



def stringSlicing():
    print('''Exercise 12: string-slicing
Declare a string
Extract the characters from index 2 to 5 (inclusive)
Print the extracted characters\n''')

    string = 'Wonderland'
    new_string = string[1:5]

    print(f'Original: {string}')
    print(f'New string: {new_string}')



def typeConversion():
    print('''Exercise 13: type-conversion
Declare a number as a string
Convert the string to an integer
Print the integer\n''')

    a = '4'
    b = int(a)
    print(f'{b} - {type(b)}')


def stringRepetition():
    print('''Exercise 14: string-repetition
Declare a string
Repeat the string 3 times
Print the repeated string\n''')

    string = "Alice's Adventures in Wonderland\n"
    print(string*3)



def calculateQuotientRemainder():
    print('''Exercise 15: calculate-quotient-remainder
Declare 2 numbers
Calculate the quotient and remainder
Print the quotient and remainder\n''')

    a = 19
    b = 7
    quotient = a // b
    remainder = a % b
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'Quotient: {a} // {b} = {quotient}')
    print(f'Remainder: {a} % {b} = {remainder}')



def floatDivision():
    print('''Exercise 16: float-division
Declare 2 numbers
Calculate the result of float division
Print the result\n''')

    a = 26
    b = 13
    c = a/b

    print(f'{a} / {b} = {c}')



def stringMethods():
    print('''Exercise 17: string-methods
Declare a string
Use a string method to count the occurrences of a character
Print the count\n''')

    string = "Alice's Adventures in Wonderland"
    find_char = 'A'
    count = string.count(find_char)
    print(f'String: {string}')
    print(f'"{find_char}": {count} occurrences in string')



def escapeSequences():
    print('''Exercise 18: escape-sequences
Declare a string with double quotes inside
Use escape sequences to include the quotes
Print the string\n''')

    string = "She said \"Hi!\""
    print(string)



def multiLineString():
    print('''Exercise 19: multi-line-string
Declare a multi-line string
Print the multi-line string\n''')

    string = """Line 1
Line 2
Line 3\nLine 4\nLine 5"""

    print(string)



def exponentiation():
    print('''Exercise 20: exponentiation
Declare 2 numbers, base and exponent
Calculate the result of base to the power of exponent
Print the result\n''')

    a = 11
    b = 3
    c = a**b
    print(f'{a}**{b}={c}')




def exponentiation_21():
    print('''Exercise 20: exponentiation
Declare 2 numbers, base and exponent
Calculate the result of base to the power of exponent
Print the result\n''')

    string = 'detartrated'

    center = string.__len__() // 2

    part1 = string[0:center]
    if string.__len__() % 2 == 0 :
        center = center - 1
        part2 = string[-1:center:-1]
    else:
        part2 = string[-1:center:-1]

    if part1 == part2:
        print(f'"{string}" is palindrome')
    else:
        print(f'"{string}" is not palindrome')



def checkAnagrams():
    print('''Exercise 22: check-anagrams
Declare 2 strings
Check if the strings are anagrams (ignoring case)
Print the result\n''')

    string1 = 'listen'
    string2 = 'silent'

    a = sorted(string1.lower())
    b = sorted(string2.lower())

    print(f'string 1: {string1}')
    print(f'string 2: {string2}')

    if a == b:
        print('strings are anagrams')
    else :
        print('strings are not anagrams')




if __name__ == "__main__":
    line()
    twoSum()
    line()
    reverseString()
    line()
    stringLength()
    line()
    concatenateString()
    line()
    isVowel()
    line()
    swapFirstLast()
    line()
    toUppercase()
    line()
    rectangleArea()
    line()
    isEven()
    line()
    extractFirstThree()
    line()
    stringInterpolation()
    line()
    stringSlicing()
    line()
    typeConversion()
    line()
    stringRepetition()
    line()
    calculateQuotientRemainder()
    line()
    floatDivision()
    line()
    stringMethods()
    line()
    escapeSequences()
    line()
    multiLineString()
    line()
    exponentiation()
    line()
    exponentiation_21()
    line()
    checkAnagrams()
    line()
