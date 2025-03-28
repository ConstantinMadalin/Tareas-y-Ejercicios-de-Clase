from datetime import datetime

class Trabajador:
    def __init__(self, nif, nombre, fecha_nacimiento, sexo, numero_colegiado=None):
        """
        Inicializa una instancia de la clase Trabajador.

        :param nif: NIF del trabajador.
        :param nombre: Nombre del trabajador.
        :param fecha_nacimiento: Fecha de nacimiento del trabajador en formato 'YYYY-MM-DD'.
        :param sexo: Sexo del trabajador.
        :param numero_colegiado: Número de colegiado (opcional).
        """
        self.nif = nif
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        self.sexo = sexo
        self.numero_colegiado = numero_colegiado
