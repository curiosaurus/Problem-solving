arr=list(map(int,input().split(" ")))
dic={}
for i in arr:
	if str(i) not in dic.keys() :
		dic[str(i)]=1
	else:
		dic.pop(str(i))
print (list(dic)[0])
