print("The leap years are :")#the header for our output
for x in range(2001,2101):#our current range is between 2001 and 2100
    if (x%4==0 and x%100!=0) or x%400==0:#it is best to search for any conditions in the problem before you actually begin to code
        print(x)
#Prac4 Q1
print("Miles \t Kilometers")#format of output
for x in range(1,11):
     miles = x*1.609#simple data conversions
     print(x," \t ", miles)

#Prac4 Q2
import math
n=0
nSquared = n*n#incrementing n squared to n*n
while nSquared < 30000:#condition
    n = n+1
    nSquared = n*n
squareNumLess = math.sqrt(nSquared)-1#since n squared will be the square greater than 30000 we need the square root of it then subtract 1
print("The largest number n such that n**2 is less than 30000 is", squareNumLess)

#Prac4 Q3
mark = int(input("Please enter a mark "))# the input statement should be entered on the top in case of no marks
high1= -1# mark are always greater than -1
high2= -1
sum=0
count=0
while mark!= -1:#when a mark is equal to -1 it will terminate
    sum += mark#adding sum
    count+= 1
    if mark>high1:# high1 will be the first value entered then compare the next
        high1 = mark
       
    if mark>high2 and mark< high1:# to be the second highest number it must be smaller than high2 and greater than the initial instantiation of -1
        high2 = mark
       
       
    mark = int(input("Please enter a mark "))#the input statement is better suited at the end of the loop because the loop will terminate with no further calculation done
avgMark = sum/count
print("The highest mark is ", high1)
print("The second highest mark is ", high2)
print("The average of the marks is ", avgMark)

#Prac4 Q4
number = (int)(input("Please enter a number"))#input statement
factor = number #factor then refers to the value of number
while factor>0:# this condition specifies that the conditon is decreasing
    if number%factor==0:#for a number to be a factor it must be a divisor of the number
        print(factor, end=" ")#special output format this changes the setting of the print statement to not start in a new line but rather leave a space and then start there
    factor-=1

#Prac4 Q5
number = (int)(input("Please enter a number "))#input a number
sumDivisors = 0# since a perfect number is equal to it divisors we increment a sum variable
for x in range(1,number+1):#range function is quite unique it start at the first number min and ends at max -1 so we must add 1 to our upper limit
    if number%x ==0:#for x to be a divisor it must result in no remainder
        sumDivisors += x
if number== sumDivisors:#if the sum of divisors is equal to the number, then the number is a perfect number
    print(number, " is a perfect number")
   
#Prac4 Q6
num1 = (int)(input("Please enter num 1 "))#input statement
num2 = (int)(input("Please enter num 2 "))#input statement
if num1< num2:#the gcd can never be bigger than the smallest of the two number so this is our range
    numRange = num1
else:
    numRange = num2
gcd= 0
for x in range(1, numRange+1):#we run a loop from 1 to the smallest of the two numbers
    if num1%x==0 and num2%x==0:# if x is a divisor of num1 and num2 we place it int the variable gcd
      gcd = x
print("The greated common divisor is ", gcd)
           
#Prac4 Q7
#this is the first series of the program
sumSeries1 = 0
for n in range(1,50):#analysis of the first series shows it has a range 1-49
    numerator = 2*n -1#a split up the terms into numerator and denominators for easier representation
    denominator = 2*n +1
    term = numerator/denominator
    sumSeries1 += term# i then added the the term to the sum of the series
print("The sum of series 1 is ", sumSeries1)
#this is the second series of the program
import math# math.sqrt is used for this series but their are alternatives like math.pow(num,0.5) ansd expontiation *0.5
sumSeries2 =0
for n in range(1,625):#analysis of this series shows it has a range 1-625
    numerator = 1
    denominator = math.sqrt(n)+ math.sqrt(n+1)
    term = numerator/denominator
    sumSeries2 += term # i then added the the term to the sum of the series
print("The sum of series 2 is ", sumSeries2)
 
#Prac4 Q8
i = int(input("Please enter a value for i "))# this value determine how many times we will iterate
sumSeries= 0# using this variable we will add all the terms
import math
for x in range(i,i+1):
    numerator = math.pow(-1,x+1)# fraction representation(numerator/denominator allows us to isolate different mathematical functions
    denominator = 2*i -1
    term = numerator/denominator
    sumSeries += term
pi = 4* sumSeries#finally the series states that all terms should be multiplid by 4
print("The approximation of pi is ", pi)

#some basic functions__________________________________________________________________________________________________________________
def get_sales(employee_number,total_number_of_employees):       
    if employee_number==1:
        sales = float(input("Enter the monthly sales for the first employee:"))
        main(sales)         
    elif employee_number==total_number_of_employees:
        sales = float(input("Enter the monthly sales for the Last employee:"))
        main(sales)
    else:
        sales = float(input("Enter the monthly sales for the NEXT employee OR enter 0 to exit:"))
        if sales ==0:
            print("Goodbye")
        else:
            main(sales)
    return sales

def get_advanced_pay():
    advancedPay = float(input("Enter the amount of advancedpay, or enter 0 if no advanced was given "))
    return advancedPay

def determine_comm_rate(sales):
    if sales <10000:
        commissionRate = 10/100
    elif sales >= 10000 and sales < 15000:
        commissionRate = 12/100
    elif sales >= 15000 and sales < 18000:
        commissionRate = 14/100
    elif sales >= 18000 and sales <22000:
        commissionRate = 16/100
    else:
        commissionRate = 18/100
    return commissionRate

def calculate_pay(sales, comm_rate , advance_pay):
    pay = sales*comm_rate - advance_pay
    return pay

def willReimburseCompany(pay):
    if pay<0:
        return True
    else:
        return False
   
def main(sales):  
   
    advance = get_advanced_pay()
    commission = determine_comm_rate(sales)
    print("Advanced pay:", advance)
    pay =  calculate_pay(sales, commission, advance)
    print("The pay is: R", pay)
    if willReimburseCompany(pay):
        print("The salesperson must reimburse the company")
    print("")
totalNumberOfEmployees = int(input("Enter the number of employees you want to run their pay:"))
for x in range(1,totalNumberOfEmployees+1):
    employeeNumber=  x
    sales=  get_sales(employeeNumber,totalNumberOfEmployees)
    if sales ==0:
        break
        
#____________________________________________________________________________________________________________________________

#Prac5Q1-Patterns
rows = (int)(input("Please enter the amount of rows "))
for x in range(rows):
    stars = x+1    
    print("*"*stars)
    
#Prac5Q2
rows = int(input("Please enter the amount of rows"))
spaces = rows-1
for x in range(rows):
    stars = x+1
    print(" "*spaces, end="")
    print("*"*stars)
    spaces = spaces- 1
    
    #Prac5Q3
num = int(input("PLease enter the number"))
spaces = num-1
for row in range(1,num+1):
    #spaces from the heading is incorrect
    print(" "*spaces*2, end="")
    for LHS in range(row,0,-1):
        print(LHS, end=" ")
    for RHS in range(2,row+1):
        print(RHS,end=" ")
    spaces -=1 
    print()
