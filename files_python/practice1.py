myfile = open("file.txt")

content = myfile.read()
myfile.close()

with open("file1.txt") as myfile1:
    content1 = myfile1.read()
    myfile1.close()
with open("test1.txt", "a") as myfile2:
    write1 = myfile2.write("Lima\nHyo\nHvca\nIca\nArequipa")
    myfile2.close()
with open("test1.txt", "r") as myfile3:
    content2 = myfile3.read()
    myfile3.close()

print(content)
print(content1)
print(content2)
"""
==== Character Meaning ========

'r' open for reading (default)
'w' open for writing the file first
'x' Create a new file and open it for writing
'a' open for writing, appending to the end of the file if it exits
"""
