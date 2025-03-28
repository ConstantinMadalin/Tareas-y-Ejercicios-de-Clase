trabajador
==========

Este módulo define la clase base `Trabajador`, que es utilizada para representar a los trabajadores de un hospital, tanto médicos como enfermeras. La clase `Trabajador` almacena información común a todos los trabajadores, como el NIF, nombre, fecha de nacimiento, y sexo.

La clase `Trabajador` es utilizada como base para las clases `Medico` y `Enfermera`, que heredan sus atributos y métodos.

Clase trabajador
------------------------

.. autoclass:: Trabajador
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

Atributos
---------

- `nif`: NIF del trabajador.
- `nombre`: Nombre del trabajador.
- `fecha_nacimiento`: Fecha de nacimiento del trabajador.
- `sexo`: Sexo del trabajador.
- `numero_colegiado`: (Opcional) Número de colegiado, utilizado solo en el caso de médicos.

Métodos
-------

La clase `Trabajador` no tiene métodos propios, pero se utiliza como clase base para las clases `Medico` y `Enfermera`, las cuales añaden su propia funcionalidad.
