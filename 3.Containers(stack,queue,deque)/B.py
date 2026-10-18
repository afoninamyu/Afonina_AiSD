def psp(s):
    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
            continue
        if len(stack) != 0 and (c == ")" and stack[-1] == "(" or c == "]" and stack[-1] == "[" or c == "}" and stack[-1] == "{"):
            stack.pop()
        else:
            return "no"
    if not stack:
        return "yes"
    return "no"

s = input()
print(psp(s))