# line = input()
# items = line.split()
# int_items = []
# last_index = len(items)-1
# index = 1
# while index <= last_index:
#     if items[index] > items[index-1]:
#         print(items[index], end=' ')
#     index +=1


# for index, item in enumerate(items):
#     if index % 2 == 0:
#         print(item, end=' ')

# last_index = len(items)-1
# current_index = 0
# while current_index <= last_index:
#     print(items[current_index])
#     current_index += 1

# for index in range(len(items)):
#     if index % 2 == 0:
#         print(items[index], end=' ')


# numbers = list(map(int, input().split()))

# count = 0

# for i in range(1, len(numbers)-1):
#     if numbers[i] > numbers[i-1] and numbers[i]>numbers[i+1]:
#         count+=1
# print(count)

numbers = list(map(int, input().split()))
cnt = 0
iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("end of numbers")
        break


if len(numbers) == 0:
       exit()