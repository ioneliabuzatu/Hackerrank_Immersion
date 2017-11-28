n = int(input().strip())
array = []
for i in range(n):
    num, string = input().strip().split()
    array.append((int(num), string) if i >= n//2 else (int(num),"-"))

array.sort(key= lambda k: k[0])  # strings in their correct order
print(*[v for k,v in array])
