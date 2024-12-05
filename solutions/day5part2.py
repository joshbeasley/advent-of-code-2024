import re
from collections import defaultdict

def is_valid(update):
  for i in range(len(update)-1):
    for j in range(i+1, len(update)):
      if update[j] in adj[update[i]]:
        return False
  return True

def reorder(update):
  for i in range(len(update)-1):
    for j in range(i+1, len(update)):
      if update[j] in adj[update[i]]:
        update[i], update[j] = update[j], update[i]
  return update

res = 0
text =  open(0).read()
rules = re.findall(r"(\d+)\|(\d+)", text)
rules = [(int(rule[0]), int(rule[1])) for rule in rules]

updates = re.findall(r"((\d+,)+\d+)", text)
updates = [list(map(int, i[0].split(','))) for i in updates]

adj = defaultdict(list)

for rule in rules:
  adj[rule[1]].append(rule[0])

for update in updates:
  if not is_valid(update):
    res += reorder(update)[len(update) // 2]
    
print(res)