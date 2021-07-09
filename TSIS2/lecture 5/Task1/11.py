import os 
size = os.stat("test.txt")
print("File size in bytes of a plain file: ", size.st_size)