import math

# Task 1 - calculate sum

""" num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
num3 = int(input('Enter third number:'))
if num1 == num2==num3:
    sum = 3 * (num1+num2+num3)
    print('The triple sum is',sum)
else: 
    sum =num1+num2+num3
    print('The sum is', sum) """


#Task 2 - get the difference


""" num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    diff = 2 * (num1 - num2)
else:
    diff = abs (num1 - num2)

print("The difference is:",diff) """


#Task 3 odd or even number
 
""" num = int(input('Enter the number '))

if num %2==0:
   print('The number',num,'is an even number!')
else:
   print('The number',num,'is an odd number!')  """

# Task 4

""" r = float(input('Input the radius of the circle '))
area = 3.14159 * r * r
print('Area of circle is',round(area,2)) """

# Task 5

""" guess = 6

user_input = int(input('Guess a number between i and 10 until you get it right '))

while user_input != guess:   
    user_input = int(input('Guess a number between i and 10 until you get it right '))
print('Well guessed!')    
 """
    
# Task 6 Celsius to Fahrenheit conversion
#Formula : C/5 = F-32/9, where C = temperature in Celsius and F = temperature in Fahrenheit. 
""" temp = float(input('enter a temperature '))
scale = (input('enter a shortcut for given scale (C for Celsius, F for Fahrenheit) ')).capitalize()

if scale == 'C':
    temp = round((temp *9)/5 + 32,1)
    print('The temperature in Fahrenheit is:',temp, '°F')
elif scale == 'F':
    temp = round((temp - 32) * 5/9,1)
    print('The temperature in Celsius is:',temp, '°C')

else:
    print(scale, 'is an invalid unit of measurement')    
 """

 # Task 7  pattern

""" row = 5
for i in range(0,row+1):
    for j in range(0,i+1):
      
       print('*', end='')
    print('\r')

row = 5
for i in range(row+1,0,-1):
    for j in range(0,i-1):
      
       print('*', end='')
    print('\r') """

#Task 8 Fibonacci series

x=int(input('enter a value '))

a = 0
b = 1
if x ==1:
     print(a)
else:
  print(a)
  print(b)

for i in range(2,x):
    c=a+b
    a = b
    b = c
    print(c)
