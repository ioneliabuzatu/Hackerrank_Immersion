def insertionSort(list):
    for i in range(1, len(list)):
        for j in range(0, i):
            if (list[i] < list[j]):
                item = list.pop(i)
                list.insert(j, item)

n = int(input().strip())
a = [int(i) for i in input().strip().split()]
insertionSort(a)
print(" ".join(map(str,a)))
