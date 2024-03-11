name=input("Enter the file name");
sen=input("Enter the sentence to write");
file1=open(name,'w');
file1.write(sen);
file1.close();
file2=open(name,'r');
text=file2.read();
print(text);
file2.close();
