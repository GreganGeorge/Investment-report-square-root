l1=[]
l2=[]
l3=[]
n1=int(input("Enter the number of elements in list 1"))
print("Enter the elements")
for i in range(n1):
    l1.append(int(input()))
n2=int(input("Enter the number of elements in list 2"))
print("Enter the elements")
for i in range(n2):
    l2.append(int(input()))
for i in l1:
    if i in l2:
        l3.append(i)
print("Common list is ",l3)
