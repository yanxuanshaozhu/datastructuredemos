def brutalForce(brackets):
    # If the string is ""
    if brackets == "":
        return True
    stack = []
    dt = {')': '(', '}': '{', ']': '['}
    for ele in brackets:
        if ele in dt.values():
            stack.append(ele)
        # When ele is a right bracket but no left brackets in the stack, or the two mismatch.
        elif len(stack) == 0 or dt[ele] != stack.pop():
            return False
    return len(stack) == 0


if __name__ == "__main__":
    inputBrackets = input("Enter a string of brackets")
    print(brutalForce(inputBrackets))
