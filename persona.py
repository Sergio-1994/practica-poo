class Persona():

    def __init__(self, tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion):
        #Encapsulamos los atributos de la clase
        self.__tipo_documento = tipo_documento
        self.__numero_documento = numero_documento
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__telefono = telefono
        self.__celular = celular
        self.__direccion = direccion

    def set_numero_documento(self, numero_documento):
        self.__numero_documento = numero_documento

    def get_numero_documento(self):
        return self.__numero_documento
    
    def set_nombres(self, nombres):
        self.__nombres = nombres

    def get_nombres(self):
        return self.__nombres

    def to_string(self):
        print("\nLos datos del paciente son:")
        return(f"Nombre: {self.get_nombres()}\nDocumento: {self.get_numero_documento()}")

    