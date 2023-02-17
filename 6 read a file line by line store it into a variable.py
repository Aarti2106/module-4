#Write a Python program to read a file line by line store it into a variable.


def fileread(file):
    Vari=""
    with open(file) as data:
        for i in range(0,100):
            Vari=Vari + data.read(i)
        return Vari
print(fileread("append_data.txt"))
