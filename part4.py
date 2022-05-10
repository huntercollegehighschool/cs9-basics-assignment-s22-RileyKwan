'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. Those two number will be the base and height of a triangle. 
The program will then output the area of that triangle. (Reminder: the area of a triangle can be calculated by (base * height)/2 ).

What should appear on the console when this code runs:

Enter the base: 8
Enter the height: 3
The area of the triangle is 12.0

'''

#start writing your code below
number=int(input("Enter a positive integer"))
if number < 0:
    number=int(input("Try again. Enter a positive integer"))
number1=int(input("Enter another positve integer"))
if number1 < 0:
   number1=int(input("Try again. Enter a positive integer"))
if number > 0 and number1 >0:
  print(("The area is", (number*number1)//2))
