# Objetivo -> Aprender a leer datos de un Excel con la librería "XLRD" y convertirlos en un Array3D
# @Author -> Carranza Balderas Enrique
# FES Aragón ICO 1358

from Array3D import Array3D
import xlrd

def Main():
    Precipitaciones = Array3D(32, 12, 35)
    print("Espere mientras los datos son leídos y transferidos a nuestra BD...")

    #Llenamos los datos leyendo uno a uno los archivos ".xls" ubicados en la carpeta "Precipitaciones".
    for ano in range(1985, 2020):
        File = xlrd.open_workbook(filename = "./Precipitaciones/" + str(ano) + "Precip.xls")
        sheet = File.sheet_by_index(0)
        for edo in range(32):
            for mes in range(12):
                Precipitaciones.set_item(edo, mes, ano-1985, sheet.cell_value(edo+2, mes+1))

    #Si no hay errores, mostramos un mensaje al usuario de que todo se hizo correctamente.
    print("¡Los datos han sido cargados a nuestra BD correctamente!, Gracias por la espera.")

    #Creamos un bucle para que mientras el usuario no presione "0", el programa siga ejecutándose.
    end = False
    
    while end != True:
        year = int(input("¿Qué año quiere consultar (1985 - 2019)?: "))

        while year < 1985 or year > 2019:
            year = int(input("\nLo sentimos, ese año no existe en nuestra BD, ¿Qué año quiere consultar (1985 - 2019)?: "))

        edo = int(input("\n¿Qué estado quiere consultar (1 - 32)?: "))

        while edo < 1 or edo > 32:
            edo = int(input("\nLo sentimos, ese estado no existe en nuestra BD, ¿Qué estado quiere consultar (1 - 32)?: "))

        month = int(input("\n¿Qué mes quiere consultar (1 - 12)?: "))

        while month < 1 or month > 12:
            month = int(input("\nLo sentimos, ese mes no existe en nuestra BD, ¿Qué mes quiere consultar (1 - 12)?: "))

        #Mostramos al usuario el dato consultado con un formato a dos decimales.
        item = "%.2f" % Precipitaciones.get_item(edo-1, month-1, year-1985)
        print(f"\n\nEl promedio mensual de lluvia es: {item}")

        #Preguntamos si desea hacer otra consulta.
        if int(input("\n¿Desea hacer otra consulta? (1.- Si 0.- No): ")) == 0:
            end = True
        else:
            print("\n\n----- ¡Comencemos de nuevo! -----")

    #Nos despedimos del usuario y termina el programa.
    print("\n\n----- ¡Hasta la próxima! -----")
    print("\nDeveloped by: DarkHawk21")

Main()
    
