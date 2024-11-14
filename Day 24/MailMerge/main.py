# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = []

with open("Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    contents = letter.readlines()
    for name in names:
        new_string = ""
        new_name = name.strip()
        for line in contents:
            new_line = line.replace("[name]", f"{new_name}")
            new_string += new_line
        with open(f"Output/ReadyToSend/{new_name}.txt", mode="w") as new_letter:
            new_letter.write(new_string)
