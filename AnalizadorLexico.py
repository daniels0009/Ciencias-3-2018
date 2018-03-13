
# - * - codificación: cp1252 - * -
clase Pila: #Clase pila
    def __init __ (self):
        self.items = []

    def apilar (self, x):
        self.items.append (x)

    def desapilar (self):
        tratar:
            return self.items.pop ()
        excepto IndexError:
            elevar ValueError ("La pila está vacía")

    def es_vacia (self):
        return self.items == []

clase Nodo (): # clase arbol
    def __init __ (self, val, izq = None, der = None):
        self.valor = val
        self.izq = izq
        self.der = der
        
#Esta función convierte la lista, en una pila.
def convertir (lista, pila):
    si lista! = []:
        si lista [0] en "+ - * /": # evalúa los operadores
            nodo_der = pila.desapilar () # Desapila debido a la posfija
            nodo_izq = pila.desapilar () # Desapila debido a la posfija
            pila.apilar (Nodo (lista [0], nodo_izq, nodo_der)) # apila arbol
        elif lista [0] en "0123456789":
            imprimir ("entra")
            valor = lista [0]
            pila.apilar (Nodo (valor [0]))
        elif lista [0] en "=":
            variable = pila.desapilar (). valor
            variables [variable] = [evaluar (pila.desapilar ())]
            print (variable + "=" + str (variables [variable] [0]))
        más:
            pila.apilar (Nodo (lista [0])) # apila nodos
        return convertir (lista [1:], pila) #recursividad
    
#Esta función resuelve el árbol           
def evaluar (arbol):
    si arbol.valor == "+":
        return evaluar (arbol.izq) + evaluar (arbol.der)
    si arbol.valor == "-":
        return evaluar (arbol.izq) - evaluar (arbol.der)
    si arbol.valor == "/":
        return evaluar (arbol.izq) / evaluar (arbol.der)
    si arbol.valor == "*":
        return evaluar (arbol.izq) * evaluar (arbol.der)
    return int (arbol.valor)
    
def main ():
    lista = []
    Pila = Pila ()
    archivo = abrir ('datos.txt', 'r')
    para linea en archivo.readlines ():
        expresion = linea.split ("")
        lista.append (expresion)
    archivo.close ()
    convertir (lista [0], pila)
   
    
si __name__ == "__main__":
    principal()
