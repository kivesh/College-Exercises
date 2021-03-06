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
    
#Prac5Q2-Patterns
rows = int(input("Please enter the amount of rows"))
spaces = rows-1
for x in range(rows):
    stars = x+1
    print(" "*spaces, end="")
    print("*"*stars)
    spaces = spaces- 1
    
    #Prac5Q3-Patterns
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

    #Prac5Q4-Patterns
rows = int(input("Please enter the number of rows"))
for x in range(rows,0,-1):
    for i in range(1,x+1):
        print(i, end="")
    print()
    
 #Prac5Q5-Patterns
lines = int(input("The number of lines needed "))
numOfSpaces = lines -1 
for x in range(1,lines+1):
    stars = (2*x)-1
    print( " "*numOfSpaces, end="")
    print("*"* stars, end="")
    numOfSpaces -=1    
    print()

#Prac5Q6-Patterns
lines = int(input("enter the number of lines"))
spaces = (lines-1)*2
num =1 
for x in range(1,lines+1):
    rangeLp = (2*x)-1
    print(" "*spaces,end="")
    for x in range(rangeLp):
        print(num,end=" ")
        num+=1
    spaces-=2
    print()

#Prac6Q1 
num=0
num = int(input("Enter a number"))
sumNum =0
stillCalc = True
def calcSumNum():
    while num!=0:
        digit = num %10
        sumNum = digit+sumNum
        num = num//10
        
    if sumNum>19:
            num = sumNum
            sumNum =0
    else:
            stillCalc = False
calcSumNum()
while stillCalc == True:
    calcSumNum()
if sumNum%3==0:
    print("The number is divisible by three")
else:
    print("Not divisivble")
    
    
#Prac6Q2
oddAbundant= False
number=12
while oddAbundant == False:
    sumAbundant= 0
    for x in range(1,number):
        if number%x==0 :
                    sumAbundant += x 
    if(sumAbundant>number):
        print(number)
        if not(number%2==0):
            oddAbundant=True
    number+=1    

   
#Prac6Q3
number = int(input("Enter a number"))
countFactors =0
for x in range(1,number+1):
    if number%x==0:
        countFactors+=1
if countFactors ==2:
    print("The number is a prime number")
   
#Prac6Q4
A = int(input("enter positive integer 1 "))
B = int(input("enter positive integer 2 "))
sumPrime =0
for x in range(A+1,B):
    factors = 0
    for i in range(1,x+1):
        if x%i==0:
            factors+=1
    if factors==2:
        sumPrime = x+sumPrime
print("The sum of all the primes between " ,A, " and " , B ," is ", sumPrime)

#Prac7Q1
def celsiusToFarenheit(tempInCelsius):
    farenheit = (9.0/5)*tempInCelsius + 32#fahrenheit = (9.0 / 5) * celsius + 32
    return farenheit
def farenheitToCelsius(tempInFarenheit):
    celsius = (tempInFarenheit-32)/(9.0/5)
    return celsius

print("Celsius\tFarenhiet")
for x in range(40,30,-1):
    x = x+0.00
    print(x,"\t",celsiusToFarenheit(x))
print("")    
print("Farenheit\tCelsius")
for x in range(120,20,-10):
    x = x +0.00
    print(x,"\t", farenheitToCelsius(x))
    
    
#Prac7Q2
num = int(input("enter a integer"))
displayNum = num
def reduceNum(numParam):
    num = numParam    
    sumNum =0
    while sumNum>19 or sumNum ==0:
        sumNum =0
        while num!=0:
            digit = num%10
            sumNum = digit +sumNum
            num = num//10
        num = sumNum
    return sumNum
sumF = reduceNum(num)
if sumF%3==0:
    print(displayNum," is divisible by three ")
    
#Prac7Q3
num = int(input("enter a number"))
def sumOfFactors(numParam):
    num = numParam
    sumFactors =0
    for x in range(1,num):
        if num%x ==0:
            sumFactors = num + sumFactors
    return sumFactors
sumFacs = sumOfFactors(num)
if sumFacs>num:
    print(num, "is abundant")
elif sumFacs <num:
    print(num, "is deficient")
else:
    print(num, "is proper")
    
    
#Palindromes
string = input("enter a string to check if it is a palindome: ")
newString = string.replace(" ","")
perfectString = ""
for char in newString:
    if char.isalpha() or char.isdigit():#remove punctuation
        perfectString = perfectString+char
perfectString = perfectString.lower()
        
reverseString = "" 
for pos in range(1,len(perfectString)+1):
    reverseString = reverseString+perfectString[pos*-1]

if reverseString == perfectString:
    print("It a palindrome!!!!!!!")
    
#count consonants
string = input("Enter a string: ")
consanant = input("Enter the consonant to be counted: ")
def howmany(st,c):
    count =0
    for char in st:
        if char ==c:
            count+=1
    return count
print("The number of occurences of the consonant is ", howmany(string, consanant))   

#remove spaces and punctuation
string = input("enter a string")
newString = ""
for char in string:
    if char.isdigit() or char.isalpha():
        newString = newString + char
print(newString)

#Add strings in their unicode numbers.
string = input("enter a string")
sumChar =0
for char in string:
    num = ord(char)-68
    sumChar= num +sumChar
print("The converted string is: ", sumChar)

import random
string = input("enter a string")
position = []
positions = random.randint(0,len(string)-1)
position.append(positions)
print(position)
newString = string(positions)

def positionInList(rand):
    for x in position:
        if x == rand:
            return false
        else:
            return true
for x in range(len(string)-2):
    positions = random.randint(0,len(string)-1)   
    while positionsInList(positions):
        positions = random.randint(0,len(string)-1)
    position.apend(positions)    
    newString = newString + string[positions]
print(newString)

