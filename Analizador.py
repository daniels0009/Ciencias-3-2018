from pila import *
from arbol import *
import sys
import re

cuentaNumeros=0
aux = 0
pila = Pila ()
valor = []
variable = []
operador = []
tokens = {}
                
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

def verificaCaracter(lista):
    if(lista[-2].isalpha() and lista[-1]=="="):
        return True
    else:
        return False
 
def patrones(expresion):
    error = 0
    patronNum = re.compile('^[-+]?[0-9]+$')
    patronVar = re.compile('^[a-z][a-zA-Z_$0-9]*$')
    patronOpe = re.compile('[-|+|*|/|=]')
    for i in expresion:
        if(patronNum.match(i)):
            #print("Num "+ i)
            valor.append(i)
            tokens["Valor"]= valor
        elif(patronVar.match(i)):
            #print("Var "+ i)
            variable.append(i)
            tokens["Variable"]= variable
        elif(patronOpe.match(i)):
            #print("Ope "+ i)
            operador.append(i)
            tokens["Operador"]= operador
        else:
            error += 1
    return error

def ejecutar(lista):
    if lista != []:
        if (patrones(lista[0])== 0):
            if(convertir(lista[0],pila,cuentaNumeros) and verificaCaracter(lista[0])):
                print (evaluar(pila.desapilar()))
            else:
                print("Error Semantico")
            return ejecutar(lista[1:])
        else:
            print("Error de Escritura")
        return ejecutar(lista[1:])
    
    

def main ():
    listaDatos=cargarArchivo("datos.txt")
    ejecutar(listaDatos)
   
    
if __name__ == "__main__":
    main()


