import os
import tkinter as tk
class Usuario:
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo} - {self.telefono}"

class Agenda:
    def __init__(self, archivo):
        self.archivo = archivo
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        try:
            with open(self.archivo, "r") as f:
                usuarios = []
                for linea in f.readlines():
                    nombre, apellido, correo, telefono = linea.strip().split(",")
                    usuarios.append(Usuario(nombre, apellido, correo, telefono))
                return usuarios
        except FileNotFoundError:
            return []

    def guardar_usuarios(self):
        with open(self.archivo, "w") as f:
            for usuario in self.usuarios:
                f.write(f"{usuario.nombre},{usuario.apellido},{usuario.correo},{usuario.telefono}\n")

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        correo = input("Ingrese el correo: ")
        telefono = input("Ingrese el teléfono: ")
        self.usuarios.append(Usuario(nombre, apellido, correo, telefono))
        self.guardar_usuarios()

    def eliminar_usuario(self, id):
        try:
            del self.usuarios[id]
            self.guardar_usuarios()
        except IndexError:
            print("Usuario no encontrado")

    def actualizar_usuario(self, id):
        try:
            usuario = self.usuarios[id]
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            correo = input("Ingrese el nuevo correo: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.correo = correo
            usuario.telefono = telefono
            self.guardar_usuarios()
        except IndexError:
            print("Usuario no encontrado")

    def ver_usuarios(self):
        for i, usuario in enumerate(self.usuarios):
            print(f"{i}: {usuario}")

    def crear_interfaz(self):
        self.root = tk.Tk()
        self.root.title("Agenda")

        self.label_nombre = tk.Label(self.root, text="Nombre:")
        self.label_nombre.pack()

        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        self.label_apellido = tk.Label(self.root, text="Apellido:")
        self.label_apellido.pack()

        self.entry_apellido = tk.Entry(self.root)
        self.entry_apellido.pack()

        self.label_correo = tk.Label(self.root, text="Correo:")
        self.label_correo.pack()

        self.entry_correo = tk.Entry(self.root)
        self.entry_correo.pack()

        self.label_telefono = tk.Label(self.root, text="Teléfono:")
        self.label_telefono.pack()

        self.entry_telefono = tk.Entry(self.root)
        self.entry_telefono.pack()

        self.button_registrar = tk.Button(self.root, text="Registrar", command=self.registrar_usuario)
        self.button_registrar.pack()

        self.root.mainloop()

def main():
    archivo = "usuarios.txt"
    agenda = Agenda(archivo)
    while True:
        print("1. Registrar usuario")
        print("2. Eliminar usuario por id")
        print("3. Actualizar usuario por id")
        print("4. Ver usuarios")
        print("5. Salir")
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            agenda.registrar_usuario()
        elif opcion == "2":
            id = int(input("Ingrese el id del usuario: "))
            agenda.eliminar_usuario(id)
        elif opcion == "3":
            id = int(input("Ingrese el id del usuario: "))
            agenda.actualizar_usuario(id)
        elif opcion == "4":
            agenda.ver_usuarios()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()


