arr=list(map(int,input().split(" ")))
j=arr[0]
for i in range (1,len(arr)):
    j^=arr[i]
print(j)
