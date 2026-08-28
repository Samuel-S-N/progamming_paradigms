list_nomes = []

for i in range (3):
    nome = str(input("Insira o nome do voluntário: "))
    list_nomes.append(nome)

idade = int(input("Insira a idade do voluntário: "))
hrs_trabalho = int(input("Insira a quantidade de horas de trabalho do voluntário: "))


print(f"{nome}\n {idade}\n {hrs_trabalho}")

print(list_nomes)