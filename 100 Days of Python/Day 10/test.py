# def format_name(f_name, l_name):
#     return str(f_name + " " + l_name).title()


# print(format_name("brad", "carpenter"))


def format_name(f_name, l_name):
    """Take a first and last name and ofrmat it to return the
    title case version of the name."""
    if f_name == "" or l_name == "":
        return

    return str(f_name + " " + l_name).title()

format_name
