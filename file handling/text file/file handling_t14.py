#read a text file and remove spaces
f = open("xyz.txt","r")
str = f.readline()
print(str , len(str))
str1 = str.strip("/n")
print(str1, len(str1))
str = f.readline()
print(str , len(str))
str1 = str.strip("/n")
print(str1, len(str1))
f.close()
