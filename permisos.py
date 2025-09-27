def validar(cadena):
    valido = True
    if len(cadena) != 3:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("\n>>> Error, se espera una cadena de 3 caracteres <<<\n")
        # valido = False
        return False
    # quiero hacerlo de forma mas chida pero bueno :^
    if cadena[0] != "-" and cadena[0] != "r":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Error. El caracter #1 no es un permiso válido\n")
        print(" ".join(cadena))
        print("^")
        print(">>> se esperaba 'w' o '-'")
        valido = False
    if cadena[1] != "-" and cadena[1] != "w":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Error. El caracter #2 no es un permiso válido\n")
        print(" ".join(cadena))
        print("  ^")   
        print(">>> se esperaba 'w' o '-'")
        valido = False
    if cadena[2] != "-" and cadena[2] != "x":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("Error. El caracter #3 no es un permiso válido\n")
        print(" ".join(cadena))
        print("    ^")
        print(">>> se esperaba 'w' o '-'")
        valido = False
    return valido
    
def main():
    print("|        rwxrwxrwx |chmod_mate| rwxrwxrwx      |\n| CAMBIAR PERMISOS DE ARCHIVOS Y DIRECTORIOS:) |")
    print("-______________________________________________-")
    print("\nValores de entrada permitidos: (rwx o ---)")
    print("* r - Permiso de Lectura\n* w - Permiso de Escritura\n* x - permiso de ejecucion");
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        permisosUser = str(input("-> Introduzca los permisos de usuario (owner): ")).lower()
        if validar(permisosUser):
            break
        # while noValido:
        #     # print("Error, se espera una cadena de 3 caracteres.")
        #     permisosUser = str(input("-> Introduzca los permisos de usuario (owner): ")).lower()
        #     if len(permisosUser) == 3:
        #         noValido = False
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        permisosGroup = str(input("-> Introduzca los permisos de grupo (group): ")).lower()
        if validar(permisosGroup):
            break
        # noValido = True
        # while noValido:
        #     print("Error, se espera una cadena de 3 caracteres.")
        #     permisosGroup = str(input("Introduzca los permisos de grupo (group): ")).lower()
        #     if len(permisosGroup) == 3:
        #         noValido = False
    while True:  
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")      
        permisosOther = str(input("-> Introduzca los permisos de otros (others): ")).lower()
        if validar(permisosOther):
            break
    #     noValido = True
    #     while noValido:
    #         print("Error, se espera una cadena de 3 caracteres.")
    #         permisosOther = str(input("Introduzca los permisos de otros (others):" )).lower()
    #         if len(permisosOther) == 3:
    #             noValido = False
    return permisosUser,permisosGroup,permisosOther

main()


