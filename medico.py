
from persona import Persona


class Medico(Persona):
    def __init__(self,especialidad, tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion):
        super().__init__(tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion)
        self.especialidad = especialidad

