l=[]
array = list(map(int,input().rstrip().rsplit()))
for i in array:
    l.append(i*i)
a= sorted(l)
for i in a:
    print(i,end=" ")