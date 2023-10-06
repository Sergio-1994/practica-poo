from persona import Persona

lista_de_medicos = []
class Medico(Persona):

    def __init__(self,especialidad, tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion):
        super().__init__(tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion)
        self.especialidad = especialidad

    
    def get_medico_id(self, documento):
        for i in lista_de_medicos:
            if i.get_numero_documento() == documento:
                return i.get_numero_documento()

    

medico1 = Medico("Cirujano", "Cedula", 123, "Andres", "Garcia", "1234", "321896787", "calle40")
medico2 = Medico("Cirujano", "Cedula", 456, "Sergio", "Morales", "1234", "32189677", "calle 42")

lista_de_medicos.append(medico1)
lista_de_medicos.append(medico2)