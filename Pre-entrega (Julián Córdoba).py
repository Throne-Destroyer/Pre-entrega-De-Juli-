Database = {}

def create_account():
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    Database[username] = password
    print("\nCuenta creada")

def leer_data():
    print("La información almacenada en la base de datos es:")
    for username, password in Database.items():
        print(username, password)

def login():
    username = input("Ingrese nombre de usuario: ")
    
    if username in Database:
        password = input("Ingrese contraseña: ")

        if Database[username] == password:
            return True
        else:
            print("No se encuentra nombre de usuario")
    else:
        print("Nombre de usuario incorrecto")
    
    return False

def back_to_menu():
    input("\nVolver al menú...")

while True:
    print("\nOpciones:")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Leer base de datos")
    print("4. Salir")

    choice = input("Ingrese su opción: ")

    if choice == "1":
        create_account()
        back_to_menu()
    elif choice == "2":
        if login():
            print("Has iniciado sesión")
            back_to_menu()
    elif choice == "3":
        leer_data()
        back_to_menu()
    elif choice == "4":
        print("Salir del programa.")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")