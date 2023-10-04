from datetime import datetime

class Orden:
    def __init__(self, medico_tratante, paciente):
        self.id = None  # Debes asignar un ID único, por ejemplo, basado en algún contador
        self.fecha_solicitud = datetime.now()
        self.fecha_ingreso = None
        self.medico_tratante = medico_tratante
        self.numero_orden = None
        self.paciente = paciente

    def registrarOrden(self):
        # Genera un número de orden único, por ejemplo, basado en la fecha y hora actual
        self.numero_orden = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.fecha_ingreso = datetime.now()
        print("Orden registrada con éxito.")
