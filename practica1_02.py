from enum import IntEnum

#Imprime el tablero elegante, introducción de la función actualizar tablero,
# que toma el tablero y una matriz e imprime por pantalla el tablero con los 
# carácteres correspondientes en su posición

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

class t():
    E_SupIzq = '\u250c'
    E_SupDch = '\u2510'
    E_InfIzq = '\u2514'
    E_InfDch = '\u2518'
    C_Sup = '\u252c'
    C_Inf = '\u2534'
    C_Izq = '\u251c'
    C_Dch = '\u2524'
    C = '\u253c'
    Hor = '\u2500'
    Vert = '\u2502'

def actualizarTablero(m, tablero):
    for i in range(6):
        for j in range(6):
            nuevoCar = m[i][j]
            #Elimino la posición del centro de la casilla, y escribo el nuevo carácter
            tablero[i*2+1] = tablero[i*2+1][:j*4+3]+ '' +tablero[i*2+1][j*4+4:]
            tablero[i*2+1] = tablero[i*2+1][:j*4+4]+ nuevoCar +tablero[i*2+1][j*4+4:]

def dibujarTablero(ruta, tablero):
    with open(ruta, 'r') as f:
        matriz = f.readlines()
    
    actualizarTablero(matriz, tablero);
    
    for lin in tablero:
        print(lin)

def validarJugada():
    pass

tablero = ['    1   2   3   4   5   6\n  ' + t.E_SupIzq + (t.Hor*3+t.C_Sup)*5 + t.Hor*3 + t.E_SupDch,
                'A ' + t.Vert + (' '*3 + t.Vert)*6,
                '  ' + t.C_Izq + (t.Hor*3 + t.C)*5 + t.Hor*3 + t.C_Dch,
                'B ' + t.Vert + (' '*3 + t.Vert)*6,
                '  ' + t.C_Izq + (t.Hor*3 + t.C)*5 + t.Hor*3 + t.C_Dch,
                'C ' + t.Vert + (' '*3 + t.Vert)*6,
                '  ' + t.C_Izq + (t.Hor*3 + t.C)*5 + t.Hor*3 + t.C_Dch,
                'D ' + t.Vert + (' '*3 + t.Vert)*6,
                '  ' + t.C_Izq + (t.Hor*3 + t.C)*5 + t.Hor*3 + t.C_Dch,
                'E ' + t.Vert + (' '*3 + t.Vert)*6,
                '  ' + t.C_Izq + (t.Hor*3 + t.C)*5 + t.Hor*3 + t.C_Dch,
                'F ' + t.Vert + (' '*3 + t.Vert)*6,
                '  ' + t.E_InfIzq + (t.Hor*3 + t.C_Inf)*5 + t.Hor*3 + t.E_InfDch]

dibujarTablero('PAR/Practica1/test_tab.txt', tablero)