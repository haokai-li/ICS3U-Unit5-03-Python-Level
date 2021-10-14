#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about level


def check_level(string):
    # This function check the level

    # process
    if string == "4+":
        answer_string = "97%"
    elif string == "4":
        answer_string = "90%"
    elif string == "4-":
        answer_string = "84%"
    elif string == "3+":
        answer_string = "78%"
    elif string == "3":
        answer_string = "75%"
    elif string == "3-":
        answer_string = "71%"
    elif string == "2+":
        answer_string = "68%"
    elif string == "2":
        answer_string = "64%"
    elif string == "2-":
        answer_string = "61%"
    elif string == "1+":
        answer_string = "58%"
    elif string == "1":
        answer_string = "54%"
    elif string == "1-":
        answer_string = "51%"
    elif string == "R":
        answer_string = "0%"
    else:
        answer_string = "-1"

    return answer_string


def main():
    # This function just call other functions

    # input
    user_string = input("Please enter your level(ex. 4+ or R): ")
    print("")

    # call functions
    checked_level = check_level(user_string)

    # output
    print("Your secore percentage is {}".format(checked_level))

    print("\nDone.")


if __name__ == "__main__":
    main()
