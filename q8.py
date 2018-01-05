fo = open("students.txt","r")
a=[{"name":"","roll":"","marks":""}]
a = fo.read()
dict.update(a)
#takes one line input at one time
print(a)
fo.close()
