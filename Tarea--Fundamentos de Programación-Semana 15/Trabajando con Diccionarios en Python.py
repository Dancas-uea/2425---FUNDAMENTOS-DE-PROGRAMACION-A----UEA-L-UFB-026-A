print("\n" + "-"*50 + "\n")
print("1. Crear un Diccionario")
# Creación del diccionario con información personal básica
informacion_personal = {
    "nombre": "Daniel Castillo",
    "edad": 22,
    "ciudad": "Puerto Asis",
    "Profesión": "Ingeniero en Tecnologias de la informacion"
}
print(informacion_personal)
print("\n" + "-"*50 + "\n")

# Acceder y modificar el valor de "ciudad"
print("2. Acceder y Modificar Valores - Verificar Existencia de Claves")
ciudad_original = informacion_personal["ciudad"]
informacion_personal["ciudad"] = "Valledupar"

# Agregar la clave "profesion" que no existía originalmente
informacion_personal["Profesión"] = "Desarrollador Web"
print(informacion_personal)
print("\n" + "-"*50 + "\n")

# Verificar si existe "telefono" y agregarlo si no existe
print("3.Verificar Existencia de Claves")
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0986941769"
    print("Se ha añadido el teléfono al diccionario")
else:
    print("El teléfono ya existía en el diccionario")

print(informacion_personal)
print("\n" + "-"*50 + "\n")  # Separador visual

# Eliminar la clave "edad" del diccionario
print("4. Eliminar una Clave")
del informacion_personal["edad"]
print(informacion_personal)
print("\n" + "-"*50 + "\n")

# Mostrar el diccionario resultante final
print("5. Imprimir el Diccionario Final:")
for clave, valor in informacion_personal.items():
    print(f"{clave.upper()}: {valor}")
