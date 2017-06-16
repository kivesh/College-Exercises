print("The leap years are :")#the header for our output
for x in range(2001,2101):#our current range is between 2001 and 2100
    if (x%4==0 and x%100!=0) or x%400==0:#it is best to search for any conditions in the problem before you actually begin to code
        print(x)
