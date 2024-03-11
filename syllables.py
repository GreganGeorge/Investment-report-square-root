syllables=0;
vowels='aeiouAEIOU'
name=input("Enter the file name");
sen=input("Enter the text to write to the file");
file1=open(name,'w');
file1.write(sen);
file1.close();
file2=open(name,'r');
text=file2.read();
for word in text.split():
    for vowel in vowels:
        syllables+=word.count(vowel);
    for ending in ['es','ed','e']:
        if word.endswith(ending):
            syllables-=1
    if word.endswith('le'):
        syllables+=1
print("Count of syllables : ",syllables);
