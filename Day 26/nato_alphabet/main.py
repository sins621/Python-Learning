import pandas

npa_data = pandas.read_csv("./Day 26/nato_alphabet/nato_phonetic_alphabet.csv")
npa_dict = {row.letter: row.code for (index, row) in npa_data.iterrows()}

user_name = input("Enter your name: ").upper()

user_npa = [npa_dict[letter] for letter in user_name]

print(user_npa)
