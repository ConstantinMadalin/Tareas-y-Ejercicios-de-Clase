import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class Trabajador:
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, numero_colegiado=None):
        self.nif = nif
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        self.sexo = sexo
        self.numero_colegiado = numero_colegiado

class Medico(Trabajador):
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, especialidad, fecha_inicio, numero_colegiado):
        super().__init__(nif, nombre, fecha_nacimiento, sexo, numero_colegiado)
        self.especialidad = especialidad
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")

    def calcular_anios_trabajados(self):
        return datetime.now().year - self.fecha_inicio.year

class Enfermera(Trabajador):
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, area, personas_a_cargo):
        super().__init__(nif, nombre, fecha_nacimiento, sexo)
        self.area = area
        self.personas_a_cargo = personas_a_cargo

    def modificar_personas_a_cargo(self, cantidad):
        self.personas_a_cargo += cantidad

class Hospital:
    def __init__(self):
        self.trabajadores = []

    def anadir_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)

    def guardar_datos_csv(self, nombre_fichero):
        datos = []
        for trabajador in self.trabajadores:
            if isinstance(trabajador, Medico):
                datos.append([trabajador.nif, trabajador.nombre, trabajador.fecha_nacimiento.strftime("%Y-%m-%d"), trabajador.sexo,
                              trabajador.especialidad, trabajador.fecha_inicio.strftime("%Y-%m-%d"), trabajador.numero_colegiado, "", ""])
            elif isinstance(trabajador, Enfermera):
                datos.append([trabajador.nif, trabajador.nombre, trabajador.fecha_nacimiento.strftime("%Y-%m-%d"), trabajador.sexo,
                              "", "", "", trabajador.area, trabajador.personas_a_cargo])

        columnas = ["NIF", "Nombre", "FechaNacimiento", "Sexo", "Especialidad", "FechaInicio", "NumeroColegiado", "Area", "PersonasACargo"]
        df = pd.DataFrame(datos, columns=columnas)
        df.to_csv(nombre_fichero, index=False)

    def cargar_datos_csv(self, nombre_fichero):
        df = pd.read_csv(nombre_fichero)
        return df  

def generar_grafica(df):
    
    if 'PersonasACargo' in df.columns:
        df['PersonasACargo'].dropna().plot(kind='hist', bins=10, color='red', edgecolor='black')
        plt.title("Distribución de Personas a Cargo de las Enfermeras")
        plt.xlabel("Personas a Cargo")
        plt.ylabel("Frecuencia")
        plt.show()

def main():
    hospital = Hospital()

    while True:
        print("\nGestión de los trabajadores del hospital")
        print("1. Añadir trabajador")
        print("2. Guardar datos en .csv")
        print("3. Cargar datos de .csv")
        print("4. Mostrar gráfica")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de trabajador (médico/enfermera): ").lower()
            nif = input("NIF: ")
            nombre = input("Nombre: ")
            fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
            sexo = input("Sexo: ")

            if tipo == "médico":
                especialidad = input("Especialidad: ")
                fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                numero_colegiado = input("Número de colegiado: ")
                medico = Medico(nif, nombre, fecha_nacimiento, sexo, especialidad, fecha_inicio, numero_colegiado)
                hospital.anadir_trabajador(medico)

            elif tipo == "enfermera":
                area = input("Área: ")
                personas_a_cargo = int(input("Número de personas a cargo: "))
                enfermera = Enfermera(nif, nombre, fecha_nacimiento, sexo, area, personas_a_cargo)
                hospital.anadir_trabajador(enfermera)

            else:
                print("Tipo de trabajador inválido.")

        elif opcion == "2":
            nombre_fichero = input("Ingrese el nombre del archivo para guardar (incluya .csv): ")
            hospital.guardar_datos_csv(nombre_fichero)

        elif opcion == "3":
            nombre_fichero = input("Ingrese el nombre del archivo a cargar (incluya .csv): ")
            df = hospital.cargar_datos_csv(nombre_fichero)
            print(df.head())  
        elif opcion == "4":
            nombre_fichero = input("Ingrese el nombre del archivo a cargar (incluya .csv): ")
            df = hospital.cargar_datos_csv(nombre_fichero)
            generar_grafica(df)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
