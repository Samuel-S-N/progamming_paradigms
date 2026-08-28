doadornome = str(input("Nome doador: "))
alimentosdoados = int(input("Quantidade de alimentos recebidos: "))
metacampanha = int(input("Meta da campanha: "))

print(alimentosdoados)

if alimentosdoados >= metacampanha:
    print("Meta Atingida")
else:
    print(f"Ainda faltam {metacampanha - alimentosdoados} para bater a meta")