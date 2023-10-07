

entidad_salud = []
class EntidadSalud:
    def __init__(self, id_entidad, nit, telefono, celular, email, persona_disponible, celular_persona_disponible, tipo_entidad_salud):
        self.id_entidad = id_entidad
        self.nit = nit
        self.telefono = telefono
        self.celular = celular
        self.email = email
        self.persona_disponible = persona_disponible
        self.celular_persona_disponible = celular_persona_disponible
        self.tipo_entidad_salud = tipo_entidad_salud
    
    

    def to_string(self):
        return f"ID Entidad: {self.id_entidad}\nNIT: {self.nit}\nTeléfono: {self.telefono}\nCelular: {self.celular}\nEmail: {self.email}\nPersona Disponible: {self.persona_disponible}\nCelular Persona Disponible: {self.celular_persona_disponible}\nTipo Entidad Salud: {self.tipo_entidad_salud}"

EntidadSalud1 = EntidadSalud(123,12,434,302,'savisalud@gmail','Juan',123,'publica')

EntidadSalud2 = EntidadSalud(124,21,444,322,'savisalud@gmail','Marta',124,'publica')
