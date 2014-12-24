array = []
length = 0
tempAry = []
def merge_sort(input_ary):
    global array
    global length
    global tempAry
    array = input_ary
    length = len(input_ary)
    tempAry = [None] * length
    do_merge_sort(0, length - 1)

def do_merge_sort(low, high):
    if low < high:
        middle = low + (high - low) // 2
        do_merge_sort(low, middle)
        do_merge_sort(middle + 1, high)
        merge_part(low, middle, high)

def merge_part(low, middle, high):
    
    for i in range(low, high + 1, 1):
        tempAry[i] = array[i]
    

    i = low
    j = middle + 1
    k = low
    while i <= middle and j <= high:
        if tempAry[i] < tempAry[j]:
            array[k] = tempAry[i]
            i += 1
        else:
            array[k] = tempAry[j]
            j += 1
        k += 1

    while i <= middle:
        array[k] = tempAry[i]
        k += 1
        i += 1

input_array = [23, 45, 22]
merge_sort(input_array)
print(array)