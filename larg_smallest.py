a=[]
n=int(input("Enter the total numbers in the list"))
for i in range(n):
    a.append(int(input()))
print("Largest number is ",max(a))
print("Smallest number is ",min(a))
