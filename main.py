personas = []

def ingresar_persona():
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    dni = input("dni: ")
    
    
    telefonos = input("ingresa los telefonos separados por comas: ").split(",") #split, por cada coma se divide
    telefonos = [telefono.strip() for telefono in telefonos] #strip, elimina espacios en blanco
    
    
    hijos = input("ingresa los nombres de los hijos separados por comas: ").split(",")
    hijos = [hijo.strip() for hijo in hijos]
    
    persona = [nombre, apellido, dni, telefonos, hijos]
    personas.append(persona)#agrega otra persona a la matriz
    print("persona ingresada correctamente")

def mostrar_datos():
    if len(personas) == 0:
        print("no hay datos")
    else:
        for persona in personas:
            nombre, apellido, dni, telefonos, hijos = persona
            print(f"{nombre} {apellido}, dni: {dni}, telefonos: {len(telefonos)} telefono(s), hijos: {len(hijos)}")#len, longitud

def filtrar_por_dni():
    dni_buscado = input("ingresa el dni para filtrar: ")
    encontrado = False
    for persona in personas:
        if persona[2] == dni_buscado:  # compara el dni
            nombre, apellido, dni, telefonos, hijos = persona
            print(f"datos de {nombre} {apellido}:")
            print(f"dni: {dni}, telefonos: {len(telefonos)} telefono(s), hijos: {len(hijos)}")
            encontrado = True
            break
    if not encontrado:
        print("no se encontro una persona con ese dni")

def mostrar_menu():
    while True:
        print("--- menu ---")
        print("1. ingresar nueva persona")
        print("2. mostrar todos los datos")
        print("3. filtrar por dni")
        print("4. salir")
        
        opcion = input("elige una opcion: ")
        
        if opcion == "1":
            ingresar_persona()
        elif opcion == "2":
            mostrar_datos()
        elif opcion == "3":
            filtrar_por_dni()
        elif opcion == "4":
            print("sasliendo del programa, hasta luego")
            break
        else:
            print("opcion no valida, intenta nuevamente6")

# ejecutar el programa
mostrar_menu()
