count=0;
name=input("Enter the file name");
sen=input("Enter the sentences to write to the file");
file1=open(name,'w');
file1.write(sen);
file1.close();
file2=open(name,'r');
text=file2.read();
textlist=text.split('.');
for i in textlist:
    if(len(i)>0):
        count=count+1;
print("Number of sentences : ",count);
