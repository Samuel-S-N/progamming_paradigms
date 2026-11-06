from functools import reduce


def filtrar_aprovados(pedidos):
    return list(
        filter(
        lambda p: p["status"] == "aprovado",
        pedidos))


def aplicar_desconto(pedidos, percentual):
    return list(
        map(
        lambda p: {**p, "valor": p["valor"] * (1 - percentual / 100)}, pedidos))


def calcular_faturamento(pedidos):
    return reduce(
        lambda acc, p: acc + p["valor"], pedidos, 0)


def pedidos_alto_valor(pedidos, valor_minimo):
    return list(
        filter(
        lambda p: p["valor"] > valor_minimo, pedidos))


def nomes_clientes(pedidos):
    return list(
        map(
        lambda p: p["cliente"], pedidos))


def processar(pedidos, operacao):
    return operacao(pedidos)


def gerar_relatorio(pedidos):
    aprovados = filtrar_aprovados(pedidos)
    return {
        "total": len(pedidos),
        "aprovados": len(aprovados),
        "bruto": calcular_faturamento(aprovados),
        "com_desconto": calcular_faturamento(aplicar_desconto(aprovados, 10)),
        "alto_valor": pedidos_alto_valor(aprovados, 500),
        "clientes": nomes_clientes(aprovados),
    }


# Dados e apresentação

PEDIDOS = [
    {"id": 1, "cliente": "Ana", "valor": 500, "status": "aprovado"},
    {"id": 2, "cliente": "Carlos", "valor": 150, "status": "pendente"},
    {"id": 3, "cliente": "Maria", "valor": 1200, "status": "aprovado"},
    {"id": 4, "cliente": "João", "valor": 80, "status": "aprovado"},
    {"id": 5, "cliente": "Fernanda", "valor": 300, "status": "cancelado"},
    {"id": 6, "cliente": "Pedro", "valor": 750, "status": "aprovado"},
]


def imprimir_relatorio(r):
    print("===== RELATÓRIO DE VENDAS =====")
    print(f"Total de pedidos: {r['total']}")
    print(f"Pedidos aprovados: {r['aprovados']}")
    print(f"Faturamento bruto: R$ {r['bruto']:.2f}")
    print(f"Faturamento com desconto: R$ {r['com_desconto']:.2f}")
    print("Pedidos de alto valor:")
    for p in r["alto_valor"]:
        print(f"- {p['cliente']}: R$ {p['valor']:.2f}")
    print("Clientes com pedidos aprovados:")
    print(", ".join(r["clientes"]))
    print("================================")


imprimir_relatorio(gerar_relatorio(PEDIDOS))

print("\n--- processar() com operações diferentes ---")
print("Aprovados:", len(processar(PEDIDOS, filtrar_aprovados)))
print("Faturamento total:", processar(PEDIDOS, calcular_faturamento))
print("Valor > 1000:", [p["cliente"] for p in processar(PEDIDOS, lambda ps: pedidos_alto_valor(ps, 1000))])
