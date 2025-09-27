#Función para validar la entrada del usuario

def validar(cadena):
    valido = True
    if len(cadena) != 3:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("\n>>> Error, se espera una cadena de 3 caracteres <<<\n")
        return False
    #Comparar caracteres si son diferentes de (r,w,x,-)
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
#Convierte la entrada a su correspondiente en número octal
def conversion(permisos):
    valor = 0
    if permisos[0] == 'r':
        valor += 4
    if permisos[1] == 'w':
        valor += 2
    if permisos[2] == 'x':
        valor += 1
    return valor 
#Función principal donde corre la lógica del programa
def main():
    print("|        rwxrwxrwx |chmod_mate| rwxrwxrwx      |\n| CAMBIAR PERMISOS DE ARCHIVOS Y DIRECTORIOS:) |")
    print("-______________________________________________-")
    print("\n   Valores de entrada permitidos: (rwx o -)")
    print("* <r> - Permiso de Lectura\n* <w> - Permiso de Escritura\n* <x> - Permiso de ejecucion\n* <-> - Negación de permiso");
    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        permisosUser = str(input("-> Introduzca los permisos de usuario (owner): ")).lower()
        if validar(permisosUser):
            break

    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        permisosGroup = str(input("-> Introduzca los permisos de grupo (group): ")).lower()
        if validar(permisosGroup):
            break
 
    while True:  
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")      
        permisosOther = str(input("-> Introduzca los permisos de otros (others): ")).lower()
        if validar(permisosOther):
            break

    octalUser = conversion(permisosUser)
    octalGroup = conversion(permisosGroup)
    octalOther = conversion(permisosOther)
    octal = f'{octalUser}{octalGroup}{octalOther}'
    nombreRutaODirectorio = input("Introduzca el nombre del directorio o archivo a modificar permisos: ")
    recursivo = input("¿Aplicar recursividad? (S/n)").lower().strip() 
    if recursivo in ['si','sí','s','y','yes']:
        recursivo = '-R'
    else:
        recursivo = ''
    #Salida del programa
    print(f'Su comando chmod es: chmod  {octal} {recursivo} {nombreRutaODirectorio} ')
    return octal,nombreRutaODirectorio,recursivo 

main()