# Tarea 2.- Imprimir en sentido contrario el contenido de una cadena usando while.
# @Author - Carranza Balderas Enrique
# 1358 - Estructura de Datos

sentence = "Work hard and get it all, it's not time to give up!"

position = len(sentence)-1

while position >= 0:
    print sentence[position],
    position -= 1

print("\n\nDeveloped by: DarkHawk21")
