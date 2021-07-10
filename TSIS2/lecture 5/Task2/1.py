import os, sys
import os.path
import shutil
from pathlib import Path
#Your current location is disk C directory:
print(os.getcwd())


#If your current location is file you have several options:

# 1:delete file
s='test.txt'
os.remove(s)

# 2:rename file
os.rename('abc.txt','abc_changed.txt')

# 3:add content to this file
with open('test2.txt','a') as file:
    file.write("Some words ")
    #file.write(input())

# 4: rewrite content of this file
with open('test2.txt','a') as file:
    file.write("Another words ")
    #file.write(input.txt)
# 5: return to the parent directory
 #path = Path("abc.txt").parent
