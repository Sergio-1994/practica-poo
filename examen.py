from datetime import datetime

examenes = []
class Examen():
    def __init__(self, observaciones, tipo_examen, id_orden):
        self.fecha_cita = datetime.now()
        self.fecha_realizacion = datetime.now()
        self.observaciones = observaciones
        self.tipo_examen = tipo_examen
        self.id_orden = id_orden
    
    def buscar_por_documento(self, cedula):
        ...


    def registrar_examen(self, examen):
        examenes.append(examen)
        print("\nExamen registrado con éxito")
        print(self.get_data())

        
    def get_data(self):
        print("\nLos datos del examen son:")
        return(f"Fecha del examen: {self.fecha_realizacion}\nObservaciones: {self.observaciones}\nTipo examen: {self.tipo_examen}\nNúmero de la orden: {self.id_orden}")
        