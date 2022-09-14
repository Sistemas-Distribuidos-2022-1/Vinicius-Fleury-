from random import randint
from time import sleep
import sys
import os

lista = []
dormir_c = False #desativar/ativar onsumidor
dormir_p = False #flag para desativar/ativar produtor
length_max = int(sys.argv[1]) 

def produtor():
 global lista, length_max, dormir_c, dormir_p

 if not dormir_p: #verifica se processo está ativo
  while len(lista) < length_max: #verifica se a lista não atingiu seu tamanho máximo
   lista.append(randint(0, 1000)) #adiciona um valor inteiro entre 0 e 1000 à lista
   print 'Olá Sr. Programador eu sou o produtor, olha como está a lista de valores ' + str(lista)
  else:
   print 'Fiz o meu serviço olha como eu deixei a lista cheinha >>> ' + str(lista)
   print 'Agora eu vou tirar uma soneca. [Produtor está tirando uma soneca acorde ele quando a lista estiver vazia] \n'
   dormir_p = True #desativa o processo A
   dormir_c = False #ativa o processo B
   consumidor() #chama o consumidor
   
def consumidor():
 global lista, length_max, dormir_c, dormir_p

 if not dormir_c: #verifica se processo está ativo
  if lista: #verifica se a lista contem valores
   del lista[0] #remove o valor que se encontra no inicio da lista
   print 'Olá Sr. Programador eu sou o consumidor, olha como está a lista de valores' + str(lista)
  else:
   print 'Fiz o meu serviço olha como eu deixei a lista limpinha >>> ' + str(lista)
   print 'Agora eu vou tirar uma soneca. [Consumidor está tirando uma soneca, acorde ele quando a lista possuir valores] \n'
   dormir_c = True #desativa o processo B
   dormir_p = False #ativa o processo A
   produtor() #chama o produtor

while True: #loop infinito
 produtor() 
 consumidor()
 print 