n = int(input().strip())
new_list=[]
for i in range(n):
    x = input()
    new_list.append(x)
print("\n".join(sorted(new_list,key=int)))#go trought the list, after you join them all and sort it
