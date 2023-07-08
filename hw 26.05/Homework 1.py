#TASK 1 Write a program that asks the user for weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram

user_weight_kilo = input('Please enter your weight in kilograms:')
pound=2.2
user_weight_pounds=pound*int(user_weight_kilo)
print('The answer of task number 1 is \n Your weight in pouns will be: ', user_weight_pounds)

# TASK 2 Write a program that generates and prints 50 random integers, each between 3 and 6.

import random
number =0
count=0

while(number<50):
    print(random.randint(3,6))
    number+=1
    count+=1
print("The answer of task number 2 is: ", count)    

# TASK 3 Write a program that asks the user to enter two numbers, x, and y, and computes | x − y | /  x+y.

input_1= int(input('Please enter the first number:'))
input_2= int(input('Please enter the second number:'))

calculation=abs(input_1-input_2)/(input_1+input_2)
print("The answer of task number 3 is: ", calculation)

# TASK 4 A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator, determine how many leap years there have been between 1600 and that year.

const_year=1600
entered_year=int(input("Please enter a year above 1600: "))
year_range = range(const_year,entered_year+1)
is_leap_count=0
for year in year_range:
    if (year%4==0 and not year%100==0) or (year%400==0):
        is_leap_count+=1
        print(year)
print("The answer of task number 4 is: ", is_leap_count)

# TASK 5 A number is called a perfect number if it is equal to the sum of all of its divisors, not including the number itself. For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6, and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4, 7,14, 28, and 28=1+2+4+7+14. However,15 is not a perfect number because its divisors are 1, 3, 5, 15, and 15 != 1 + 3 + 5. Write a program that finds all four of the perfect numbers that are less than 10000.

for i in range(1,10000):
    div_sum=0
    for j in range(1,i):
        if i%j==0:
            div_sum+=j
    if i==div_sum:
        print("The answer of task number 5 is: ", i)