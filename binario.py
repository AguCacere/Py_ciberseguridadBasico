def binario(decimal):
    binario = ""
    while decimal // 2!= 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


numero = int(input("Introduce el numero a convertir en binario: "))
print(binario(numero))