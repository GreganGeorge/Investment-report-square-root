a=[]
l=[]
n=int(input("Enter the number of elements in the list"))
for i in range(n):
    a.append(int(input()))
for item in a:
    if(item%2==0):
        l.append(item)
l.sort()
print("Even list is ",l)
        
