def aluno():
    print("Caio Simonassi\n1051392421012\n1º Semestre DSM")

quantNome = int(input("\nDigite quantos nomes voce deseja digitar: "))
listaNome = []
contador = 0

aluno()

while contador < quantNome:
    nome = input("\nDigite um nome: ")
    listaNome.append(nome)
    contador += 1

listaNome.sort()

print(f"Aqui estão os nomes em ordem alfabetica: {listaNome}")
