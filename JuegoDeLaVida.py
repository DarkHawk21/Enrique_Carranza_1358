# Juego de la vida
# - Juego del tipo "zero-players"
# - Creado por el inglés John Conwry en 1970
# - Simula el acceso, caida, y alternancia de seres vivos.

# Reglas
# - Si una célula que se encuentra viva tiene 0 o un vecino, muere por soledad para la siguiente generación. Donde los vecinos son las 8 celulas que lo rodean inmediatamente.
# - Una célula viva que tiene dos o tres vecinos, sobrevive para la siguiente generación.
# - Una célula viva que tiene 4 o más vecinos, muere por sobrepoblación para la siguiente generación.
# - Una célula muerta con exactamente 3 vecinos vivos, resulta en un nacimiento cuya vida empieza en la siguiente generación. Todas las demás células muertas permanecen muertas para la siguiente generación.
# @Author -> Enrique Carranza Balderas
from Array2D import Array2D

class JuegoDeLaVida:
    def __init__(self, rows, cols, generaciones, poblacion_inicial):
        self.__cuadro = Array2D(rows, cols)
        self.__filas = rows
        self.__columnas = cols
        self.__generaciones = generaciones
        self.__cuadro.clearing(0)
        for cell in poblacion_inicial:
            self.__cuadro.set_item(cell[0], cell[1], 1)

    def to_string(self):
        self.__cuadro.to_string()

    def configure_next_gen(self, nueva_generacion):
        self.__cuadro.clearing(0)
        for cell in nueva_generacion:
            self.__cuadro.set_item(cell[0], cell[1], 1)

    def set_cell_death(self, row, col):
        self.__cuadro.set_item(row, col, 0)

    def set_cell_alive(self, row, col):
        self.__cuadro.set_item(row, col, 1)

    def is_live_cell(self, row, col):
        if self.__cuadro.get_item(row, col) == 1:
            return True
        else:
            return False

    def get_num_live_neighborns(self, row, col):
        limites = self.calcula_vecinos(row, col)
        cont = 0
        for fila in range(limites[0], limites[2] + 1, 1):
            for cols in range(limites[1], limites[3] + 1, 1):
                if fila == row and cols == col:
                    pass
                else:
                    if self.is_live_cell(fila, cols):
                        cont += 1
        return cont

    def calcula_vecinos(self, y, x):
        #[y_ini, x_ini, y_fin, x_fin]
        vecinos = [y-1, x-1, y+1, x+1]
        if vecinos[0] == -1:
            vecinos[0] == 0
        if vecinos[1] == -1:
            vecinos[1] == 0
        if vecinos[2] == self.__filas:
            vecinos[2] == self.__filas - 1
        if vecinos[3] == self.__columnas:
            vecinos[3] == self.__columnas - 1
        return vecinos

#Pruebas
def main():
    inicial = [[1,2],[2,1],[2,2],[2,3]]
    juego = JuegoDeLaVida(20,20,4,inicial)
    juego.to_string()
    for r in range(5):
        for c in range(5):
            print(f"[{r}][{c}] = {juego.get_num_live_neighborns(r,c)}")
            
main()
