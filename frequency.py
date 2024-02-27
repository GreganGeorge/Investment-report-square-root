string=str(input("Enter the string"))
words=string.split()
w={}
for word in words:
    if(word not in w):
        w[word]=1
    else:
        w[word]+=1
print(w)
