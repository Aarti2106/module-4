
#Write a Python program to read first n lines of a file.

n=int(input("enter the number :"))
f=open("file.txt","r")
for i in range(n):
      print(f.readline())
