class Persona():

    def __init__(self, tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion):
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.celular = celular
        self.direccion = direccion

    def to_string(self):
        print(f"Nombre: {self.nombre}\n\
              Documento: {self.numero_documento}")

    