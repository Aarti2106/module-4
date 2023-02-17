#Write a Python program to read first n lines of a file.

n = int(input("\n\t\tEnter Lines To Read : "))
f = open("my_fileWrite a Python program to read last n lines of a file..txt","r")
for i in range(n):
	print(f.readline())

