from Parser import *

# get user formula to evaluate
print("Please input the expression to be evaluated: ")
# Take the input as a string
input_str = input()

# Calling function to execute program
try:
    result = parsing(input_str)
    print("We finished and the result is: ")
    print(result)
except InvalidCharacterError:
    print("An invalid character was found. Aborting.")
except InvalidNeighborError:
    print("There are two symbols or two numbers adjacent, and we don't know what to do with them. Aborting.")
except ParenthesesMismatchError:
    print("Parentheses (number of opening and closing) do not match. Aborting.")





