# from tkinter import *

# window = Tk()

# try:
#     file = open("non_existent_file.txt") 
#     dictionary = {"key":"value"}
#     print(dictionary["wrong_key"])
# except FileNotFoundError:
#     file = open("non_existent_file.txt", "w")
#     print("File Not Found Error")
# except KeyError as error_message:
#     print(error_message)
# else:
#     contents = file.read()
#     print(contents)
# finally:
#     file.close()

# window.mainloop()

# height = float(input("Height: "))

# if height >= 3:
#     raise ValueError("You have entered an unrealistic height.")

# weight = int(input("Weight: "))


# bmi = weight / height ** 2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try: 
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie.")
#     else:
#         print(fruit + " pie")

# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except:
            pass
    
    return total_likes


count_likes(facebook_posts)


