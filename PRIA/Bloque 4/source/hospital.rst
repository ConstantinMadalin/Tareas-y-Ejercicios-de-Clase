Hospital Documentation
======================

Bienvenido a la documentación del sistema de gestión de trabajadores de un hospital. Este sistema permite gestionar tanto a médicos como a enfermeras, almacenando información clave sobre ellos, como su nombre, fecha de nacimiento, especialidad (en el caso de los médicos), y área de trabajo (en el caso de las enfermeras), entre otros.

Este sistema está compuesto por varias clases que definen a los trabajadores del hospital y gestionan diversas acciones como agregar, eliminar, y modificar trabajadores. A continuación se describe la estructura principal del sistema.

Contenido
---------
1. `Trabajador`
2. `Medico`
3. `Enfermera`
4. `Hospital`

trabajador
----------
La clase `Trabajador` es la clase base para todos los trabajadores en el sistema. Define los atributos comunes a todos los trabajadores, como el `NIF`, `nombre`, `fecha_nacimiento`, `sexo` y, opcionalmente, el `numero_colegiado`.

Atributos:
- `nif`: El NIF del trabajador.
- `nombre`: El nombre del trabajador.
- `fecha_nacimiento`: La fecha de nacimiento del trabajador.
- `sexo`: El sexo del trabajador.
- `numero_colegiado`: El número de colegiado (solo para médicos).

Métodos:
- `__init__(self, nif, nombre, fecha_nacimiento, sexo, numero_colegiado=None)`: Constructor de la clase, que inicializa los atributos mencionados.

medico
------
La clase `Medico` hereda de `Trabajador` y añade atributos específicos para los médicos. Incluye la especialidad del médico, la fecha de inicio de trabajo y el número de colegiado.

Atributos:
- `especialidad`: La especialidad médica (por ejemplo, Cardiología).
- `fecha_inicio`: La fecha en que el médico empezó a trabajar en el hospital.

Métodos:
- `__init__(self, nif, nombre, fecha_nacimiento, sexo, especialidad, fecha_inicio, numero_colegiado)`: Constructor que inicializa los atributos de la clase `Medico`.
- `calcular_anios_trabajados(self)`: Calcula el número de años que el médico ha trabajado en el hospital.

enfermera
---------
La clase `Enfermera` también hereda de `Trabajador`, pero agrega atributos específicos para las enfermeras, como el área en la que trabajan y el número de personas a su cargo.

Atributos:
- `area`: El área donde trabaja la enfermera (por ejemplo, Urgencias, Pediatría).
- `personas_a_cargo`: El número de personas a cargo de la enfermera.

Métodos:
- `__init__(self, nif, nombre, fecha_nacimiento, sexo, area, personas_a_cargo)`: Constructor que inicializa los atributos de la clase `Enfermera`.
- `modificar_personas_a_cargo(self, cantidad)`: Modifica el número de personas a cargo de la enfermera.
- `mostrar_info(self)`: Muestra la información completa de la enfermera.

Hospital
--------
La clase `Hospital` gestiona una lista de trabajadores, permitiendo agregar, eliminar, y modificar trabajadores. También permite mostrar la lista de trabajadores y detalles de un trabajador específico.

Atributos:
- `trabajadores`: Una lista que contiene todos los trabajadores del hospital.

Métodos:
- `__init__(self)`: Inicializa la lista vacía de trabajadores.
- `anadir_trabajador(self, trabajador)`: Añade un trabajador a la lista.
- `borrar_trabajador(self, nif)`: Borra un trabajador de la lista por su NIF.
- `mostrar_lista_trabajadores(self)`: Muestra una lista de todos los trabajadores.
- `mostrar_detalle_trabajador(self, nif)`: Muestra los detalles completos de un trabajador específico.
- `calcular_anios_medico(self, nif)`: Muestra los años trabajados por un médico específico.
- `mostrar_personas_a_cargo(self, nif)`: Muestra el número de personas a cargo de una enfermera.
- `modificar_personas_a_cargo(self, nif, cantidad)`: Modifica el número de personas a cargo de una enfermera.
- `guardar_datos_csv(self, nombre_fichero)`: Guarda los datos de los trabajadores en un archivo CSV.
- `cargar_datos_csv(self, nombre_fichero)`: Carga los datos de los trabajadores desde un archivo CSV.

Uso del Sistema
---------------
El sistema se puede utilizar a través de la consola. A continuación se describen las acciones disponibles:

1. **Añadir trabajador**: Permite añadir un nuevo trabajador (médico o enfermera) al hospital.
2. **Borrar trabajador**: Permite borrar un trabajador del hospital usando su NIF.
3. **Mostrar lista de trabajadores**: Muestra una lista con todos los trabajadores registrados.
4. **Mostrar detalle de un trabajador**: Muestra los detalles completos de un trabajador específico.
5. **Mostrar número de años trabajados de un médico**: Muestra el número de años que un médico ha trabajado en el hospital.
6. **Mostrar número de personas a cargo de una enfermera**: Muestra el número de personas a cargo de una enfermera.
7. **Añadir personas a cargo de una enfermera**: Permite añadir personas a cargo de una enfermera.
8. **Reducir personas a cargo de una enfermera**: Permite reducir el número de personas a cargo de una enfermera.
9. **Guardar datos en un archivo CSV**: Permite guardar todos los datos de los trabajadores en un archivo CSV.
10. **Cargar datos desde un archivo CSV**: Permite cargar los datos de los trabajadores desde un archivo CSV previamente guardado.
11. **Salir**: Sale del programa.

Ejemplo de Uso
---------------
```python
from hospital.enfermera import Enfermera
from hospital.medico import Medico
from hospital.hospital import Hospital

# Crear una instancia de Hospital
hospital = Hospital()

# Crear médicos y enfermeras
medico = Medico(nif="12345678A", nombre="Dr. Pérez", fecha_nacimiento="1980-05-15", sexo="Masculino", 
                especialidad="Cardiología", fecha_inicio="2010-01-01", numero_colegiado="12345")
enfermera = Enfermera(nif="87654321B", nombre="Ana López", fecha_nacimiento="1985-02-20", sexo="Femenino", 
                      area="Urgencias", personas_a_cargo=5)

# Añadir al hospital
hospital.anadir_trabajador(medico)
hospital.anadir_trabajador(enfermera)

# Mostrar la lista de trabajadores
hospital.mostrar_lista_trabajadores()

# Mostrar detalles de un trabajador
hospital.mostrar_detalle_trabajador("12345678A")

# Guardar datos en CSV
hospital.guardar_datos_csv("trabajadores.csv")

# Cargar datos desde CSV
hospital.cargar_datos_csv("trabajadores.csv")
