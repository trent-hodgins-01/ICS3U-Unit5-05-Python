# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/18/2021
# This is the Canada Post program
# The user enters in a lot of information
# The program displays the information formatted correctly


def information(
    full_name,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartment=None,
):
    # return information formatted correcty

    information = full_name + "\n"
    if apartment != None:
        information = information + apartment + "-"
    information = information + street_number
    information = information + " " + street_name
    information = information + "\n" + city
    information = information + " " + province
    information = information + "  " + postal_code

    return information


def main():
    # gets a users name and other information, and prints it formatted correctly
    middle_name = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name AND type (Main ST, Express Pkwy...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abbreviation, ex ON, BC...): ")
    postal_code = input("Enter you postal code (A1B 2C3): ")

    if middle_name != None:
        formated_correctly = information(
            full_name, street_number, street_name, city, province, postal_code
        )
    else:
        formated_correctly = information(
            full_name, street_number, street_name, city, province, postal_code
        )

    print("")
    print(formated_correctly.upper())
    print("\nDone.")


if __name__ == "__main__":
    main()
