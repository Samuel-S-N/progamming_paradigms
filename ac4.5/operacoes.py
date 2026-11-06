from functools import reduce


def filtrar_aprovados(pedidos):
    return list(
        filter(
        lambda p: p["status"] == "aprovado", pedidos))


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
