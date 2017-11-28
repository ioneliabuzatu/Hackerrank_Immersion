n  = int(input().strip())
array = [int(i) for i in input().strip().split()]

count=0
for i in range(1,n):
    item = array[i]
    position = i
    while(position > 0 and array[position-1] > item):#compare current item with its position
        array[position] = array[position-1]
        position -= 1
        array[position]=item
        count+=1#count number of shifts for every sorting step
print(count)
