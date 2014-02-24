def insert_sort(numbers, noDecre=True):
    if len(numbers) <= 1:
        return numbers
    for i in range(1, len(numbers)):
        insert_one = numbers[i]
        j = i - 1
        if noDecre:
            while j >= 0 and insert_one < numbers[j]:
                numbers[j + 1] = numbers[j]
                j = j - 1
            numbers[j + 1] = insert_one
        else:
            while j >= 0 and insert_one > numbers[j]:
                numbers[j + 1] = numbers[j]
                j = j - 1
            numbers[j + 1] = insert_one
    return numbers

if __name__ == '__main__':
    numArray = [31, 41, 59, 26, 41, 58]
    print insert_sort(numArray)
    print insert_sort(numArray, False)