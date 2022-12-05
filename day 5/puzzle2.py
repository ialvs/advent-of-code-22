def rearrange(quantity,stack1,stack2):
    stack_as_list = stack1.split() 
    stack_as_list2 = stack2.split() 
    removed_list = []
    reversed_removed_list = []
    
    for q in range(quantity):
        crate = stack_as_list.pop()
        removed_list.append(crate)

    for removed_item in reversed(removed_list):
        reversed_removed_list.append(removed_item)
    
    for item in reversed_removed_list:
        stack_as_list2.append(item)
    
    return ' '.join(stack_as_list), ' '.join(stack_as_list2)

with open('crates.txt') as crates:
    stacks = crates.readlines()

with open('input.txt') as input:
    lines = input.readlines()

print(stacks)

x = 1

for line in lines:
    quantity = int(line.split()[1])
    stack1 = stacks[int(line.split()[3]) - 1]
    stack2 = stacks[int(line.split()[5]) - 1]
    #print('exec ',x)
    stacks[int(line.split()[3]) - 1],stacks[int(line.split()[5]) - 1] = rearrange(quantity,stack1,stack2)
    x += 1
    #print('fim exec ',x)

for stack in stacks:
    out = stack.split()
    print(out[-1])
