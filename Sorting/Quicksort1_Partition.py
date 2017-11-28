n =int(input().strip())
arr = [int(x) for x in input().strip().split(' ')]
if len(arr) <= 1:
    print (arr)
else:
    print(" ".join(str(x) for x in arr if x < arr[0]), arr[0], " ".join(str(x) for x in arr if x > arr[0]))
    
