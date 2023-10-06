from datetime import datetime
from examen import Examen

ordenes = []
class Orden:
    def __init__(self, medico_tratante, numero_orden, paciente):
        self.fecha_solicitud = datetime.now()
        self.fecha_ingreso = datetime.now()
        self.medico_tratante = medico_tratante
        self.numero_orden = numero_orden
        self.paciente = paciente
    
    def get_numero_orden(self):
        return self.numero_orden

    def registrar_orden(self, orden):
        ordenes.append(orden)
        print("\nOrden registrada con éxito")
        print(self.get_data())
        exam = Examen("observaiciones", "Triglicéridos", self.get_numero_orden())
        exam.registrar_examen(exam)

    def get_data(self):
        print("\nLos datos del orden son:")
        return(f"Fecha solicitud: {self.fecha_solicitud}\nMédico: {self.medico_tratante}\nNúmero de orden: {self.numero_orden}\nPaciente: {self.paciente}")
