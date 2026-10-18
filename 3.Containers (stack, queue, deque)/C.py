s = input().split()
stack = []
for c in s:
    if not c.isnumeric():
        b = stack.pop()
        a = stack.pop()
        if c == "+":
            stack.append(a+b)
        elif c == "-":
            stack.append(a-b)
        else:
            stack.append(a*b)
    else:
        stack.append(int(c))
print(stack[0])