#MAP()
#map(funcao, iteravel)

from functools import reduce


precos = [100, 200, 300, 400]

def aplicar_aumento(preco):
    return preco * 1.1

novos_precos = list(map(
    lambda preco : preco * 1.1,
    precos))
print(novos_precos)

#filter()
produtos = [ 
    {"nome": "notebook", "preco": 3500},
    {"nome": "mouse", "preco": 80},
    {"nome": "teclado", "preco": 150},
    {"nome": "monitor", "preco": 900}
]

promocao = list(
    filter(
        lambda produto : produto["preco"] < 200,
        produtos
    )
)

print(promocao)

from functools import reduce
valores = [100, 200, 50, 150]
total = reduce(
    lambda acumulador, valor : acumulador + valor,
    valores,
    0
)

print(total)