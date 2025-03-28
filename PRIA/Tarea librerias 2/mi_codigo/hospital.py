import csv
from datetime import datetime

class Trabajador:
    """
    Representa a un trabajador del hospital.
    
    Atributos:
        nif (str): Número de identificación fiscal del trabajador.
        nombre (str): Nombre del trabajador.
        fecha_nacimiento (datetime): Fecha de nacimiento del trabajador.
        sexo (str): Sexo del trabajador (M/F).
        numero_colegiado (str): Número de colegiado para médicos (opcional).
    """
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, numero_colegiado=None):
        """
        Inicializa un trabajador.
        
        Args:
            nif (str): Número de identificación fiscal del trabajador.
            nombre (str): Nombre del trabajador.
            fecha_nacimiento (str): Fecha de nacimiento en formato 'YYYY-MM-DD'.
            sexo (str): Sexo del trabajador (M/F).
            numero_colegiado (str, opcional): Número de colegiado para médicos.
        """
        self.nif = nif
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        self.sexo = sexo
        self.numero_colegiado = numero_colegiado

class Medico(Trabajador):
    """
    Representa a un médico en el hospital, heredando de la clase Trabajador.
    
    Atributos:
        especialidad (str): Especialidad del médico.
        fecha_inicio (datetime): Fecha en la que el médico comenzó a trabajar.
    """
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, especialidad, fecha_inicio, numero_colegiado):
        """
        Inicializa un médico con la especialidad y la fecha de inicio.
        
        Args:
            nif (str): Número de identificación fiscal del trabajador.
            nombre (str): Nombre del trabajador.
            fecha_nacimiento (str): Fecha de nacimiento en formato 'YYYY-MM-DD'.
            sexo (str): Sexo del trabajador (M/F).
            especialidad (str): Especialidad del médico.
            fecha_inicio (str): Fecha de inicio en formato 'YYYY-MM-DD'.
            numero_colegiado (str): Número de colegiado del médico.
        """
        super().__init__(nif, nombre, fecha_nacimiento, sexo, numero_colegiado)
        self.especialidad = especialidad
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")

    def calcular_anios_trabajados(self):
        """
        Calcula los años que el médico ha trabajado en el hospital.
        
        Returns:
            int: Número de años trabajados.
        """
        return datetime.now().year - self.fecha_inicio.year

class Enfermera(Trabajador):
    """
    Representa a una enfermera en el hospital, heredando de la clase Trabajador.
    
    Atributos:
        area (str): Área en la que trabaja la enfermera.
        personas_a_cargo (int): Número de personas a cargo de la enfermera.
    """
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, area, personas_a_cargo):
        """
        Inicializa una enfermera con el área y el número de personas a cargo.
        
        Args:
            nif (str): Número de identificación fiscal del trabajador.
            nombre (str): Nombre del trabajador.
            fecha_nacimiento (str): Fecha de nacimiento en formato 'YYYY-MM-DD'.
            sexo (str): Sexo del trabajador (M/F).
            area (str): Área en la que trabaja la enfermera.
            personas_a_cargo (int): Número de personas a cargo de la enfermera.
        """
        super().__init__(nif, nombre, fecha_nacimiento, sexo)
        self.area = area
        self.personas_a_cargo = personas_a_cargo

    def modificar_personas_a_cargo(self, cantidad):
        """
        Modifica el número de personas a cargo de la enfermera.
        
        Args:
            cantidad (int): Número de personas a añadir o reducir.
        """
        self.personas_a_cargo += cantidad

class Hospital:
    """
    Representa un hospital que gestiona los trabajadores.

    Atributos:
        trabajadores (list): Lista de trabajadores del hospital.
    """
    def __init__(self):
        """
        Inicializa el hospital con una lista vacía de trabajadores.
        """
        self.trabajadores = []

    def anadir_trabajador(self, trabajador):
        """
        Añade un trabajador al hospital.

        Args:
            trabajador (Trabajador): El trabajador a añadir.
        """
        self.trabajadores.append(trabajador)

    def borrar_trabajador(self, nif):
        """
        Borra un trabajador del hospital mediante su NIF.

        Args:
            nif (str): El NIF del trabajador a borrar.
        """
        self.trabajadores = [t for t in self.trabajadores if t.nif != nif]

    def mostrar_lista_trabajadores(self):
        """
        Muestra la lista de trabajadores del hospital.
        """
        for trabajador in self.trabajadores:
            tipo = "Médico" if isinstance(trabajador, Medico) else "Enfermera"
            print(f"{trabajador.nif}: {trabajador.nombre} ({tipo})")

    def mostrar_detalle_trabajador(self, nif):
        """
        Muestra los detalles de un trabajador especificado por su NIF.

        Args:
            nif (str): El NIF del trabajador a mostrar.
        """
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
        """
        Calcula los años trabajados de un médico especificado por su NIF.

        Args:
            nif (str): El NIF del médico.
        """
        for trabajador in self.trabajadores:
            if isinstance(trabajador, Medico) and trabajador.nif == nif:
                print(f"Años trabajados: {trabajador.calcular_anios_trabajados()} años")
                return
        print("Médico no encontrado.")

    def mostrar_personas_a_cargo(self, nif):
        """
        Muestra el número de personas a cargo de una enfermera especificada por su NIF.

        Args:
            nif (str): El NIF de la enfermera.
        """
        for trabajador in self.trabajadores:
            if isinstance(trabajador, Enfermera) and trabajador.nif == nif:
                print(f"Personas a cargo: {trabajador.personas_a_cargo}")
                return
        print("Enfermera no encontrada.")

    def modificar_personas_a_cargo(self, nif, cantidad):
        """
        Modifica el número de personas a cargo de una enfermera especificada por su NIF.

        Args:
            nif (str): El NIF de la enfermera.
            cantidad (int): El número de personas a añadir o reducir.
        """
        for trabajador in self.trabajadores:
            if isinstance(trabajador, Enfermera) and trabajador.nif == nif:
                trabajador.modificar_personas_a_cargo(cantidad)
                print(f"Personas a cargo actualizado: {trabajador.personas_a_cargo}")
                return
        print("Enfermera no encontrada.")

    def guardar_datos_csv(self, nombre_fichero):
        """
        Guarda la lista de trabajadores en un archivo CSV.

        Args:
            nombre_fichero (str): El nombre del archivo donde se guardarán los datos.
        """
        with open(nombre_fichero, "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Tipo", "NIF", "Nombre", "FechaNacimiento", "Sexo", "Especialidad", "FechaInicio", "NumeroColegiado", "Area", "PersonasACargo"])
            for trabajador in self.trabajadores:
                if isinstance(trabajador, Medico):
                    escritor.writerow(["Medico", trabajador.nif, trabajador.nombre, trabajador.fecha_nacimiento.strftime("%Y-%m-%d"), trabajador.sexo, trabajador.especialidad, trabajador.fecha_inicio.strftime("%Y-%m-%d"), trabajador.numero_colegiado, "", ""])
                elif isinstance(trabajador, Enfermera):
                    escritor.writerow(["Enfermera", trabajador.nif, trabajador.nombre, trabajador.fecha_nacimiento.strftime("%Y-%m-%d"), trabajador.sexo, "", "", "", trabajador.area, trabajador.personas_a_cargo])

    def cargar_datos_csv(self, nombre_fichero):
        """
        Carga los datos de trabajadores desde un archivo CSV.

        Args:
            nombre_fichero (str): El nombre del archivo desde donde se cargarán los datos.
        """
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
