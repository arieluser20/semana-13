# Definimos una base de datos simulada de usuarios
usuarios = {
    "estudiante1": {"rol": "estudiante", "clave": "1234"},
    "profesor1": {"rol": "profesor", "clave": "abcd"},
    "admin1": {"rol": "administrador", "clave": "adminpass"}
}

# Áreas y permisos
permisos = {
    "aula": ["estudiante", "profesor", "administrador"],
    "laboratorio": ["profesor", "administrador"],
    "oficina": ["administrador"]
}

def verificar_acceso(usuario, clave, area):
    # Verificamos si el usuario existe
    if usuario not in usuarios:
        return "Acceso denegado: usuario no registrado."
    
    # Verificamos la clave
    if usuarios[usuario]["clave"] != clave:
        return "Acceso denegado: clave incorrecta."
    
    # Verificamos permisos de acceso al área
    rol = usuarios[usuario]["rol"]
    if rol in permisos.get(area, []):
        return f"Acceso concedido al área '{area}' para el rol '{rol}'."
    else:
        return f"Acceso denegado: el rol '{rol}' no tiene permiso para ingresar a '{area}'."

# Ejemplo de uso
usuario = input("Ingrese su nombre de usuario: ")
clave = input("Ingrese su clave: ")
area = input("Ingrese el área que desea acceder (aula, laboratorio, oficina): ")

resultado = verificar_acceso(usuario, clave, area)
print(resultado)
