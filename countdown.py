#countdown proyect with python
import time


#cuntdown function declaration
def countdown(t):
    
    while t > 0:
        print(f"\r{'Time remaining:':^15}{str(t):>2}", end="")
        t -= 1
        time.sleep(1)
    else:
        print()
        print("we did it!!! BUMM BUMM BUMM")

#get input from the user 
t = int(input("Enter the time in seconds: "))

#call the function with the countdown
seconds = countdown(t)
