#Write a Python program to copy the contents of a file to another file.
f1=open("ab.txt","r")
f2=open("copy.txt","w")

s=f1.read()
f2.write(s)

f1.close()
f2.close()

