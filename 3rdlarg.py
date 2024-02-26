a=[]
n=int(input("Enter the number of elements in the list"))
for i in range(n):
    a.append(int(input()))
a.sort()
print("Third largest element is ",a[-3])
