n  = int(input().strip())
array = [int(i) for i in input().strip().split()]


for i in range(1,n):
    item = array[i]
    position = i
    while position > 0 and array[position-1] > item:#compare current item with its position
        array[position] = array[position-1]
        position -= 1
    array[position]=item
    print( " ".join( repr(e) for e in array ) )
   
