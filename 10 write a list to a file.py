#Write a Python program to write a list to a file.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
file=open('ab.txt', 'w')
for i in color:
    file.write('%s\n' % i)

print("Print Successfully")

file.close()
