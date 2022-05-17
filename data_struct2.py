'''
Esta implementacion es para un problema de un puzzle lineal.
Ejemplo: [4,2,3,1] 
Estado objetivo : [1,2,3,4]

Para llegar al estado objetivo se hace uso de 3 operadores.
Operador_D = Intercambiar las dos piezas de la derecha
Operador_C = Intercambiar las dos piezas centrales.
Operador_I = Intercambiar las dos piezas de la izquierda.

[2,1,4,3] -> [1,2,4,3]  Operador_I
[1,2,4,3] -> [1,2,3,4]  Operador_D

Ejemplo con arbol BFS:

                                       [3,1,2,4]
                D                         C                              I
            [3,1,4,2]                  [3,2,1,4]                      [1,3,2,4]
      D       C        I          D        C        I             D          C        I  
[3,1,2,4]  [3,4,1,2]  [1,3,4,2]  [3,2,4,1] [3,1,2,4] [2,3,1,4]  [1,3,4,2]  [1,2,3,4]   [3,1,2,4]
 
 En este caso, falta expandir un nivel de profundidad hasta que revise el estado objetivo
 que se encuentra en d=2, por cuestiones de espacio no se realiza d=3.

'''

from numpy import DataSource


class Nodo:
    def __init__(self,datos,hijos=None):
        self.datos = datos 
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)
    '''
    set_hijos(hijos): Asigna al nodo la lista de hijos que son pasados como parametro
    '''
    def set_hijos(self,hijos):
        self.hijos = hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self

    def get_hijos(self):
        return self.hijos
    
    def get_padre(self):
        return self.padre
    
    def set_padre(self,padre):
        self.padre = padre
    
    def set_datos(self,datos):
        self.datos = datos
    
    def get_datos(self):
        return self.datos
    
    def set_coste(self,coste):
        self.coste = coste
    
    def get_coste(self):
        return self.coste
    
    '''
    igual(nodo): Devuelve true si el dato contenido en el nodo es igual al nodo pasado como parametro
    '''
    def igual(self,nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    '''
    en_lista(lista_nodos): Devuelve True si el dato contenido en el nodo es igual a alguno
    de los nodos contenidos en la lista de nodos pasada como parametro.
    '''
    def en_lista(self,lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista
    
    def __str__(self) -> str:
        return str(self.get_datos())


def buscar_solucion_BFS(estado_inicial,solucion):
    solucionado = False
    nodos_visitados=[]
    nodos_frontera = [] #Estos son los nodos que visitaremos, en grafos una frontera son los child

    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo=nodos_frontera.pop(0) #Extraemos el nodo
        nodos_visitados.append(nodo) #Lo añadimos a la lista de visitados
        if nodo.get_datos() == solucion:
            #Solucion encontrada
            solucionado = True
            return nodo #Encontró solucion
        else:
            #EXPANDIR NODO
            dato_nodo = nodo.get_datos()

            #Operador_I
            hijo = [dato_nodo[1],dato_nodo[0],dato_nodo[2],dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            nodos_frontera.append(hijo_izquierdo)

            #Operador_C
            hijo =[dato_nodo[0],dato_nodo[2],dato_nodo[1],dato_nodo[3]]
            hijo_central = Nodo(hijo)
            nodos_frontera.append(hijo_central)

            #Operador_D
            hijo = [dato_nodo[0],dato_nodo[1],dato_nodo[3],dato_nodo[2]]
            hijo_der = Nodo(hijo)
            nodos_frontera.append(hijo_der)

            nodo.set_hijos([hijo_izquierdo,hijo_central,hijo_der])



if __name__ == "__main__":
    estado_inicial = [4,2,3,1]
    solucion = [1,2,3,4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial,solucion)

    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    #resultado.append(estado_inicial)
    #resultado.reverse()
    print(resultado)


    