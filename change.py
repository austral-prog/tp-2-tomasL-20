def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)
    print(f"Ingresar gasto: \n {expense}")
    print(f"dinero recibido: \n {money}")
    print(f"Vuelto")
    print(f"Pesos:\n {pesos}")
    print(f"Centavos: \n {centavos}")


change()

