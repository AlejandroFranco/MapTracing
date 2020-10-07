class Trayectoria:
    # una trayectoria tiene un conjunto de estaciones, rutas y un peso del trayecto
    def _init_(self, estaciones, rutas, pesotrayecto):
        self.estaciones = estaciones
        self.rutas = rutas
        self.pesotrayecto = pesotrayecto


class Ruta:
    def _init_(self, nombre, peso, einicio, efin):
        self.nombre = nombre
        self.peso = peso
        self.einicio = einicio
        self.efin = efin


class Estacion:
    def _init_(self, nombre, estado, color):
        self.nombre = nombre
        self.estado = estado
        self.color = color


class Lector:

    def decor(self, func):
        def wrap():
            print("\nPABLO ALEJANDRO FRANCO LEMUS\nLenguajes Formales y de programación\n")
            print("\n201708993\n ")

        return wrap()

    @decor
    def menu(self):
        print("1. Cargar Archivo")
        print("2. Graficar Ruta")
        print("3. Graficar Mapa")
        print("3. salir")
        opcion = input(">>Ingrese una opción: ")
        if opcion == "1":
            analizarArchv(cargarArchivo())
            self.menu()
        elif opcion == "2":
            print("2")
        elif opcion == "3":
            quit()
        else:
            print("Ingrese un numero 1-3")
            self.menu()


def analizarArchv(contenido):
    rutas = []
    estaciones = []
    estado = 0
    lexema = ''
    for linea in contenido:
        for caracter in linea:
            if caracter == '\n':
                continue
            lexema = lexema + caracter


def cargarArchivo():
    ruta = input(">>Escriba la ruta completa del archivo: ")
    dimExt = len(ruta)
    if ruta.endswith(".txt", dimExt - 4, dimExt):
        try:
            archivo = open(ruta, "r")
            contenido = archivo.read()
            archivo.close()
            return contenido
        except FileNotFoundError:
            print("Archivo no encontrado...")
            print("\n")
            cargarArchivo()
    else:
        print("Ingrese una ruta y extensión correcta (.txt) para el archivo")
        cargarArchivo()


lector = Lector()
lector.menu()
