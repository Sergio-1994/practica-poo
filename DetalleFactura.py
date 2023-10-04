from examen import Examen

class DetalleFactura:
    def __init__(self, id_detalle, examen):
        self.id_detalle = id_detalle
        self.examen = examen

    def crear_examen(self,fecha_cita, fecha_realizacion, observaciones):
        """
        Crea un nuevo examen y lo asigna al detalle de factura.

        Args:
            tipo_examen (str): El tipo de examen.
            fecha_cita (str): La fecha de la cita para el examen.
            fecha_realizacion (str): La fecha en que se realizó el examen.
            observaciones (str): Observaciones relacionadas con el examen.

        Returns:
            None
        """
        examen = Examen(fecha_cita, fecha_realizacion, observaciones)
        self.examen = examen
