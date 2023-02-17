#Write a python program to find the longest words.

f=open("file2.txt","r")
s=f.read()
lst=s.split()
#max words
print(max(lst,key=len))
#min words
print(min(lst,key=len))

