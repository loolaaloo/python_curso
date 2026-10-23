def main():
    edad = int(input("¿Cuál es tu edad?: "))
    dia = input("¿Es semana o finde?: ").lower().strip()
    descuento = input("¿Tienes credencial de estudiante?, (si/no): ").lower().strip()
    if edad < 0 or (dia != "finde" and dia != "semana") or (descuento != "si" and descuento != "no" ):
        print("error, invalid data")
    else:
        precio = calcular_precio(edad, dia, descuento)
        print(f"Tu boleto cuesta: ${precio}")


def calcular_precio(edad, dia, descuento):
    if edad < 5:
        return 0
    elif edad < 13:
        precio = 50
    elif edad < 60:
        precio = 90
    else:
        precio = 60
    if dia == "finde":
        precio += 20
    if descuento == "si" and 13<=edad<60 :
        precio -= 10
    return precio

main()