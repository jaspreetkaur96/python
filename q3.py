#if ( a > b )
#	if ( a > c ) : print "A is the greatest"
#	else : print " C is the greatest"
#if ( b > c ) : print " B is greater"  
import sys
list=[]
list=sys.argv[1:]
list.sort()
print(list[2])
