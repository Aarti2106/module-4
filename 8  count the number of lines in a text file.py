
#Write a Python program to count the number of lines in a text file.

f=open("append_data.txt","r")
lst=f.readlines()

print("No Of Line Are :",len(lst))
f.close()

print("-------------------------------")


with open("file2.txt","r")as f:
    lst=f.readlines()
print("No Of Line Are :",len(lst))
    
