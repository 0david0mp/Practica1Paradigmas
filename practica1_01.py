from enum import IntEnum

#Abrir fichero con tablero y represntación sencilla por la consola

class Elem(IntEnum):
    VACIO = 0
    TIENDA = 1
    CASA = 2
    MANSION = 3
    EDIFICIO = 4
    HOSPITAL = 5
    BIGFOOT = 6
    BEBE = 7
    ESCUELA = 8
    UNIVERSIDAD = 9
    WICK = 10
    ESCOMBRO = 11

def dibujarTablero(ruta):
    tablero = ['  123456\n +'+'-'*6+'\n', 'A|', 'B|', 'C|', 'D|', 'E|', 'F|']

    with open(ruta, 'r') as f:
        lineas = f.readlines()
    
    print(tablero[0],end='')
    for i in range(6):
        tablero[i+1] = tablero[i+1] + lineas[i]
        print(tablero[i+1],end='')
    

def validarJugada():
    pass

dibujarTablero('PAR/Practica1/test_tab.txt')