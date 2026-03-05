def exchange_money(budget, exchange_rate):
    foreign_currency = budget / exchange_rate
    return foreign_currency

# Pruebas

# Japón
yen = exchange_money(300, 0.0075)
print("300 USD en yenes:", yen)

# México
peso_mex = exchange_money(300, 0.059)
print("300 USD en pesos mexicanos:", peso_mex)

# Colombia
peso_col = exchange_money(300, 0.00025)
print("300 USD en pesos colombianos:", peso_col)

# República Dominicana
peso_rd = exchange_money(300, 0.017)
print("300 USD en pesos dominicanos:", peso_rd)