 #Universidad Nacional Autónoma de México
 #Facultad de Ciencias
 #Licenciatura en Ciencias de la Computación
 #Estructuras Discretas 
 #Practica5
 #Escrito por: Hernandez Vazquez Diego y Bruno Bernardo Soto Lugo
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
        def _repr(nodo, indent):
            if nodo.es_vacio():
                return indent + "ø"
            # línea de la raíz
            s = indent + "(" + str(nodo.raiz) + "\n"
            # representación del izquierdo con mayor indentación
            s += _repr(nodo.izquierdo, indent + "  ") + "\n"
            # representación del derecho con mayor indentación
            s += _repr(nodo.derecho, indent + "  ") + ")"
            return s

        return _repr(self, "")


    def es_vacio(self):
        """Devuelve True si el árbol es vacío, y False en otro caso."""
        # Regresa True si el árbol no tiene ningún elemento (raiz = None, izquierdo = None, derecho = None).
        # Segun el constructor, si raiz = None, entonces izquierdo y derecho también lo son.
        # Asi, solo se checa si raiz = None.
        return self.raiz is None


    def es_hoja(self):
        """Devuelve True si el árbol tiene un único nodo, y False en otro caso.
        """
        # Verifica si los dos hijos, derecho e izquierdo, son vacios.
        # De ser asi, es una hoja.
        # Tambien verificamos que el arbol no sea completamente vacio para evitar una excepcion.
        return not self.es_vacio() and self.derecho.es_vacio() and self.izquierdo.es_vacio()

    def copia(self):
        """Devuelve un nuevo árbol idéntico a este."""
        # Si el arbol es completamente vacio, o sea, no tiene ningun elemento,
        # regresa un arbol sin nada.
        if self.es_vacio():
            return Arbol()
        # Crear un nuevo arbol sin elementos.
        # nuevo_arbol = Arbol()
        # La raiz de este nuevo arbol sera la misma.
        # nuevo_arbol.raiz = self.raiz
        # En los nodos derecho e izquierdo se aplica el caso recursivo, al ser
        # estos arboles tambien.
        # nuevo_arbol.derecho = self.derecho.copia()
        # nuevo_arbol.izquierdo = self.izquierdo.copia()
        ## OPTIMIZACION DE CODIGO
        # Se regresa un arbol con la misma raiz, y los casos recursivos en derecha e izquierda.
        return Arbol(self.raiz,self.izquierdo.copia(),self.derecho.copia())

    def num_nodos(self):
        """Devuelve el número de nodos en el árbol."""
        # Si un nodo ya es vacio (no existe), regresar 0.
        if self.es_vacio():
            return 0
        else:
        # De otro modo regresar 1 (el nodo actual) mas los casos recursivos en
        # izquierda y derecha.
            return 1 + self.derecho.num_nodos() + self.izquierdo.num_nodos()


    def direccion(self, elemento):
        """Si elemento se encuentra en el árbol, devuelve cadena con la
        dirección (en binario) del primer nodo del árbol (en un recorrido
        in-order) que contenga al elemento.   En otro caso devuelve False.
        """
        def _helper(nodo, path):
            if nodo.es_vacio():
                return False
            # Va de orden -> izquierdo, raiz, derecho
            left = _helper(nodo.izquierdo, path + "0")
            if left is not False:
                return left
            if nodo.raiz == elemento:
                return path
            right = _helper(nodo.derecho, path + "1")
            if right is not False:
                return right
            return False

        return _helper(self, "")



    def gira(self, direccion):
        """Recibe como entrada una dirección dada como una cadena binaria, y gira
        (intercambia el subárbol izquierdo por el derecho) el subárbol que tiene
        como raíz al nodo con la dirección dada.  El árbol original no es
        alterado, se devuelve una copia del árbol girado.   Si la dirección no
        corresponde a un nodo del árbol, se devuelve una copia del árbol
        original.
        """
        copia = self.copia()
        # Si el árbol es vacío o la copia es vacía
        # regresamos la copia sin cambios
        if copia.es_vacio():
            return copia

        # Si la dirección es la cadena vacía
        # giramos la raíz del árbol
        if direccion == "":
            copia.izquierdo, copia.derecho = copia.derecho, copia.izquierdo
            return copia

        nodo = copia
        for bit in direccion:
            if bit == "0":
                # ir a la izquierda
                if nodo.izquierdo.es_vacio():
                    # dirección inválida -> devolver
                    return copia
                nodo = nodo.izquierdo
            elif bit == "1":
                # ir a la derecha
                if nodo.derecho.es_vacio():
                    return copia
                nodo = nodo.derecho
            else:
                # carácter inválido -> devolver
                return copia

        # Si llegamos a un nodo válido giramos
        # sus hijos intercambiándolos
        if nodo.es_vacio():
            return copia
        nodo.izquierdo, nodo.derecho = nodo.derecho, nodo.izquierdo
        return copia

    def es_isomorfo(self, arbol):
        """Compara dos árboles binarios y devuelve True si son isomorfos,
        False en otro caso.
        """
        # Si ambos arboles son vacios, son isomorfos
        if self.es_vacio() and arbol.es_vacio():
            return True
        # Si uno de los dos es vacio, no son isomorfos
        if self.es_vacio() or arbol.es_vacio():
            return False
        # Si las raíces no coinciden, no pueden ser isomorfos
        if self.raiz != arbol.raiz:
            return False
        # Checar si los subarboles izquierdo y derecho son isomorfos
        return ((self.izquierdo.es_isomorfo(arbol.izquierdo) and
                 self.derecho.es_isomorfo(arbol.derecho)) or
                (self.izquierdo.es_isomorfo(arbol.derecho) and
                 self.derecho.es_isomorfo(arbol.izquierdo)))
