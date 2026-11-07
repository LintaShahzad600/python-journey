#- Ask the user for two numbers and an operator.
#- Use separate functions for each operation, or one function that handles the selected operation.
#- Reject invalid operators and non-numeric input.
#- Handle division by zero.
#- Create test_calculator.py to test the calculations.
#Revision: int(), float(), if/elif/else, functions, try/except, raise, pytest.

def cal(a,b,op):
    
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
       return a/b

def main():
    
   try:
       a=int(input(print("Enter 1 no")))
       b=int(input(print("Enter 2 no")))
       op=str(input(print("Enter an operator +,-,*,/")))
       result=cal(a, b, op)
       print("Your Calculated value is",result)
   except ZeroDivisionError:
       print("Error: Division by zero is not allowed.")
   except ValueError:
       print("Error: Please enter valid numbers and operator.")