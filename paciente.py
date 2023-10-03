from persona import Persona

pacientes = []
class Paciente(Persona):    

    def __init__(self, tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion, fecha_nacimiento, email, nombre_pariente, contacto_pariente):

        # heredamos los atributos de la clase padre
        super().__init__(tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion)
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email
        self.__nombre_pariente = nombre_pariente
        self.__contacto_pariente = contacto_pariente

    def solicitar_examen(self):
        numero_orden = int(input("Ingrese el número de la orden que le otorgó el médico, por favor: "))


    def buscar_paciente_id(self,documento):
        for i in pacientes:
            if i.get_numero_documento() == documento:
                return i.to_string()


    def registrar_paciente(self,paciente):
        pacientes.append(paciente)
        print("\nPaciente registrado con éxito")
        self.solicitar_examen()
        
        


    def imprimir_paciente(self):
        print(self.nombres, self.apellidos)



