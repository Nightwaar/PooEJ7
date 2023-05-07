from clase import Viajero
import csv
if __name__ == '__main__' :
    #viajero = Viajero(1,1,'marcos','molina',111)
    listaviajeros= []
    archivo = open('viajeros.csv')
    reader= csv.reader(archivo,delimiter=',')
    for fila in reader:
        #print(fila)
        listaviajeros.append(Viajero(fila[0],fila[1],fila[2],fila[3],fila[4]))
    for i in range(len(listaviajeros)):
        listaviajeros[i].mostrar()
    numviaj=Viajero.ingreso(listaviajeros)
    print ("1. Consultar millas ")
    print ("2. Acumular ")
    print ("3. Canjear ")
    print ("4. Mostrar el que tiene mayor cantidad de millas acumuladas ")
    opc = int(input("Ingrese opcion :")) 
    while opc !=5:
        if opc == 1:
            print("La cantidad de millas es: {}".format(listaviajeros[numviaj].accion1()))
        elif opc == 2:
            millas= int(input("Ingrese cantidad de millas a acumular")) 
            listaviajeros[numviaj]+=millas
            print(listaviajeros[numviaj].mostrarmil())
        elif opc == 3:
            millasACanjear = int(input("Ingrese la cantidad de millas a canjear "))
            listaviajeros[numviaj].accion3(millasACanjear)
            print(listaviajeros[numviaj].mostrarmil())
        elif opc == 4:
            mayor= listaviajeros[0]
            for i in range(1,len(listaviajeros)):
                mayor=listaviajeros[i] if listaviajeros[i]>mayor else mayor
            print("El que tiene mas millas acumulas es:")
            print(mayor.mostrar())
        opc = int(input("2Ingrese opcion "))