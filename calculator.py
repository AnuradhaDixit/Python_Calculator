from art import logo


#Add
def add(n1, n2):
  return n1 + n2
  
#Subtract
def subtract(n1, n2):
  return n1 - n2
  
#Multiply
def multiply(n1, n2):
  return n1 * n2
  
#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  n1 = float(input("Enter the first number"))
  for operator in operations:
    print(operator)
  should_continue = True
  while should_continue: 
    operation_symbol = input("Pick an operation from the line above")
    n2 = float(input("Enter the second number"))
    operator_function = operations[operation_symbol]
    answer1 = operator_function(n1,n2)
    print(f'{n1} {operation_symbol} {n2} = {answer1}')
    if input(f'Type "y" to continue calculating with {answer1}, or type "n" to exit.') == "y":
      n1 = answer1
    else:
      should_continue = False
      calculator()

calculator()