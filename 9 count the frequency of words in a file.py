#Write a Python program to count the frequency of words in a file.
f=open("data.txt","r")
wrd=input("Enter The Word :")

s=f.read()
lst=s.split()
count=0
for i in lst:
    if(i==wrd):
        count+=1
print("Word {} Occurred {} Time".format(wrd,count))
