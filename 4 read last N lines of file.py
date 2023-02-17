#Write a Python program to read last n lines of a file.
n=int(input("enter the number :"))
f=open("file.txt")
for i in (f.readlines()[-n:]):
      print(i,end="")
