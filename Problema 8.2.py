"""
Problema 8.2
Se tiene un archivo de texto de palabras separadas por un blanco o el carácter de fin
de línea. Escribir un programa para formar una lista enlazada con las palabras del
archivo. Una vez formada la lista, se pueden añadir nuevas palabras o borrar alguna
de ellas. Al finalizar el programa, escribir las palabras de la lista en el archivo.

Pág.289, del libro "Estructura de datos" (Luis Joyanes Aguilar, Ignacio Zahonero Martínez, 2008)
"""

# clase Nodo la cual tienen el método constructor con las variables "dato" y la variable que tiene el apuntador
# al "siguiente" nodo de la lista.
class Nodo:

    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


# Está la clase de la lista enlazada que tiene las operaciones de agregar datos al frente o agregarlos al final,
# además el de eliminar e imprimir listas.
# Para el manejo de del archivo txt también se incluyeron 2 métodos uno para leer los datos y otro para guardarlos
class listaEnlazada:
    def __init__(self):
        self.cabeza = None

    # MÉTODOS DE LA LISTA ENLAZADA

    # Este método inserta un elemento a la lista por la parte del frente que la contiene la variable
    # cabeza la cual es igual al la clase Nodo (donde se usa la variable dato) y al apuntador al siguiente nodo
    def agregarFrente(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)

    # Método para agregar elementos al final de la lista
    def agregarFinal(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato=dato)
            return
        aux = self.cabeza
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = Nodo(dato=dato)

    # Método para eliminar nodos, este método lo que hace es buscar el elemento que se le indica
    # eliminar esto lo hace a través de un ciclo while, un if y elif. Mientras la variable aux (que es igual a
    # la cabeza de la lista) y "aux.dato" que tiene los valores de la lista sean diferentes al elemento que queremos
    # eliminar, una nueva variable llamada previo(por ser el nodo previamente evaluado por el while)
    # guardara el valor de la variable "aux" y luego le indicara que apunte al siguiente nodo en la lista.
    # A continuación entra en acción el if que evalua si la variable "previo" es None: la cabesa tendra
    # a la variable "aux" apuntando al siguiente nodo, de lo contrario el elemento "previo" es igual al elemento
    # "aux" siguiente. Lo que hace es mirar un nodo más adelante del que tiene enfrente y de ser el nodo
    # que busca lo eliminara, esto se hace asi porque al no ser una lista doblemente enlazada no se puede
    # retroceder nodos por lo que se tiene que ir mirando uno más por delante.
    def eliminar(self, elemento):
        aux = self.cabeza
        previo = None
        while aux and aux.dato != elemento:
            previo = aux
            aux = aux.siguiente
        if previo is None:
            self.cabeza = aux.siguiente
        elif aux:
            previo.siguiente = aux.siguiente
            aux.siguiente = None

    # este método lo que hace es imprimir todos los nodos de la lista a través de un ciclo while que
    # evalua si el nodo(la cabeza) es diferente de None lo imprimirá y hará que el nodo apunte al siguiente
    # asi continuamente hasta que la condición del while se romperá y termina el ciclo
    def ImprimirLista(self):
        nodo = self.cabeza
        while nodo != None:
            print(nodo.dato, end=" => ")
            nodo = nodo.siguiente

        return nodo

    # MÉTODOS SOBRE LEER Y GUARDAR LOS DATOS DEL ARCHIVO
    # Este método lee las palabras que están en el archivo.txt abre el txt usando la dirección que
    # está en la variable archivo, luego usando un ciclo for itera cada línea en el archivo separando el
    # texto y haciendo una multilista. El siguiente for se encarga de separar esa multilista en palabras
    # separadas, pero en una unica lista, posteriormente en la variable cabeza se guarda palabra por palabra
    # (como un nuevo nodo) con "línea" como dato y el apuntador siguiente
    def leerDatos(self, archivo):
        palabra = []
        with open(archivo) as archivo:
            for linea in archivo:
                palabra.extend(linea.split())
            for linea in palabra:
                linea.replace(' ', '\n')
                self.cabeza = Nodo(dato=linea, siguiente=self.cabeza)
            return palabra

    # Este método se encarga de guardar la lista enlazada de palabras que han sido modificadas ya sea
    # eliminando o agregando elementos segun se necesite. Primero abre un nuevo archivo en modo escritura "w"
    # después con un for itera los datos que contenga la variable "entrada", hace uso de "range" que inicia en 0
    # hasta la cantidad de lementos que contenga "entrada" (que los cuenta usando la función "len") por
    # último escribe elemento por elemento en la variable "archivo" y cierra mismo.
    def guardarDatos(self, entrada):
        archivo = open("datos.txt", 'w')
        archivo.write('')
        for f in range(0, len(entrada)):
            linea = str(entrada[f][:]) + '\n'
            archivo.write(linea)
        archivo.close()


# Instancia
s = listaEnlazada()
archivo = s.leerDatos("datos.txt")

print("\n----------------lista-Enlazada-Se-agrega-HOLA-al-inicio-y-ADIOS-al-final--y-se-elimina-la-palabra"
      "-destornillador------------------------------")
print("\n")

# se usan los métodos de una lista enlazada para modifcar las palabras del archivo
s.agregarFrente("HOLA")
s.agregarFinal("ADIOS☺")
s.eliminar("destornillador") # la palabra a eliminar depende del texto que exista en datos.txt
s.ImprimirLista()

# para guardar la lista en el archivo datos.txt
s.guardarDatos(archivo)

