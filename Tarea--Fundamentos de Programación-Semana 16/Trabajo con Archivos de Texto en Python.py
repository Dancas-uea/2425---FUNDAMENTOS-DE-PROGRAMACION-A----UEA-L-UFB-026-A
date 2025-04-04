# Tarea: Trabajo con Archivos de Texto en Python
# Autor: Carlos Daniel Castillo Cabrera
# Fecha: Abril 2025

# Escritura de Archivo de Texto
def escribir_archivo():
    """Función para crear y escribir en un archivo de texto"""
    try:
        # Abrir el archivo en modo escritura ('w')
        with open('Las Cosas Ocultas.txt', 'w', encoding='utf-8') as archivo:
            # Escribir tres párrafos de notas personales
            archivo.write("1. La Biblioteca del Vaticano – Alberga millones de manuscritos y textos antiguos, "
                          "muchos inaccesibles al público, incluyendo posiblemente conocimientos "
                          "históricos, esotéricos y científicos censurados.\n\n")

            archivo.write("2. Las Líneas de Nazca en Perú – Gigantescos geoglifos solo visibles "
                          "desde el aire, cuyo verdadero propósito (ritual, astronómico o alienígena) "
                          "sigue siendo un enigma.\n\n")

            archivo.write("3. La Red Global de Túneles Subterráneos – Desde ciudades subterráneas "
                          "como Derinkuyu (Turquía) hasta túneles secretos bajo capitales "
                          "mundiales, su origen y uso exacto son desconocidos.\n\n")

        print("Archivo 'Las Cosas Ocultas.txt' creado y escrito exitosamente.")
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")


# Lectura de Archivo de Texto
def leer_archivo():
    """Función para leer un archivo de texto conservando el formato"""
    try:
        # Abrir el archivo en modo lectura ('r')
        with open('Las Cosas Ocultas.txt', 'r', encoding='utf-8') as archivo:
            print("\nContenido del archivo 'Las Cosas Ocultas.txt':\n")
            # Leer todo el contenido y mostrarlo directamente

            print(archivo.read())
    except FileNotFoundError:
        print("Error: El archivo 'Las Cosas Ocultas.txt' no existe.")
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
# Ejecutar las funciones
escribir_archivo()
leer_archivo()