from operacoes import (
    calcular_faturamento, filtrar_aprovados, gerar_relatorio, pedidos_alto_valor, processar,
)

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
