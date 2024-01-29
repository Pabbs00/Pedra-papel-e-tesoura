import random

escolhas = ["Pedra", "Papel", "Tesoura"]


def linha(texto):
  print("="*(len(texto)))

def limpar_tela():
  print("\033c", end="")

def tela():
  texto_2 = "Escolha uma das opções abaixo (Digite o número correspondente):"
  texto = "Seja Bem Vindo(a) ao Pedra, Papel e Tesoura !"
  linha(texto_2)
  print(texto.center(len(texto_2)))
  linha(texto_2)
  print(texto_2)

def opções():
  for x in range(len(escolhas)):
    print(f"{x+1} - {escolhas[x]}")
  print("4 - Sair")
  print("="*30)

def escolha():
  escolha = int(input("Digite sua escolha: "))
  return escolha

def jogar():
  resultado = random.randint(1,2)
  if resultado == 1:
    print("Você Perdeu!")
  else:
    print("Você Ganhou!")
  