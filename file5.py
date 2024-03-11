syllables=0;
sent=0;
w=0;
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
sentence=text.split('.');
for i in sentence:
    if len(i)>0:
        sent=sent+1;
for sen in text.split('.'):
    for word in sen.split():
        w=w+1;
print("sentences : ",sent,"words : ",w)
index=206.835-1.015*(w/sent)-84.6*(syllables/w)
level=round(0.39*(w/sent)+11.8*(syllables/w)-15.59)
print("The Flesch index is ",index);
print("The Grade Level Equivalent is ",level);
    
