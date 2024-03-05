import mysql.connector

class ConexionDB:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def obtener_cursor(self):
        return self.connection.cursor()

    def cerrar_conexion(self):
        self.connection.close()

class ManejoUsuarios:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def obtener_correo_por_nombre(self):
        cursor = self.conexion.obtener_cursor()
        buscar_mail = str(input("Ingresa un nombre para obtener el correo electrónico: "))
        cursor.execute("SELECT Correo FROM alumnos WHERE Nombre = %s", (buscar_mail,))
        result = cursor.fetchall()
        if result:
            for correo in result:
                print(correo[0])
        else:
            print("No se encontró ese nombre en la base de datos.")

    def agregar_usuario(self):
        cursor = self.conexion.obtener_cursor()
        nombre = str(input("Ingresa el nombre del nuevo usuario: "))
        correo = str(input("Ingresa el correo del nuevo usuario: "))
        cursor.execute("INSERT INTO alumnos (Nombre, Correo) VALUES (%s, %s)", (nombre, correo))
        self.conexion.connection.commit()
        print("Usuario agregado correctamente.")

def main():
    conexion = ConexionDB(host="localhost", user="root", password="", database="programa")
    usuarios = ManejoUsuarios(conexion)

    while True:
        print("\n----------MENU---------- \n1. Obtener correo electrónico por nombre\n2. Agregar nuevo usuario\n3. Salir\n------------------------")  
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            usuarios.obtener_correo_por_nombre()
        elif opcion == "2":
            usuarios.agregar_usuario()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

    conexion.cerrar_conexion()

if __name__ == "__main__":
    main()
