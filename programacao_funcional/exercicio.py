from functools import reduce
vendas = [50, 150, 200, 80, 300]

filtradas = filter(
    lambda valor : valor > 100,
    vendas
)

com_taxa = map(
    lambda valor : valor * 1.05,
    vendas
)

com_taxa = map(
    lambda valor : valor * 1.05,
    filtradas
)

total = reduce(
    lambda acumulador, valor : acumulador + valor,
    com_taxa,
    0
)

print(f"Total: {total}")