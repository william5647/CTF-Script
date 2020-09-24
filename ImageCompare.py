with open('./kitters.png', 'rb') as f:
  kitters = f.read()

with open('./cattos.png', 'rb') as f:
  cattos = f.read()

flag = ''
for i in range(min(len(kitters), len(cattos))):
  if kitters[i] != cattos[i]:
    flag += cattos[i]
print flag
