x = float(input("purchase:"))
y = float(input("sale:"))
z = (y/x) - 1
w = (z)*100
print(f"Profit in %: {w}%")

net_profit = (z*x)
print(f"profit in $: $ {net_profit}")

gross_billing = (z*x) + x
print(f"gross billing: $ {gross_billing}")
