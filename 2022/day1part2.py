elfs =  open(0).read().split('\n\n')
elfs = [list(map(int, elf.split())) for elf in elfs]
elfs = [sum(elf) for elf in elfs]
print(sum(sorted(elfs)[-3:]))
