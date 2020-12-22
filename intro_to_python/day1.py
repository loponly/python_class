num = 1
ug = "word"

num2 = 1.2

print(str(num)+ug+' ')
print(f'{ug} - {num}')

print(ug)
print(num2)
# str,int,float,def,for, -> Not allowed to declare variable


# function
def func(num1, num2):
    print('ji')
    return num1 + num2


# list
numbers = [1, 2, 3, 5, func(1, 23)]

# dictionary
hun = {
    'ner': 'Bob',
    'nas': 34,
    'numbers': numbers
}

print(list(hun.keys()))
print(list(hun.values()))

# for in list
for index, number in enumerate(numbers):
    print(f'index: {index} value: {number}')
    # print(f'value: {number}')

print(hun['ner'])

# Dictionary in list
for key, value in hun.items():
    print(f'key: {key} value: {value}')


# list manipulation
empty_list = []

empty_list.append('hello')
empty_list.append('world')

empty_list[0] = 'other'

ug = ug + 's'
# print(ug)

#              start,end,incremental
for i in range(10, 0, -1):
    print(i)

# if condtion
if numbers[1] < numbers[0] or numbers[2] > number[3]:
    print('more')
elif numbers[2] > numbers[3]:
    print('less')
else:
    print('other')
