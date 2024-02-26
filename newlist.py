a=[]
l=[]
n=int(input("Enter the number of elements in the list"))
for i in range(n):
    a.append(int(input()))
value=int(input("Enter the value to check"))
for item in a:
    if(item<value):
        l.append(item)
print("New list is ",l)
