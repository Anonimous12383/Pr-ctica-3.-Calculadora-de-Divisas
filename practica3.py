def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

budget = float(input("Ingrese cuanto dinero quiere cambiar: "))
exchange_rate = float(input("Ponga la tasa de cambio: "))

resultado = exchange_money(budget, exchange_rate)

print("El dinero convertido es:", resultado)