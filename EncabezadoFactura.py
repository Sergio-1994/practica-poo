from examen import Examen

class EncabezadoFactura:
    def __init__(self, id_factura, total_pagar, fecha_factura, paciente, orden):
        self.id_factura = id_factura
        self.total_pagar = total_pagar
        self.fecha_factura = fecha_factura
        self.paciente = paciente
        self.orden = orden
        self.examenes_realizados = []  # Lista para almacenar los exámenes realizados en esta factura

    def crear_examenes(self, fecha_cita, fecha_realizacion, observaciones):
        """
        Crea un nuevo examen y lo agrega a la lista de examenes_realizados.

        Args:
            fecha_cita (str): La fecha de la cita para el examen.
            fecha_realizacion (str): La fecha en que se realizó el examen.
            observaciones (str): Observaciones relacionadas con el examen.

        Returns:
            None
        """
        # Crear un objeto Examen y agregarlo a la lista de examenes_realizados
        examen = Examen(fecha_cita, fecha_realizacion, observaciones)
        self.examenes_realizados.append(examen)