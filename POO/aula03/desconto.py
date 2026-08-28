def calcular_desconto(valor, percentual):
    
    valor_desconto = valor - (valor * (percentual * 0.01))
    return(valor_desconto)

preco = float(input("Insira o preço original do produto: "))
desconto = float(input("Insira a % de desconto desejada: "))

print(calcular_desconto(preco, desconto))