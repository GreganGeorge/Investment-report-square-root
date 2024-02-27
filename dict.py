dict1={'k1':'v1','k2':'v2','k3':'v3'}
dict2={}
for i in dict1:
    dict2[dict1[i]]=i
print("New dictionary is",dict2)
