import argparse

parser= argparse.ArgumentParser()
parser.add_argument("number1", help="first number")
parser.add_argument("number2", help="second number")
parser.add_argument("operation", help="operation")

args= parser.parse_args()
print(args.number1)
print(args.number2)
print(args.operation)

n1=int(args.number1)
n2=int(args.number2)
op=args.operation
result=None

if op=="add":
  result=n1+n2
elif op=="subtract":
  result=n1-n2
elif op=="multiply":
  result=n1*n2

print("result is:", result)