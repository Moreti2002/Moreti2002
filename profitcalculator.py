x = float(input("purchase:"))
y = float(input("sale:"))
z = (y/x) - 1
w = (z)*100
print(f"Profit in %: {w}%")

profit_in_money = (z*x)
print(f"profit in $: $ {profit_in_money}")

money_after_profit = (z*x) + x
print(f"Dinheiro final: $ {money_after_profit}")
