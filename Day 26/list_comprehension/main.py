# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]

# print(new_list)

# numbers = []

# for i in range(1, 5):
#     numbers.append(i*2)

# print(numbers)

# new_list = [i*2 for i in range(1, 5)]

# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

long_names = [name.upper() for name in names if len(name) > 5]

print(long_names) 