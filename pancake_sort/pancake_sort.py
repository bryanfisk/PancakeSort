stack = [3,5,6,8,1,2,9,7,4]
sorted_stack = sorted(stack)

def flip(ls, pos):
        return ls[:pos + 1][::-1] + ls[pos + 1:]

def find_max_out_of_place(ls):
        sorted_list = sorted(ls)[::-1]
        ls = ls[::-1]
        for index, x in enumerate(ls):
                if sorted_list[index] != x:
                        return len(ls) - index - 1

flips = 0
while stack != sorted_stack:
    max_out = find_max_out_of_place(stack)
    stack_index = stack.index(sorted_stack[max_out])
    stack = flip(stack, stack_index)
    if stack_index == 0:
        pass
    else:
        flips += 1
    stack = flip(stack, max_out)
    flips += 1

print(flips)

