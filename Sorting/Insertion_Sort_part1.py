n = input()
array = [int(i) for i in input().strip().split()]
def sort_1(array):
    i = array.__len__() -1#unsorted element
    e = array[i]
    while(i >= 1 and array[i] >= e):#loop to move to right or to left
        if array[i-1] > e:
            array[i]= array[i-1]
        elif array[i -1] < e:
            array[i]= e
        print(str(array).strip("[]").replace(",",""))
        i = i -1
    if e < array[0]:
        array[0] = e
        print(str(array).strip("[]").replace(",",""))

sort_1(array)
