# Program to input user’s first name & print its length.
name=str(input("enter your name"))
print(len(name))


# WAP to find the occurrence of ‘$’ in a String.
name=str(input("enter your name"))
print(name.find("$"))


# Program to check if a number entered by the user is odd or even.
num=int(input("enter the number"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")


# Username validitor
name=input("enter username")
if len(name)==8:
    if name.count("@")==1:
        print("VALID USERNAME")
else:
    print('INVALID USERNAME')


# Middle Character Challenge prints middle of 
string=str(input("enter your string"))
length=len(string)
if length%2==0:
    print(string[length//2:length//2+2])
else:
    print(string[length//2])


# Password Strength Checker
password=input("enter the password")
if len(password)>=8 and password.find("@") != -1:
    print("strong password")
elif len(password)>=6:
    print("medium password" )
else:
    print("weak password")

# Program to find the Smallest and Greatest of all numbers 
a=float(input("enter the  first number"))
b=float(input("enter the second number"))
c=float(input("enter the third number"))
if a>b and a>c :
    print("Greatest number is :-",a)
elif b>a and b>c:
    print("Greatest number is :-",b)
elif c>a and c>b:
    print("Greatest number is :-",c)
    if a<b and a<c :
        print("Smallest number is :-",a)
    elif b<a and b<c:
        print("Smallest number is :-",b)
    elif c<a and c<b:
        print("Smallest number is :-",c)
else:
    print("all numers are equal")

# String analyst 
sentence=str(input("enter any sentence"))
print("number of characters in string :",len(sentence))
print("number of occurence of a :",sentence.count("a"))
print("first index of a :",sentence.find("a"))
print("capitalized :",sentence.capitalize())


# assign grades according to marks
marks=float(input("enter your marks"))
if marks>=90:
    print("A Grade")
elif marks>=80:
    print("B Grade")
elif marks>=70:
    print("C Grade")
elif marks>=60:
    print("D Grade")
else:
    print("E Grade")

if marks>=40:
    print("PAAS")
else:
    print("FAIL")


#Multiple operations with a three digit numbers
num=int(input("enter a three digit number"))
str_num=str(num)
if len(str_num)==3:
    a=num//100
    b=(num//10)%10
    c=num%10
    sum=a+b+c
    print("sum:",sum)
    if sum%2==0:
        print("the sum is even")
    else:
        print("sum is odd")
    if sum%3==0:
            print("the sum is divisible by three")
    else:
            print("the sum is not divisible by three")

else:
    print("it is not a three digit number")

# program to check the first and last character of a string are samee
string=str(input("enter any string"))
if string[0]==string[-1]:
    print("the first and last character of the string are same")
else:
    print("the first and last character of the string are NOT same")