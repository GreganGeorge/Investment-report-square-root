d1={}
d2={}
l=[]
n1=int(input("Enter the number of key value pairs in the first dictionary"))
for i in range(n1):
    key=int(input("Enter the key"))
    value=int(input("Enter the value"))
    d1[key]=value
n2=int(input("Enter the number of key value pairs in the second dictionary"))
for i in range(n2):
    key=int(input("Enter the key"))
    value=int(input("Enter the value"))
    d2[key]=value
for item1 in d1:
    for item2 in d2:
        print(item1,item2)
        if(item1==item2):
            l.append(item1)
print("Common keys are ",l)
    

