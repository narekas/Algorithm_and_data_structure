# Stack Lifo

a = input('str: ')
stack = []
flVerify = True

for lt in a:
    if lt in '([{':
        stack.append(lt)
    elif lt in ')]}':
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

        flVerify = False
        break

if flVerify and len(stack) == 0:
    print('Yes')
else:
    print('No')
