from ListaEnlazada import ListaEnlazada

if __name__ == "__main__":

    lista1 = ListaEnlazada()
    op = -1

    while op != 0:
        print("\n--- Operaciones sobre listas ligadas ---")
        print("1: Crear Lista")
        print("2: Mostrar Lista")
        print("3: Promedio de la lista")
        print("4: Personal")
        print("5: Insertar al Inicio")
        print("6: Insertar al Final")
        print("7: Insertar antes de nodo X")
        print("8: Insertar despues de nodo X")
        print("9: Eliminar primer nodo")
        print("10: Eliminar último nodo")
        print("11: Eliminar nodo con información X")
        print("12: Busqueda de elemento")
        print("0: Salir")

        try:
            op = int(input("\nElige una opcion: "))

            match op:
                case 1:
                    lista1.crear_lista()

                case 2:
                    lista1.mostrar_lista()

                case 3:
                    lista1.promedio()

                case 4:
                    lista1.personal()

                case 0:
                    print("Adios")

                case 5:
                    dato = int(input("Dame un número para insertarlo al inicio: "))
                    lista1.inserta_inicio(dato)

                case 6:
                    dato = int(input("Dame un número para insertarlo al final: "))
                    lista1.inserta_final(dato)

                case 7:
                    dato = int(input("Dame un número para insertarlo antes de otro: "))
                    ref = int(input("Dame el número de referencia: "))
                    lista1.inserta_antes_de(dato, ref)

                case 8:
                    dato = int(
                        input("Dame un número para insertarlo después de otro: ")
                    )
                    ref = int(input("Dame el número de referencia: "))
                    lista1.inserta_despues_de(dato, ref)

                case 9:
                    lista1.eliminar_inicio()

                case 10:
                    lista1.eliminar_ultimo()

                case 11:
                    x = int(input("Dame el número a eliminar: "))
                    lista1.eliminar_nodo_x(x)

                case 12:
                    x = int(input("Dame el número a buscar: "))
                    lista1.buscar_elemento(x)

                case _:
                    print("Opción no válida")

        except ValueError:
            print("Por favor, ingresa un valor numérico.")
