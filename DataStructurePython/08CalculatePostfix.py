def calculate(string):
    ls = []
    for element in string:
        if element.isdigit():
            ls.append(element)
        else:
            operand1 = int(ls.pop())
            operand2 = int(ls.pop())
            if element == '+':
                ls.append(operand2 + operand1)
            elif element == '-':
                ls.append(operand2 - operand1)
            elif element == '*':
                ls.append(operand2 * operand1)
            elif element == '/':
                ls.append(operand2 / operand1)
    return ls.pop()


if __name__ == "__main__":
    print(calculate("78+32+/"))
