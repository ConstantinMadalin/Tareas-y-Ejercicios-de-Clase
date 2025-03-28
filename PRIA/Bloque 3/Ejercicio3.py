# Crear un diccionario vacío
diccionario = {}

# Abrir el archivo de texto en modo lectura
with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        # Eliminar espacios en blanco innecesarios al principio y al final
        linea = linea.strip()

        # Separar la línea en "apellidos, nombre" y "teléfono" usando el signo '=' como delimitador
        if '=' in linea:
            parte_nombre_tel = linea.split('=')  # Dividimos por el signo '='
            
            # Limpiar las partes de los espacios en blanco innecesarios
            clave = parte_nombre_tel[0].strip()  # "apellidos, nombre"
            telefono = parte_nombre_tel[1].strip()  # "teléfono"
            
            # Si la clave ya existe en el diccionario, agregamos el teléfono a la lista
            if clave in diccionario:
                diccionario[clave].append(telefono)
            else:
                # Si no existe, creamos una nueva entrada con el teléfono
                diccionario[clave] = [telefono]

# Mostrar el diccionario con la información procesada
for clave, telefonos in diccionario.items():
    print(f"{clave}: {', '.join(telefonos)}")
