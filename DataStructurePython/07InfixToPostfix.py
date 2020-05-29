def convert(string):
    mapping = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    stack = []
    ls = []
    for element in string:
        if element.isalnum():
            ls.append(element)
        elif element == '(':
            stack.append(element)
        elif element == ')':
            operator = stack.pop()
            while operator != '(':
                ls.append(operator)
                operator = stack.pop()
        else:
            while (len(stack) != 0) and mapping[stack[-1]] > mapping[element]:
                ls.append(stack.pop())
            stack.append(element)
    while len(stack) != 0:
        ls.append(stack.pop())
    return "".join(ls)


if __name__ == "__main__":
    print(convert("a+b"))
