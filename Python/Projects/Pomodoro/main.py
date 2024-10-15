import os
import time
import platform

from datetime import date

clear = lambda: (
    os.system("cls") if platform.system() == "Windows" else os.system("clear")
)
bar_width = lambda: os.get_terminal_size().columns - 2
append_minute = lambda i: "s" if i > 119 else ""
append_second = lambda i: "s" if i > 1 else ""


def timer(seconds):
    clear()
    for i in reversed(range(seconds)):
        if i >= 60:
            print(f"{i//60} Minute{append_minute(i)} remaining.")
        elif i > 0:
            print(f"{i} Second{append_second(i)} remaining.")

        progress_percent = (seconds - i) / seconds
        plus_chars = "+" * int(bar_width() * progress_percent)
        minus_chars = "-" * int(bar_width() - len(plus_chars))
        print(f"[{plus_chars}{minus_chars}]")
        time.sleep(1)
        print("\x1B[1A\x1B[0K\x1B[1A\x1B[0K", end="")


def append_to_logfile(string, filename):
    logfile = open(f"{filename}.txt", "a")
    logfile.write(string)
    logfile.close()

def create_logfile():
    f = open(f"{date.today()}.txt", "x")


print(
    """
--------------------------------------------------------\n
-              Welcome to the Pomodoro Timer           -\n
--------------------------------------------------------\n
    """
)


minutes = int(
    input("How long would you like your working splits to be? (Minutes): \n")
)

split_seconds = minutes * 60

minutes = int(input("How long would you like your breaks to be? (Minutes): \n"))
break_seconds = minutes * 60

working = "y"

while working == "y":
    print("Working..")
    timer(split_seconds)

    print("Work split is over")
    time.sleep(1)
    clear()

    working = input(
        "Are you ready to start your break? ('y' = yes, 'q' = quit)\n"
    )
    clear()

    print("Break time!")
    timer(break_seconds)

    working = input(
        "Would you like to continue working? ('y' = Yes, 'n' = No)\n"
    )

print("See you later")
