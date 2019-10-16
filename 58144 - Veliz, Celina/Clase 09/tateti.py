from tablero import draw_tablero, win ,validate, full
#draw_tablero([" "," "," "," "," "," "," "," "," "])
numeros=[]
tablero=[]
for i in range (0,9):
    tablero.append(" ")
    numeros.append(str(i+1))
draw_tablero(numeros)
while win(tablero)==False and full(tablero)==False:
    print ("Es el turno de la X")
    valido=False
    while not valido:
        print ("Ingrese una posicion valida del 1 al 9")
        posicion=int(input())
        valido=validate(tablero,posicion)
        if not valido:
            print("Error de posicion")
    tablero[posicion -1]=numeros[posicion -1]="X"
    draw_tablero(numeros)
    gano=win(tablero)
    if gano:
        print ("Gano X")
    else:
                print ("Es el turno de la 0")
    valido=False
    while not valido:
        print ("Ingrese una posicion valida del 1 al 9")
        posicion=int(input())
        valido=validate(tablero,posicion)
        if not valido:
            print("Error de posicion")
    tablero[posicion -1]=numeros[posicion -1]="0"
    draw_tablero(numeros)
    gano=win(tablero)
    if gano:
       print ("Gano 0")
if full(tablero) and not win(tablero):
    print("Nadie gano")