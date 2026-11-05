from nodo import Nodo


class ListaEnlazada:
    def __init__(self):
        self.p = None

    def crear_lista(self):
        print("\n--- CREACION DE LISTAS LIGADAS ---")

        dato = int(input("Introduce el primer elemento a la lista: "))
        self.p = Nodo(dato)

        t = self.p

        res = int(input("¿Desea ingresar más nodos a la lista? (1: Si, 0: No): "))

        while res == 1:
            nuevo_dato = int(input("Escribe el elemento: "))
            q = Nodo(nuevo_dato)

            t.liga = q
            t = q

            res = int(input("¿Desea agregar más nodos a la lista? (1: Si, 0: No): "))

    def mostrar_lista(self):
        print("\n--- Elementos de la lista ---")

        q = self.p

        if q is None:
            print("La lista está vacía.")
            return

        while q is not None:
            print(f"[{q.info}] -> ", end="")
            q = q.liga

        print("NIL")

    def promedio(self):
        print("\n--- Promedio de la lista ---")

        if self.p is None:
            print("La lista está vacía, no se puede calcular el promedio.")
            return

        q = self.p
        suma = 0
        contador = 0

        while q is not None:
            suma += q.info
            contador += 1
            q = q.liga

        promedio = suma / contador
        print(f"El promedio de los elementos es: {promedio:.2f}")

    def personal(self):
        print("\n--- Cantidad de elementos ---")

        q = self.p
        contador = 0

        while q is not None:
            contador += 1
            q = q.liga

        print(f"La lista contiene {contador} elemento(s).")

    def inserta_inicio(self, dato: int):
        q = Nodo(dato)  # CREAR (Q) y asignar INFORMACION
        q.liga = self.p  # Q.LIGA = P
        self.p = q  # P = Q
        print(f"Elemento {dato} insertado al inicio.")

    def inserta_final(self, dato: int):
        if self.p is None:
            self.inserta_inicio(dato)
            return

        t = self.p
        # Recorrido hasta el penúltimo (T.LIGA <> NILL)
        while t.liga is not None:
            t = t.liga

        q = Nodo(dato)
        t.liga = q  # Enlaza el último nodo al nuevo
        print(f"Elemento {dato} insertado al final.")

    def inserta_antes_de(self, dato, ref):
        q = self.p
        t = None
        band = True

        if q is None:
            return  # Validación de seguridad para lista vacía

        # Sustitución del do-while por un while estándar para seguir las convenciones de Python
        while q is not None and q.info != ref and band:
            if q.liga is not None:
                t = q
                q = q.liga
            else:
                band = False

        if band:
            # Creación del nuevo nodo
            x = Nodo(dato)

            # Inserción al principio de la lista
            if self.p == q:
                x.liga = self.p
                self.p = x
                print(f"\nElemento {dato} insertado antes del primer nodo ({ref}).")
            # Inserción en el medio o final
            else:
                t.liga = x
                x.liga = q
                print(f"\nElemento {dato} insertado antes de {ref}.")

    def inserta_despues_de(self, dato, ref):
        q = self.p  # 'self.p' representa el nodo inicial 'p'
        band = True

        # Validación básica por si la lista está vacía
        if q is None:
            return

        # Adaptación del bucle do-while original a un while convencional en Python
        while q is not None and q.info != ref and band:
            if q.liga is not None:
                q = q.liga
            else:
                band = False

        # Si se encontró el nodo de referencia (BAND sigue siendo true)
        if band:
            # Creación del nuevo nodo (equivalente a nodo T = new nodo(); T.INFO = DATO;)
            t = Nodo(dato)

            # Inserción del nuevo nodo 't' después del nodo 'q'
            t.liga = q.liga
            q.liga = t

            # Impresión del resultado (equivalente a Console.WriteLine)
            print(f"\nElemento {dato} insertado después de {ref}.")

    def eliminar_inicio(self):
        if self.p is None:
            print("No hay nodos para eliminar.")
            return

        q = self.p
        # Se verifica si la lista tiene más de un nodo
        if q.liga is not None:
            self.p = q.liga  # Se redefine el puntero al inicio
            print(f"Elemento {q.info} eliminado (quedan más nodos).")
        else:
            self.p = None  # P = NILL
            print(f"Elemento {q.info} eliminado (la lista quedó vacía).")

    def eliminar_ultimo(self):
        if self.p is None:
            print("No hay nodos para eliminar.")
            return

        if self.p.liga is None:

            print(f"Elemento {self.p.info} eliminado (la lista quedó vacía).")
            self.p = None

        else:
            q = self.p
            t = None

            while q.liga is not None:
                t = q
                q = q.liga

            t.liga = None
            print(f"Elemento {q.info} eliminado (quedan más nodos).")

    def eliminar_nodo_x(self, x):
        if self.p is None:
            print("La lista está vacía.")
            return

        q = self.p
        t = None
        band = True

        while q.info != x and band:
            if q.liga is not None:
                t = q
                q = q.liga
            else:
                band = False

        if not band:
            print("ELEMENTO NO ENCONTRADO")
        else:
            if self.p == q:
                self.p = q.liga
            else:
                t.liga = q.liga

            print(f"Elemento {x} eliminado correctamente.")

    def buscar_elemento(self, x):
        if self.p is None:
            print("La lista está vacía.")
            return

        q = self.p
        band = True

        while q.info != x and band:
            if q.liga is not None:
                q = q.liga
            else:
                band = False

        if not band:
            print(f"El elemento {x} no fue encontrado.")
        else:
            print(f"El elemento {x} está en la lista.")
