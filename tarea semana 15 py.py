# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Barcelona"

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Arquitecto"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "600123456"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
informacion_personal
