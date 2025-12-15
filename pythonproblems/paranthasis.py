def is_balance(expr):
    stack=[]
    for char in expr:
        if char in ['[','}','(']:
            return False
        stack.append(char)
    else:
        if not stack:
            return False
        current_char = stack.pop()
        if current_char == '(':
            if char!='(':
                return False
        if current_char == '{':
            if char!='}':
                return False
        if current_char == '[':
            if char!=']':
                return False
    if stack:
        return False
    else:
        return True
x =is_balance("[()}{}")
print(x)



def is_balance(expr):
    stack=()
    for char inn expr:
        if char in stack:
            return False
        stack.append(char)
        else:
            if not in stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char !=')':
                    return False
            if current_char == '{':
                if char !='}':
                    return False
            if current_char == '[':
                if char !=']':
                    return False
    if stack: 
        return False
    else:
        return True
x = is_balance("[(){}]")
print(x)
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)

            