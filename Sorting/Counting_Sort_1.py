n=int(input().strip())
ar=list(map(int, input().split()))

count = [0] * 100              # init with zeros
for a in ar:
    count[a] += 1            # count occurences
print(*count)        
   
        
