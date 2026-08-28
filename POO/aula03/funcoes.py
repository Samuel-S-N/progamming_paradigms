def notas(n1, n2):
    return(n1 + n2)/2



nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))

media = notas( nota1, nota2)

if media >= 6:
    print("Aprovado")

else:
    print("Reprovado")