def aluno():
    print("Caio Simonassi\n1051392421012\n1º Semestre DSM")
    
quantNome = int(input("\nDigite quantos nomes de cidade voce deseja digitar: "))
listaCidade = []
contador = 0

aluno()

while contador < quantNome:
    nome = input("\nDigite o Nome de uma Cidade: ")
    listaCidade.append(nome)
    print(listaCidade)
    contador += 1
