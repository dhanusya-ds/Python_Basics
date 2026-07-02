'''
#read the file
f= open("sample_data.txt","r")
print(f.read())

#read the 1st line

print(f.readline(), end ='')

print(f.readlines()) #as a list

print("Filename:",f.name)
print("Mode:",f.mode)
print("is closed:",f.closed)
f.close()
print("is closed:",f.closed)

#writing a file
f = open("text.txt","w") #it creates a new file
f.write("Hey Girl\n")
f.write("Looking Awesome")


#with statement

with open("sample_data.txt") as f:
    print(f.read())
    print(f.read(3)) #reading particular char


with open("sample_data.txt") as f:
    for x in f:
        print(x)

#append content to the existing file
with open("text.txt","a") as f:
    f.write("\nCool Honey")
with open("text.txt") as f:
    print(f.read())

#overwrite content    
with open("text.txt","w") as f:
    f.write("happy")
with open("text.txt") as f:
    print(f.read())

#create a sample 'abc.txt' file
f = open("abc.txt","w")

#to del a file
import os
os.remove("abc.txt")

#check the file exists or not
import os
if os.path.exists("abc.txt"):
    os.remove("abc.txt")
else:
    print("the file is not exists")

'''
#to remove a folder
import os
os.rmdir("sample_txt_f")





