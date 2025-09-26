
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
    return permisosUser,permisosGroup,permisosOther

main()


