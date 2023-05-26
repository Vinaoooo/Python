contador = 0
resposta = str(input("Digite sua resposta, Certa ou Errada: "))

while resposta != 'sair':
    resposta = str(input("digite outra resposta "))
    if resposta == 'certa' :
        contador = contador + 1
    if resposta == 'sair':
        print("{} respostas certas" .format(contador))


