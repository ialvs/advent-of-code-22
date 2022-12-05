def rearrange(quantity,stack1,stack2):

    aux1 = stack1.split()
    aux2 = stack2.split()

    for q in range(quantity):
        crate = aux1.pop()
        aux2.append(crate)

    return ' '.join(aux1), ' '.join(aux2)

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



    
