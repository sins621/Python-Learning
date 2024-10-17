def is_leap_year(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 != 0:
                return False
            else:
                return True


def print_function(is_leap_year):
    if is_leap_year:
        print("True")
    else:
        print("False")

print_function(is_leap_year(2000))
print_function(is_leap_year(2100))
print_function(is_leap_year(1989))
