# Implementação de um algoritmo não recursivo de mergesort

def mergesort(vetor):
  block = 1
  n = len(vetor)
  while block < n:
    i1 = 0
    i2 = block
    while i2 < n:
      join(vetor[i1:i2], vetor[i2:(i2 + block)])
      i1 = i2 + block
      i2 = i1 + block
    block = block * 2
  return vetor

# Função auxliar para comparação de elementos
def join(vetor1, vetor2):
  print(vetor1)
  print(vetor2)
  print('join...')
