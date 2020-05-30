# My first attempt to write bubble sort algorithm


def books_sorted(books):
    alphabet = "aąbcćdeęfghijklłmnoópqrstuvwxyzźż"
    end = len(books) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, end):
            if alphabet.index(books[i].lower()[0]) > alphabet.index(
                books[i + 1].lower()[0]
            ):
                sorted = False
                books[i], books[i + 1] = books[i + 1], books[i]
            elif alphabet.index(books[i].lower()[0]) == alphabet.index(
                books[i + 1].lower()[0]
            ):

                for j in range(1, len(books[i])):
                    if alphabet.index(
                        books[i].replace(" ", "").lower()[j]
                    ) > alphabet.index(books[i + 1].replace(" ", "").lower()[j]):
                        sorted = False
                        books[i], books[i + 1] = books[i + 1], books[i]
                        sorted = True
                        break

    return books


books = ["Nad Niemnem", "Dżuma", "Grona Gniewu", "Wiedźmin", "Dom na skale"]
print(books_sorted(books))
