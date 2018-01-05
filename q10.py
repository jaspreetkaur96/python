b=int(input("enter a num"))
a=[1,2,0,3]
try :
 for num in a :
  x=b/num
  print(x)
except ZeroDivisionError as DBZ :
  print("Division by 0 not allowed")
else :
 print(x)
