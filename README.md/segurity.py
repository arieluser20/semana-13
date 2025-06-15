import re
import hashlib

# Función para verificar si una contraseña es segura
def verificar_contraseña(password):
    # Requisitos mínimos
    longitud_minima = 8
    tiene_mayuscula = re.search(r'[A-Z]', password)
    tiene_minuscula = re.search(r'[a-z]', password)
    tiene_numero = re.search(r'\d', password)
    tiene_simbolo = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    if (len(password) >= longitud_minima and tiene_mayuscula and tiene_minuscula and
        tiene_numero and tiene_simbolo):
        return True
    else:
        return False

# Función para hashear la contraseña usando SHA-256
def hashear_contraseña(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

# Función principal
def main():
    print("🔐 Bienvenido al sistema de verificación de contraseñas seguras")
    password = input("Ingrese su contraseña: ")

    if verificar_contraseña(password):
        hash_seguro = hashear_contraseña(password)
        print("✅ Contraseña segura.")
        print(f"🔒 Hash de la contraseña: {hash_seguro}")
    else:
        print("❌ Contraseña insegura. Debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas, números y símbolos.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
