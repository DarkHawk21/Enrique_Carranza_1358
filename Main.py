# @Author -> Carranza Balderas Enrique
# Grupo -> 1358 FES Aragón

from JuegoDeLaVida import JuegoDeLaVida

def main():
    #Preguntamos al usuario el tamaño de un lado del cuadrado en el que generaremos las impresiones para así sacar filas y columnas.
    lado = int(input("¿Cuantas casillas tendrá de ancho su cuadrado generador?: "))

    #Preguntamos al usuario cuantas generaciones quiere que genere la computadora
    gen = int(input("¿Cuántas generaciones quieres que te muestre el juego?: "))

    #Preguntamos al usuario cuantas células vivas habrá en la población inicial.
    pob_ini = int(input("¿Cuántas células vivas habrá en la población inicial?: "))

    #Generamos una población inicial con los valores que el usuario introduce en el programa.[[1,3],[2,2],[2,3],[2,4]]
    print("Ahora vamos a introducir las posiciones de la población inicial de células vivas una a una.")
    print("\n ----- Posiciones iniciales -----")
    generacion_inicial = []

    for item in range(pob_ini): #Pedimos los valores iniciales al usuario.
        rowP = int(input(f" Fil{item} = "))
        colP = int(input(f" Col{item} = "))
        generacion_inicial.append([rowP, colP])

    #Instanciamos la clase Juego de la Vida creando una nueva llamada game.
    game = JuegoDeLaVida(lado, lado, gen, generacion_inicial)

    #Imprimimos en pantalla la primera generación.
    print("\n ----- Generación inicial -----")
    game.to_string()
    print(" Población:", len(generacion_inicial)) #Número de células vivas.

    #Imprimimos las generaciones recorriendo una por una.
    for generacion in range(2, gen+1):
        nueva_generacion = [] #Almacenará la configuración generada después de verificar celda por celda y encontrar el número de celulas que seguirán vivas.
        print("\n\n ----- Generación", generacion, "-----")

        #Recorremos las filas del cuadrado.
        for row in range(lado):
            #Recorremos las columnas del cuadrado.
            for col in range(lado):
                vecinos = game.get_num_live_neighborns(row, col) #Obtenemos los vecinos vivos de la célula acual.

                #Si la célula actual está viva, entonces vemos cuantos vecinos tiene, si son 2 o 3 sigue viva para la siguiente generación.
                if game.is_live_cell(row, col):
                    if vecinos == 2 or vecinos == 3:
                        nueva_generacion.append([row, col]) #Anexamos la configuración a la lista de vivos.
                else: #Si la célula actual está muerta, entonces vemos cuantos vecinos tiene, si son 3 entonces nace para la siguiente generación.
                    if vecinos == 3:
                        nueva_generacion.append([row, col]) #Anexamos la configuración a la lista de vivos.

        game.configure_next_gen(nueva_generacion) #Anexamos el arreglo de configuración generado al cuadrado de la nueva generación.
        game.to_string() #Imprimimos la nueva generación.
        print(" Población:", len(nueva_generacion)) #Imprimimos el número de células vivas en la generación actual.

    print("\n Developed by: DarkHawk21")
main() #Invocamos el método main del archivo para su funcionamiento.
