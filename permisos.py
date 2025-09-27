def conversion(permisos):
    valor = 0
    if permisos[0] == 'r':
        valor += 4
    if permisos[1] == 'w':
        valor += 2
    if permisos[2] == 'x':
        valor += 1
    
    return valor 

def main():
    print("|       rwxrwxrwx |chmod_mate| rwxrwxrwx     |\n|cambiar permisos de archivos y directorios:)|")
    print("-____________________________________________-")
    print("Valores de entrada permitidos: (rwx o ---)")
    permisosUser = str(input("Introduzca los permisos de usuario (owner): ")).lower()
    if len(permisosUser) != 3:
        noValido = True
        while noValido:
            print("Error, se espera una cadena de 3 caracteres.")
            permisosUser = str(input("Introduzca los permisos de usuario (owner): ")).lower()
            if len(permisosUser) == 3:
                noValido = False

    permisosGroup = str(input("Introduzca los permisos de grupo (group): ")).lower()
    if len(permisosGroup) != 3:
        noValido = True
        while noValido:
            print("Error, se espera una cadena de 3 caracteres.")
            permisosGroup = str(input("Introduzca los permisos de grupo (group): ")).lower()
            if len(permisosGroup) == 3:
                noValido = False
    permisosOther = str(input("Introduzca los permisos de otros (others): ")).lower()
    if len(permisosOther) != 3:
        noValido = True
        while noValido:
            print("Error, se espera una cadena de 3 caracteres.")
            permisosOther = str(input("Introduzca los permisos de otros (others):" )).lower()
            if len(permisosOther) == 3:
                noValido = False
    octalUser = conversion(permisosUser)
    octalGroup = conversion(permisosGroup)
    octalOther = conversion(permisosOther)
    octal = f'{octalUser}{octalGroup}{octalOther}'
    return octal

main()


