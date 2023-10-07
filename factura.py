from examen import Examen
from datetime import datetime

facturas = []
class Factura:
    def __init__(self, id_factura, total_pagar, paciente, orden):
        self.id_factura = id_factura
        self.total_pagar = total_pagar
        self.fecha_factura = datetime.now()
        self.paciente = paciente
        self.orden = orden
        self.examenes_realizados = []  # Lista para almacenar los exámenes realizados en esta factura
    

    def crear_factura(self,factura):
        facturas.append(factura)

        print("Su examen le genero factura")

    def get_paciente(self):
        return f" Nombre paciente:{self.paciente} \n Total a pagar: {self.total_pagar} "   