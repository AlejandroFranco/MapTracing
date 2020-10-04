
def menu():
    print("\nPABLO ALEJANDRO FRANCO LEMUS\nLenguajes Formales y de programación\n")
    print("\n201708993\n")
    print("1. Cargar archivo")
    print("2. Graficar operación")
    print("3. salir")
    opcion = input(">>Ingrese una opción: ")
    if opcion == "1":
        print("1")
    elif opcion == "2":
        print("2")
    elif opcion == "3":
        quit()
    else:
        print("Ingrese un numero 1-3")
        menu()

menu()