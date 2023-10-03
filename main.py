import pygame
from pygame.locals import QUIT
import random
import math
pygame.init()
tela = pygame.display.set_mode((1000, 800))
az = (11, 32, 189)
vd = (4, 204, 17)
vm = (255,0,0)
am = (250, 200, 3)
listapalavra = ['gato', 'vaca', 'escada', 'profissão', 'nuvem', 'doce', 'maçã', 'uva', 'pirâmide', 'quadrado']
listacontador = [0,0,0,0,0,0,0,0,0,0]
listafaixas = [[az, 15], [vd, 30], [vm, 45], [am, 60]]
listacores = [az, vd, vm, am]
lista2 = []

def desenho():
  pygame.draw.rect(tela, (255,255,255), (0,0,1000,800))
  x = 500
  y = 400
  angulo = 40
  for p in listapalavra:
    for f in listafaixas:
      if p in f:
        cor = f[0]
        tamanho = f[1]
    fonte = pygame.font.Font(pygame.font.get_default_font(), tamanho)
    tt = fonte.render(p, False, (cor))
    tela.blit(tt, (x, y))
    x = math.cos(math.radians(angulo)) * len(p) * 30
    y = math.sin(math.radians(angulo)) * len(p) * 30
    angulo += 40
    x += 1000 // 2
    y += 800 // 2

for x in range(40):
  p = random.choice(listapalavra)
  lista2.append(p)
  listacontador[listapalavra.index(p)] += 1
maior = listacontador[0]
menor = listacontador[0]
for x in range (10):
  if maior < listacontador[x]:
    maior = listacontador[x]
  if menor > listacontador[x]:
    menor = listacontador[x]
tamanhofaixa = (maior - menor)

for x in range (10):
  if listacontador[x] <= tamanhofaixa/4 + menor:
    listafaixas[0].append(listapalavra[x])
  elif listacontador[x] > tamanhofaixa/4 + menor and listacontador[x] <= 2*tamanhofaixa/4 + menor:
    listafaixas[1].append(listapalavra[x])
  elif listacontador[x] > 2*tamanhofaixa/4 + menor and listacontador[x] <= 3*tamanhofaixa/4 + menor:
    listafaixas[2].append(listapalavra[x])
  else:
    listafaixas[3].append(listapalavra[x])


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    desenho()
    pygame.display.update()
