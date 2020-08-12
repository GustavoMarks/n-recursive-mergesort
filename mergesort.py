# Implementação de um algoritmo não recursivo de mergesort

def mergesort(vetor):
  block = 1
  n = len(vetor)
  while block < n:
    i1 = 0
    i2 = block
    while i2 < n:
      outputvetor = join(vetor[i1:i2], vetor[i2:(i2 + block)])
      # sobrescrevendo vetor original
      i = 0
      x = i1
      while x < i2 + block and i < len(outputvetor) :
        vetor[x] = outputvetor[i]
        i = i + 1
        x = x + 1
      i1 = i2 + block
      i2 = i1 + block
    block = block * 2
  return vetor

# Função auxliar para comparação de elementos
def join(vetor1, vetor2):
  i = 0
  j = 0
  outputvetor = []
  while i < len(vetor1) and j < len(vetor2):
    if vetor1[i] < vetor2[j]:
      outputvetor.append(vetor1[i])
      i = i + 1
    else:
      outputvetor.append(vetor2[j])
      j = j + 1
  
  if(i < len(vetor1)):
    for x in range (i, len(vetor1)):
      outputvetor.append(vetor1[x])

  if(j < len(vetor2)):
    for x in range (j, len(vetor2)):
      outputvetor.append(vetor2[x])
  return outputvetor
