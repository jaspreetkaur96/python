str1=input("Enter bigger string: ")
str2=input("Enter another string ")
#Taking input
x=str1.find(str2)
if ( x == -1 ) : print("string2 not found")
else : print ("string2 found at",x)
