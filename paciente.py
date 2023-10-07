from DetalleFactura import DetalleFactura
from persona import Persona
from Orden import Orden
from medico import lista_de_medicos


pacientes = []
class Paciente(Persona):    

    def __init__(self, tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion, fecha_nacimiento, pos, email, nombre_pariente, contacto_pariente):

        # heredamos los atributos de la clase padre
        super().__init__(tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion)
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__fecha_nacimiento = fecha_nacimiento
        self.__pos = pos
        self.__email = email
        self.__nombre_pariente = nombre_pariente
        self.__contacto_pariente = contacto_pariente
        self.aux = 0

    def solicitar_examen(self, paciente):
        numero_orden = int(input("\nIngrese el número de la orden que le otorgó el médico, por favor: "))
        for i in lista_de_medicos:
            print(f"Nombre: {i.get_nombres()} | Cedula: {i.get_numero_documento()}")

            
        med = int(input("Seleccione el médico según el número de cedula, por favor: "))        
        if self.aux != numero_orden:
            self.aux = numero_orden
            orden = Orden(med,numero_orden,paciente.get_nombres())
            
            orden.registrar_orden(orden,self.__pos)
        else:
            print("Ya existe una orden, puedes crear el examen")

    def buscar_paciente_id(self,documento):
        for i in pacientes:
            if i.get_numero_documento() == documento:
                return i.to_string()


    def registrar_paciente(self,paciente):
        pacientes.append(paciente)
        print("\nPaciente registrado con éxito")
        self.solicitar_examen(paciente)
        
        


    def imprimir_paciente(self):
        print(self.set_nombres, self.__apellidos)

    def get_pos(self):
       return self.__pos

