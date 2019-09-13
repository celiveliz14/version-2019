from generador import generador_mejor, generador
adivinado=False
aleatorio= generador(1,100000)
minimo=1
maximo=100
while adivinado == False:
     print ("Ingrese numero")
     numero= int (input())
     if numero == aleatorio:
         print ("Ganaste")
         adivinado=True
     if numero < aleatorio:
         print ("Es mayor")
     if numero > aleatorio:
        print ("Es menor")
     if adivinado == False:
        print ("Ahora le toca a la computadora")
        computadora=generador(minimo,maximo)
        print ("La computadora penso" + str(computadora))
        if computadora == aleatorio:
            print ("Gano la computadora")
            adivinado=True
        if computadora < aleatorio:
            minimo=computadora
        if computadora > aleatorio:
            maximo=computadora

    
    
     