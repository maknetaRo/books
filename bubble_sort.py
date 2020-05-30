def bubble_sort(sequence):
    indexing_length = len(sequence) - 1
    sorted = False

    counter = 0
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if sequence[i] > sequence[i + 1]:
                sorted = False
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                counter += 1

    return sequence, counter


print(bubble_sort([3, 2, 1, 4, 7, 5, 6]))
