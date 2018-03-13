from pila import *
from arbol import *

cuentaNumeros=0
aux = 0
pila = Pila ()

def errorLexico(self,pos):
    #lista1[pos-1]=">>"+lista1[pos-1]+"<<"
    return("Error en la siguiente posicion")
        
def convertir(lista, pila,cuentaNumeros):
    if lista != []:
        if lista[0] in "+-*/=":
            if pila.es_vacia() != True:
                nodo_der = pila.desapilar()
            else:
                return False
            if pila.es_vacia() != True:
                nodo_izq = pila.desapilar()
            else:
                return False
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
            cuentaNumeros=0
        else:
            if cuentaNumeros<2:
                pila.apilar(Nodo(lista[0]))
                cuentaNumeros=cuentaNumeros+1
            else:
                return False
        return convertir(lista[1:],pila,cuentaNumeros)
    return True

def evaluar(arbol):
    if arbol.valor == "=":
        resultado =arbol.der.valor+ "=" +str(evaluar(arbol.izq))
        return resultado
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

def cargarArchivo(nombre):
    archivo = open(nombre,"r")
    lista =[]
    for linea in archivo.readlines():
        expresion=linea.split(" ")
        lista.append(expresion[:-1])
    return lista

def main ():
    listaDatos=cargarArchivo("datos.txt")
    if(convertir(listaDatos[0],pila,cuentaNumeros)):
        print evaluar(pila.desapilar())
   
    
if __name__ == "__main__":
    main()
