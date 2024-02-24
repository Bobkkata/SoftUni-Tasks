# 1_numbers_dictionary

numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f"The variable number must be an integer")
    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print(f"Number does not exist in dictionary")
    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print(f"Number does not exist in dictionary")
    line = input()
print(numbers_dictionary)


# 2_email_validator


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class NameTooLongError(Exception):
    pass


class MinUnderscore(Exception):
    pass


email = input()

VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_SYMBOL_COUNT = 4
MAX_NAME_SYMBOL_COUNT = 15


while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")
    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")
    elif len(email.split("@")[0]) <= MIN_NAME_SYMBOL_COUNT:
        raise NameTooShortError("Name must be more than 4 symbols!")
    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    elif len(email.split("@")[0]) >= MAX_NAME_SYMBOL_COUNT:
        raise NameTooLongError("Name must not exceed 10 symbols!")

    print("Email is valid")
    email = input()

