books = [
    "Pride and Prejudice",
    "Heart of Darkness",
    "The Grapes of Wrath",
    "Mackbet",
    "Wuthering Heights",
    "Vanity Fair",
]


def find_smallest_index(books):
    smallest = ord(books[0][0].lower())
    smallest_index = 0

    for i in range(1, len(books)):
        if ord(books[i][0].lower()) < smallest:
            smallest = ord(books[i][0].lower())
            smallest_index = i
    return smallest_index


print(find_smallest_index(books))


def selection_sort(books):
    new_books = []
    for i in range(len(books)):
        smallest = find_smallest_index(books)
        new_books.append(books.pop(smallest))
    return new_books


print(selection_sort(books))
