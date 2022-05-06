def selectionSort(list):
    n = len(list)
    i = 0
    for i in range(n-2):
        min = i
        j = i + 1
        print(i)
        for j in range(n-1):
            if list[j] < list[min]:
                min = j
                print(j)
        temp = list[min]
        list[min] = list[j]
        list[j] = temp
    return list

list = [2, 7, 4, 1 ,5 ,3]
print(selectionSort(list))
