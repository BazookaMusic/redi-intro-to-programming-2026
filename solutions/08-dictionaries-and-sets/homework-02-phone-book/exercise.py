def add_contact(book, name, number):
    book[name] = number


def find_number(book, name):
    return book.get(name, "Unknown")


def remove_contact(book, name):
    if name in book:
        del book[name]
        return True
    return False


def names_starting_with(book, letter):
    names = []
    for name in book:
        if name[0] == letter:
            names.append(name)
    return names


book = {"Ana": "0151 111", "Ben": "0152 222"}
print(find_number(book, "Zoe"))
add_contact(book, "Zoe", "0153 333")
print(find_number(book, "Zoe"))
print(remove_contact(book, "Ben"))
print(remove_contact(book, "Ben"))
print(names_starting_with(book, "Z"))
