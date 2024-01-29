import configurações

while True:
  configurações.limpar_tela()
  configurações.tela()
  configurações.opções()
  escolha = configurações.escolha() 
  if escolha == 4:
    configurações.limpar_tela()
    break
  elif escolha in [1,2,3]:
    configurações.jogar()
    i = input("Deseja jogar novamente? (s/n): ")
    if i == "n":
      configurações.limpar_tela()
      break
    else:
      pass