def file_to_int_list(file_name):
    with open(file_name) as file:
        return [int(i.strip()) for i in file.readlines()]


file1 = file_to_int_list("./file1.txt")
file2 = file_to_int_list("./file2.txt")

result = [i for i in file1 if i in file2]

print(result)
