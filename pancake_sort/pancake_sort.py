stack = [3,5,6,8,1,2,9,7,4]

def flip(ls, pos):
        return ls[:pos + 1][::-1] + ls[pos + 1:]

flips = 0
i = len(stack)
while i > 0:
    max_pos = stack.index(max(stack[:i]))
    if max_pos != i - 1:
        if max_pos != 0:
            stack = flip(stack, max_pos)
            flips += 1
        stack = flip(stack, i - 1)
        flips += 1
        i -= 1
    else:
        i -= 1

print(stack)
print(flips)