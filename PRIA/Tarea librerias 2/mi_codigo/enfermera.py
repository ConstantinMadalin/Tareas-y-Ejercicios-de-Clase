from .trabajador import Trabajador

class Enfermera(Trabajador):
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, area, personas_a_cargo):
        """
        Inicializa una instancia de la clase Enfermera.

        :param nif: NIF de la enfermera.
        :param nombre: Nombre de la enfermera.
        :param fecha_nacimiento: Fecha de nacimiento (en formato YYYY-MM-DD).
        :param sexo: Sexo de la enfermera.
        :param area: Área en la que trabaja la enfermera (por ejemplo, urgencias, pediatría).
        :param personas_a_cargo: Número de personas a cargo de la enfermera.
        """
        super().__init__(nif, nombre, fecha_nacimiento, sexo)
        self.area = area
        self.personas_a_cargo = personas_a_cargo

    def modificar_personas_a_cargo(self, cantidad):
        """
        Modifica el número de personas a cargo de la enfermera.

        :param cantidad: Número de personas a añadir o reducir a cargo de la enfermera.
        :return: None
        """
        self.personas_a_cargo += cantidad

    def mostrar_info(self):
        """
        Muestra la información completa de la enfermera.
        """
        print(f"NIF: {self.nif}")
        print(f"Nombre: {self.nombre}")
        print(f"Sexo: {self.sexo}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento.strftime('%Y-%m-%d')}")
        print(f"Área: {self.area}")
        print(f"Personas a Cargo: {self.personas_a_cargo}")
