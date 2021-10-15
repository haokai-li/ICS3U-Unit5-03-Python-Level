#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about level


def check_level(level):
    # This function check the level

    # process
    if level == "4+":
        answer_string = 97
    elif level == "4":
        answer_string = 90
    elif level == "4-":
        answer_string = 84
    elif level == "3+":
        answer_string = 78
    elif level == "3":
        answer_string = 75
    elif level == "3-":
        answer_string = 71
    elif level == "2+":
        answer_string = 68
    elif level == "2":
        answer_string = 64
    elif level == "2-":
        answer_string = 61
    elif level == "1+":
        answer_string = 58
    elif level == "1":
        answer_string = 54
    elif level == "1-":
        answer_string = 51
    elif level == "R":
        answer_string = 0
    else:
        answer_string = -1

    return answer_string


def main():
    # This function just call other functions

    # input
    user_string = input("Please enter your level(ex. 4+ or R): ")
    print("")

    # call functions
    checked_level = check_level(user_string)

    # output
    if checked_level == -1:
        print("This is not a level.")
    else:
        print("Your score percentage is {}%".format(checked_level))

    print("\nDone.")


if __name__ == "__main__":
    main()
