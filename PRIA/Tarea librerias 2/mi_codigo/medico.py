from datetime import datetime
from .trabajador import Trabajador

class Medico(Trabajador):
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, especialidad, fecha_inicio, numero_colegiado):
        """
        Inicializa una instancia de la clase Medico.
        
        :param nif: NIF del médico.
        :param nombre: Nombre del médico.
        :param fecha_nacimiento: Fecha de nacimiento (en formato YYYY-MM-DD).
        :param sexo: Sexo del médico.
        :param especialidad: Especialidad del médico (por ejemplo, cardiología, pediatría).
        :param fecha_inicio: Fecha de inicio de su actividad profesional (en formato YYYY-MM-DD).
        :param numero_colegiado: Número de colegiado del médico.
        """
        super().__init__(nif, nombre, fecha_nacimiento, sexo, numero_colegiado)
        self.especialidad = especialidad
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")

    def calcular_anios_trabajados(self):
        """
        Calcula los años que ha trabajado el médico desde su fecha de inicio.
        
        :return: El número de años trabajados.
        """
        return datetime.now().year - self.fecha_inicio.year

    def mostrar_info(self):
        """
        Muestra la información completa del médico.
        """
        print(f"NIF: {self.nif}")
        print(f"Nombre: {self.nombre}")
        print(f"Sexo: {self.sexo}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento.strftime('%Y-%m-%d')}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Fecha de Inicio: {self.fecha_inicio.strftime('%Y-%m-%d')}")
        print(f"Número Colegiado: {self.numero_colegiado}")
        print(f"Años Trabajados: {self.calcular_anios_trabajados()}")
