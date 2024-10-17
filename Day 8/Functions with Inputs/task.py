def calculate_love_score(name1, name2):
    total1 = 0
    total2 = 0
    KEYWORDS1 = ["T", "R", "U", "E"]
    KEYWORDS2 = ["L", "O", "V", "E"]
    names_combined = list(name1 + name2)

    for i in range(len(KEYWORDS1)):
        for l in names_combined:
            if l.lower() == KEYWORDS1[i].lower():
                total1 += 1

        for l in names_combined:
            if l.lower() == KEYWORDS2[i].lower():
                total2 += 1

    print(f"{total1}{total2}")


calculate_love_score(list("Kanye West"), list("Kim Kardashian"))
