def fact(n) :
 if ( n== 1 ) or ( n == 0 ) :
  fac=1
  return fac
 else :
  return n*fact(n-1)

n=int(input("enter number"))
x=fact(n)
print(x)
