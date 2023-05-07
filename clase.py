class Viajero:
    __NumeroViajero= ''
    __DNI= ''
    __nombre = ''
    __apellido= ''
    __millasacumuladas=int('0')
    def __init__(self,NumeroViajero='',DNI='',nombre='',apellido='',millasacumuladas=0):
        self.__NumeroViajero = NumeroViajero
        self.__DNI = DNI
        self.__nombre = nombre 
        self.__apellido = apellido 
        self.__millasacumuladas = int(millasacumuladas) 
    def __radd__(self,otro):
        self.__millasacumuladas += otro
        return otro
    def __rsub__(self,otro):
        self.__millasacumuladas -=otro
        return self
    def __gt__(self,otro):
        return self.__millasacumuladas >otro.accion1()
    def mostrarmil(self):
        return self.__millasacumuladas
    def accion1(self):
        return self.__millasacumuladas
    def accion3(self,millascanjear):
        if millascanjear <= self.__millasacumuladas:
            self.__millasacumuladas = millascanjear - self.__millasacumuladas
            print('Millas canjeadas')
        else: 
            print('No se puede canjear')
        return  
    def mostrar(self):
            print('El numero de viajero es:{}'.format(self.__NumeroViajero))
            print('El DNI es:{}'.format(self.__DNI))
            print('El nombre es: {}'.format(self.__nombre))
            print('El apellido es:{}'.format(self.__apellido))
            print('Las millas acumuladas son: {}'.format(self.__millasacumuladas))
    def verifnum(self,numero):
        if self.__NumeroViajero == numero:
            return True
    def ingreso(lista):
        numviajero = input("Ingrese un numero de viajero:")
        for i in range(len(lista)):
            if lista[i].verifnum(numviajero) == True:
                print(lista[i])
                return i
