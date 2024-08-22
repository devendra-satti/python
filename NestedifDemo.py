x=int(input("Enter a number : "))  	#Takes the input from the user 

if(x>0):	#if x>0 then control flow enters into this if loop
    print(f"{x} is positive number")		#Then it prints x is positive number
    if(x>10):	#and now if x>10 control flow enters into this if loop
        print(f"and also {x} is greater than 10")	
    else: 	#if x>0 but x < 10,then this else block will be executed
        print(f"and also {x} is less than 10")
else:		#if x<0 then this else block will be executed
    print(f"{x} is negative number")
        
