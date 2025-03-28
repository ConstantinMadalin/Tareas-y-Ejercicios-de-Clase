import csv
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

    def borrar_trabajador(self, nif):
        self.trabajadores = [t for t in self.trabajadores if t.nif != nif]

    def mostrar_lista_trabajadores(self):
        for trabajador in self.trabajadores:
            tipo = "Médico" if isinstance(trabajador, Medico) else "Enfermera"
            print(f"{trabajador.nif}: {trabajador.nombre} ({tipo})")

    def mostrar_detalle_trabajador(self, nif):
        for trabajador in self.trabajadores:
            if trabajador.nif == nif:
                tipo = "Médico" if isinstance(trabajador, Medico) else "Enfermera"
                print(f"Tipo: {tipo}\nNombre: {trabajador.nombre}\nSexo: {trabajador.sexo}\nFecha de Nacimiento: {trabajador.fecha_nacimiento.strftime('%Y-%m-%d')}")
                if isinstance(trabajador, Medico):
                    print(f"Especialidad: {trabajador.especialidad}\nFecha de Inicio: {trabajador.fecha_inicio.strftime('%Y-%m-%d')}\nColegiado: {trabajador.numero_colegiado}")
                if isinstance(trabajador, Enfermera):
                    print(f"Área: {trabajador.area}\nPersonas a Cargo: {trabajador.personas_a_cargo}")
                return
        print("Trabajador no encontrado.")

    def calcular_anios_medico(self, nif):
        for trabajador in self.trabajadores:
            if isinstance(trabajador, Medico) and trabajador.nif == nif:
                print(f"Años trabajados: {trabajador.calcular_anios_trabajados()} años")
                return
        print("Médico no encontrado.")

    def mostrar_personas_a_cargo(self, nif):
        for trabajador in self.trabajadores:
            if isinstance(trabajador, Enfermera) and trabajador.nif == nif:
                print(f"Personas a cargo: {trabajador.personas_a_cargo}")
                return
        print("Enfermera no encontrada.")

    def modificar_personas_a_cargo(self, nif, cantidad):
        for trabajador in self.trabajadores:
            if isinstance(trabajador, Enfermera) and trabajador.nif == nif:
                trabajador.modificar_personas_a_cargo(cantidad)
                print(f"Personas a cargo actualizado: {trabajador.personas_a_cargo}")
                return
        print("Enfermera no encontrada.")

    def guardar_datos_csv(self, nombre_fichero):
        with open(nombre_fichero, "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Tipo", "NIF", "Nombre", "FechaNacimiento", "Sexo", "Especialidad", "FechaInicio", "NumeroColegiado", "Area", "PersonasACargo"])
            for trabajador in self.trabajadores:
                if isinstance(trabajador, Medico):
                    escritor.writerow(["Medico", trabajador.nif, trabajador.nombre, trabajador.fecha_nacimiento.strftime("%Y-%m-%d"), trabajador.sexo, trabajador.especialidad, trabajador.fecha_inicio.strftime("%Y-%m-%d"), trabajador.numero_colegiado, "", ""])
                elif isinstance(trabajador, Enfermera):
                    escritor.writerow(["Enfermera", trabajador.nif, trabajador.nombre, trabajador.fecha_nacimiento.strftime("%Y-%m-%d"), trabajador.sexo, "", "", "", trabajador.area, trabajador.personas_a_cargo])

    def cargar_datos_csv(self, nombre_fichero):
        with open(nombre_fichero, "r") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar la cabecera
            for linea in lector:
                tipo, nif, nombre, fecha_nacimiento, sexo, especialidad, fecha_inicio, numero_colegiado, area, personas_a_cargo = linea
                if tipo == "Medico":
                    medico = Medico(nif, nombre, fecha_nacimiento, sexo, especialidad, fecha_inicio, numero_colegiado)
                    self.anadir_trabajador(medico)
                elif tipo == "Enfermera":
                    enfermera = Enfermera(nif, nombre, fecha_nacimiento, sexo, area, int(personas_a_cargo))
                    self.anadir_trabajador(enfermera)

def main():
    hospital = Hospital()

    while True:
        print("\nGestión de los trabajadores del hospital")
        print("1. Añadir trabajador")
        print("2. Borrar trabajador")
        print("3. Mostrar lista de trabajadores")
        print("4. Mostrar detalle de un trabajador")
        print("5. Mostrar número de años trabajados de un médico")
        print("6. Mostrar número de personas a cargo de una enfermera")
        print("7. Añadir personas a cargo de una enfermera")
        print("8. Reducir personas a cargo de una enfermera")
        print("9. Guardar datos en .csv")
        print("10. Cargar datos de .csv")
        print("11. Salir")

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
            nif = input("Ingrese el NIF del trabajador a borrar: ")
            hospital.borrar_trabajador(nif)

        elif opcion == "3":
            hospital.mostrar_lista_trabajadores()

        elif opcion == "4":
            nif = input("Ingrese el NIF del trabajador: ")
            hospital.mostrar_detalle_trabajador(nif)

        elif opcion == "5":
            nif = input("Ingrese el NIF del médico: ")
            hospital.calcular_anios_medico(nif)

        elif opcion == "6":
            nif = input("Ingrese el NIF de la enfermera: ")
            hospital.mostrar_personas_a_cargo(nif)

        elif opcion == "7":
            nif = input("Ingrese el NIF de la enfermera: ")
            cantidad = int(input("Cantidad de personas a añadir: "))
            hospital.modificar_personas_a_cargo(nif, cantidad)

        elif opcion == "8":
            nif = input("Ingrese el NIF de la enfermera: ")
            cantidad = int(input("Cantidad de personas a reducir: "))
            hospital.modificar_personas_a_cargo(nif, -cantidad)

        elif opcion == "9":
            nombre_fichero = input("Ingrese el nombre del archivo para guardar (incluya .csv): ")
            hospital.guardar_datos_csv(nombre_fichero)
            print("Datos guardados correctamente.")

        elif opcion == "10":
            nombre_fichero = input("Ingrese el nombre del archivo a cargar (incluya .csv): ")
            hospital.cargar_datos_csv(nombre_fichero)
            print("Datos cargados correctamente.")

        elif opcion == "11":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()