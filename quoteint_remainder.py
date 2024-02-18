
def find(dividend, divisor, start, end) :
    #If start is greater than end, it returns  (0, dividend)
	if(start>end):
	    return ( 0, dividend )

	mid = (start + end) // 2
	n = dividend - (divisor * mid)
    
	if (n > divisor):  #If n is greater than divisor, it updates start to mid + 1.
		start = mid + 1
		

	elif (n < 0):  #If n is less than 0, it updates end to mid - 1.
		end = mid - 1
		
	else :  
		if (n == divisor) : #If n is equal to divisor, it increments mid by 1, sets n to 0, and returns (mid, n) immediately.
			mid =mid+1; 
			n = 0; 
		return ( mid, n ); 
	
	return find(dividend, divisor, start, end); 

def divide(dividend, divisor) : 

	return find(dividend, divisor, 1, dividend); 

dividend = int(input("Enter your dividend: "))
divisor = int(input("Enter your divisor: "))

ans = divide(dividend, divisor); 

print("Quoteint is: {}".format(ans[0]))
print("Remainder is: {}".format(ans[1]))



