x = float(input("Compra:"))
y = float(input("Venda:"))
z = (y/x) - 1
w = (z)*100
print(f"Lucro em %: {w}%")

lucro_em_dinheiro = (z*x)
print(f"Lucro em R$: R$ {lucro_em_dinheiro}")

dinheiro_final = (z*x) + x
print(f"Dinheiro final: R$ {dinheiro_final}")
