def action(char):
    if char == "+":
        summary(int(input()),int(input()))
    if char == "-":
        minus(int(input()),int(input()))
    if char == "/":
        delit(int(input()), int(input()))
    if char == "*":
        umn(int(input()),int(input()))
def summary(a, b):
    return a+b
def minus(a,b):
    return a-b
def umn(a,b):
    return a*b
def delit(a,b):
    return a/b