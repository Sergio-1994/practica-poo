class Paciente(Persona):

    def __init__(self, fecha_nacimiento, email, nombre_paciente, contacto_paciente, tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion):

        # heredamos los atributos de la clase padre
        super().__init__(tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion)
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.nombre_pariente = nombre_pariente
        self.contacto_pariente = contacto_pariente

    def solicitar_examen(self):
        pass