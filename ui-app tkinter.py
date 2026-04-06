import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio


class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.servicio = TareaServicio()

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Botones
        tk.Button(root, text="Agregar", command=self.agregar_tarea).pack()
        tk.Button(root, text="Completar", command=self.completar_tarea).pack()
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack()

        # Lista
        self.lista = tk.Listbox(root, width=50, height=10)
        self.lista.pack(pady=10)

        # Atajos teclado
        self.root.bind("<Return>", lambda e: self.agregar_tarea())
        self.root.bind("<c>", lambda e: self.completar_tarea())
        self.root.bind("<C>", lambda e: self.completar_tarea())
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())
        self.root.bind("<d>", lambda e: self.eliminar_tarea())
        self.root.bind("<D>", lambda e: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda e: self.root.quit())

    def agregar_tarea(self):
        texto = self.entry.get()

        if not texto.strip():
            messagebox.showwarning("Aviso", "Escribe una tarea")
            return

        self.servicio.agregar_tarea(texto)
        self.entry.delete(0, tk.END)
        self.actualizar_lista()

    def completar_tarea(self):
        try:
            indice = self.lista.curselection()[0]
            self.servicio.completar_tarea(indice)
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def eliminar_tarea(self):
        try:
            indice = self.lista.curselection()[0]
            self.servicio.eliminar_tarea(indice)
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.servicio.obtener_tareas():
            if tarea.completada:
                self.lista.insert(tk.END, f"✔ {tarea.descripcion}")
            else:
                self.lista.insert(tk.END, f"✘ {tarea.descripcion}")