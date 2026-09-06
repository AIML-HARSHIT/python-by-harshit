# #Program to input 2 numbers & print their sum.
a=int(input("enter the first number"))
b=int(input("enter the second number"))
sum=(a+b)
print("the sum is " ,sum)


# Program to input side of a square & print its area.
side=float(input("enter the side of the square in metres"))
area=side*side
print("the area of square is",area,"sqm")


#Program to input 2 floating point numbers & print their average.
num1=float(input("enter the first number"))
num2=float(input("enetr the second number"))
total=num1+num2
average=total/2
print("the average of",num1,"and",num2,"is",average)


# Program to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print(a>=b)


# Program to take a 3-digit number and find the sum of its digits.
num=int(input("enter a three digit number"))
a=num//100
print("first digit :-",a)
b=(num//10)%10
print("second digit:-",b)
c=num%10
print("third digit:-",c)
total=a+b+c
print("sum of the digits is :- ",total)


# Write a Python program that takes the food price as a floating-point number and calculates the final bill 
# using 5% GST and 10% sevice tax.
food_price=float(input("enter the food price"))
print("GST = 5%")
print("service tax = 10%")
gst=food_price*0.05
service_tax=food_price*0.10
bill=food_price+gst+service_tax
print("final bill :",bill)


# Swap the values of two variables
a=int(input("enter the number a "))
b=int(input("enter the number b "))
print("before swapping")
print("a:",a)
print("b:",b)
a,b=b,a
print("after swapping")
print("a:",a)
print("b:",b)

# ALTERNATIVE METHOD
a=int(input("enter the number a "))
b=int(input("enter the number b "))
print("before swapping")
print("a:",a)
print("b:",b)
x=a+b
a=x-a
b=x-b
print("after swapping")
print("a:",a)
print("b:",b)