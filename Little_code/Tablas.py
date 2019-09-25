# @Objetive: Generate a program with FOR that prints the multiplication tables from 1 to 10.
# @Author: Enrique Carranza Balderas
# School: UNAM - FES Aragón
# Subject: Estructuras de datos
# Group: 1358 - 2020-1

for tabla in range(1,11,1) :
    print("----- TABLA DE MULTIPLICAR DEL ", tabla, " -----")

    for fila in range(1,11,1) :
        print(tabla, " x ", fila, " = ", tabla * fila)

    print()

print("Developed by: DarkHawk21")
        
