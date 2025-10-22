class Arbol:
    """Clase para representar árboles binarios recursivos. La variable 'raiz'
    es un elemento, 'izquierdo' es un árbol y 'derecho' es un árbol.
    """
    def __init__(self, raiz=None, izquierdo=None, derecho=None):
        """Constructor de la clase. Si raiz es None construye un árbol binario
        vacío, en otro caso, asigna a raiz como raíz del árbol, a izquierdo
        como subárbol izquierdo, y a derecho como subárbol derecho.
        """
        if raiz is None:
            self.raiz = self.izquierdo = self.derecho = None
        else:
            self.raiz = raiz
            if izquierdo is None:
                self.izquierdo = Arbol()
            elif not isinstance(izquierdo, Arbol):
                raise TypeError("¡El subárbol izquierdo debe ser árbol!")
            else:
                self.izquierdo = izquierdo
            if derecho is None:
                self.derecho = Arbol()
            elif not isinstance(derecho, Arbol):
                    raise TypeError("¡El subárbol derecho debe ser árbol!")
            else:
                self.derecho = derecho


    def __eq__(self, arbol):
        """Compara dos árboles binarios y devuelve True si son iguales,
        False en otro caso."""
        return (self.raiz == arbol.raiz
                and self.izquierdo == arbol.izquierdo
                and self.derecho == arbol.derecho)


    def __repr__(self):
        """Representación en cadena, legible para humanos, de
        un árbol. Ejemplo:
        (10,
        (5
        (1
        ø
        ø)
        (6
        ø
        ø)))
        """
        return ""


    def es_vacio(self):
        """Devuelve True si el árbol es vacío, y False en otro caso."""
        return False


    def es_hoja(self):
        """Devuelve True si el árbol tiene un único nodo, y False en otro caso.
        """
        return False


    def copia(self):
        """Devuelve un nuevo árbol idéntico a este."""
        return Arbol()


    def num_nodos(self):
        """Devuelve el número de nodos en el árbol."""
        return 0


    def direccion(self, elemento):
        """Si elemento se encuentra en el árbol, devuelve cadena con la
        dirección (en binario) del primer nodo del árbol (en un recorrido
        in-order) que contenga al elemento.   En otro caso devuelve False.
        """
        return ""


    def gira(self, direccion):
        """Recibe como entrada una dirección dada como una cadena binaria, y gira
        (intercambia el subárbol izquierdo por el derecho) el subárbol que tiene
        como raíz al nodo con la dirección dada.  El árbol original no es
        alterado, se devuelve una copia del árbol girado.   Si la dirección no
        corresponde a un nodo del árbol, se devuelve una copia del árbol
        original.
        """
        return Arbol()


    def es_isomorfo(self, arbol):
        """Compara dos árboles binarios y devuelve True si son isomorfos,
        False en otro caso.
        """
        return False
