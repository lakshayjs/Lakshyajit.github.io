#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lakshyajit Singh  100921673

operation = input("Enter a math operation (+, -, *, /, ^): ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if operation == "+":
    total = num1 + number2
elif operation == "-":
    total = num1 - number2
elif operation == "*":
    total = num1 * number2
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
        total = None
    else:
        total = num1 / number2
elif operation == "^":
    total = 1
    number2 = int(number2)
    for _ in range(number2):
        total *= num1
else:
    print("Invalid.")
    total = None

if total is not None:
    print("Result:", total)


# In[ ]:




