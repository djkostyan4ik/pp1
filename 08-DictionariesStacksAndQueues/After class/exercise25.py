# def evaluate(expression):

#     expression = expression.split()

#     stack = []

#     operators = '/*+-='

#     for element in expression:
#         if element not in operators:
#             stack.append(int(element))
#         else:
#             a = stack.pop()
#             b = stack.pop()

#             if element == '+':
#                 stack.append(b+a)
#             elif element == '-':
#                 stack.append(b-a)
#             elif element == '*':
#                 stack.append(b*a)
#             elif element == '/':
#                 stack.append(int(b/a))

#     return stack.pop()


# arr = "2 3 +"

# answer = evaluate(arr)

# print(f"Value of given expression '{arr}' = {answer}")


import stack

list = " 0123456789+-*/"
operators = "+-*/"

isCorrect = False
while not isCorrect:
    exp = input("Expression [0-9, +, -, *, /, =]: ")

    if exp == "q":
        break

    isCorrect = True
    for i in exp[0:len(exp)-1]:
        if i not in list:
            isCorrect = False
    if not exp.endswith("="):
        isCorrect = False

for i in exp:
    if i.isnumeric():
        stack.push(int(i))
    elif i in operators:
        a = stack.pop()
        b = stack.pop()
        if i == "+":
            c = b + a
        elif i == "-":
            c = b - a
        elif i == "*":
            c = b * a
        elif i == "/":
            c = b / a
        stack.push(c)
    elif i == "=":
        end = stack.pop()

print("Result:", end)