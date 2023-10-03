class Examen():
    def __init__(self, fecha_cita, fecha_realizacion, observaciones):
        self.fecha_cita = fecha_cita
        self.fecha_realizacion = fecha_realizacion
        self.observaciones = observaciones
    
    def buscar_por_documento(self, cedula):
        pass