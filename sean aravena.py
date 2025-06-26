nombreusuario = []
usuarios = {}

def validadorcontraseña(contraseña):
    contador_numeros = 0
    contador_letras = 0
    if len(contraseña) < 8:
        print("La contraseña debe tener mínimo 8 caracteres.")
        return False
    for letra in contraseña:
        if letra.isdigit():
            contador_numeros += 1
        if letra.isalpha() and letra.isupper():
            contador_letras += 1
    if contador_numeros < 1:
        print("La contraseña debe contener al menos un número.")
        return False
    if contador_letras < 1:
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False
    return True

def validadorSexo(sexo):
    if sexo != "F" and sexo != "M":
        print("El sexo se debe ingresar como M para masculino o F para femenino.")
        return False
    return True

def buscarusuarios(nombre):
    if nombre in usuarios:
        print("Usuario encontrado.")
        return usuarios[nombre]
    print("Usuario no encontrado.")
    return None

opcion = "0"
while opcion != "4":
    print("\n1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    opcion = input("Ingrese la opción que desea (1-4): ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del usuario: ").lower()
            if nombre in usuarios:
                print("El usuario ya existe.")
                continue
            while True:
                sexo = input("Ingrese el sexo del usuario (M/F): ").upper()
                if validadorSexo(sexo):
                    break
            while True:
                contraseña = input("Ingrese una contraseña con mínimo 8 caracteres: ")
                if validadorcontraseña(contraseña):
                    break
            usuarios[nombre] = {"sexo": sexo, "contraseña": contraseña}
            print("Usuario agregado exitosamente.")

        case "2":
            nombre = input("Ingrese el nombre del usuario que desea buscar: ").lower()
            datos = buscarusuarios(nombre)
            if datos:
                print(f"Datos del usuario: Sexo - {datos['sexo']}, Contraseña - {datos['contraseña']}")

        case "3":
            nombre = input("Ingrese el nombre del usuario que desea eliminar: ").lower()
            if nombre in usuarios:
                del usuarios[nombre]
                print("Usuario eliminado correctamente.")
            else:
                print("El usuario no existe.")

        case "4":
            print("Saliendo...")

        case _:
            print("Opción no válida.")