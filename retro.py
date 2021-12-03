import numpy as np
ordem = input('Qual a ordem da matriz?\n')
print('A ordem da matriz será : ' +  ordem + 'x' + ordem)
matriz = np.zeros((int(ordem),int(ordem)))
coluna = np.array([])
matrizb = np.zeros((int(ordem),1))
pivo = 0
solucao = np.zeros((int(ordem),1))

analiseAv = 0
Nula = 0
for i in range(int(ordem)):
  for j in range(int(ordem)):
     matriz[i][j] = (int(input('digite o elemento da linha '+ str(i+1)+ ' coluna ' + str(j+1)+'\n')))
print('agora preencha a matriz b')
for k in range(int(ordem)):
  matrizb[k] = (int(input('digite o elemeto da coluna ' + str(k+1) + '\n')))
for y in range(int(ordem)-1):
  pivo = matriz[y][y]
  if pivo == 0:
    print('pivo nulo')
    break
  j = i + 1
  for j in range(int(ordem)):
    cont = matriz[j][y]/pivo
    for x in range(int(ordem)):
      matriz[j][x] = matriz[j][x] - cont * matriz[y][x]
    matrizb[j] = matrizb[j] - cont * matrizb[i]
    print('multiplicador :' + str(j) + ';' + str(y) + ';')

solucao[int(ordem)-1] = matrizb[int(ordem)-1]/matriz[int(ordem)-1][int(ordem)-1]
soma = 0
for l in range(int(ordem)-2,-1,-1):
  soma = 0
  for c in range(int(ordem)):
    soma = soma + matriz[l][c] * solucao[c]
  solucao[l] = (matrizb[l] - soma)/matriz[i][i]
for n in range(int(ordem)):
  print('x['+str(n)+']'+'='+str(solucao[n]))