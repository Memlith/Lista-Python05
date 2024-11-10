def aluno():
    print("\nCaio Simonassi\n1051392421012\n1º Semestre DSM\n")
    
numero = int(input("\nDigite um numero que voce acha que esta na lista: "))
listaNumeros = [1,1,2,3,5,8,13,21,34,55,89,144,233]

aluno()

if numero in listaNumeros:
    print("\no Numero esta na lista! :)\n")
else:
    print("\no Numero NAO esta na lista! :(\n")


