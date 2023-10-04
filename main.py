from paciente import Paciente
from medico import Medico
from Orden import Orden
from EntidadSalud import (
    EntidadSalud,
)  # Asegúrate de que el nombre del archivo sea correcto
from EncabezadoFactura import EncabezadoFactura
from DetalleFactura import DetalleFactura


# Crear una lista para almacenar médicos
lista_de_medicos = []

# Agregar médicos a la lista
medico1 = Medico(
    "Cirujano", "Cedula", 100020456, "Andres", "Garcia", "1234", "321896787", "calle 40"
)
medico2 = Medico(
    "Cirujano", "Cedula", 100029999, "Sergio", "Morales", "1234", "32189677", "calle 42"
)

# Agregar los médicos a la lista
lista_de_medicos.append(medico1)
lista_de_medicos.append(medico2)

# Crear una lista para almacenar las entidades de salud
lista_entidades_salud = []


switch = True
menu = "\n***** Laboratorio clínico Konoha SAS *****\n\
1. Realizar examen\n\
2. Consultar factura\n\
3. Médico tratante que más pacientes remitió\n\
4. Consultar paciente por número de documento\n\
5. Orden medico\n\
6. Registrar entidad de salud\n\
7. Registrar un examen\n\
8. Detalle Factura\n\
9. Cerrar la aplicación\n\n"


aux = 0
while switch:
    option = int(input(menu))
    if option == 1:
        tipo_documento = input("Ingrese el tipo de documento, por favor: ")
        numero_documento = int(input("Ingrese el número de documento, por favor: "))
        if aux != numero_documento:
            aux = numero_documento
            nombres = input("Ingrese su nombre, por favor: ")
            apellidos = input("Ingrese sus apellidos, por favor: ")
            telefono = input("Ingrese su teléfono, por favor: ")
            celular = input("Ingrese su celular, por favor: ")
            direccion = input("Ingrese su dirección, por favor: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento, por favor: ")
            email = input("Ingrese su email, por favor: ")
            nombre_pariente = input("Ingrese el nombre del pariente, por favor: ")
            contacto_pariente = input("Ingrese el contacto del pariente, por favor: ")
            pacient = Paciente(
                tipo_documento,
                numero_documento,
                nombres,
                apellidos,
                telefono,
                celular,
                direccion,
                fecha_nacimiento,
                email,
                nombre_pariente,
                contacto_pariente,
            )
            pacient.registrar_paciente(pacient)
        else:
            print("\nEl paciente ya se encuentra registrado")

    elif option == 2:
        print("Consultando factura")
    elif option == 3:
        print("Médico con mas pacientes")
    elif option == 4:
        documento = int(input("Ingrese el número de docuemento, por favor: "))
        print(f"{pacient.buscar_paciente_id(documento)}")
    elif option == 5:
        # Opción para registrar una orden médica
        tipo_documento_medico = input(
            "Ingrese el tipo de documento del médico, por favor: "
        )
        numero_documento_medico = input(
            "Ingrese el número de documento del médico, por favor: "
        )

        # Buscar al médico por su tipo y número de documento
        medico_encontrado = None
        for (
            medico
        ) in (
            lista_de_medicos
        ):  # Reemplaza "lista_de_medicos" con la lista real de médicos
            if (
                medico.get_tipo_documento() == tipo_documento_medico
                and medico.get_numero_documento() == numero_documento_medico
            ):
                medico_encontrado = medico
                break

        if medico_encontrado:
            # Crear una orden médica y registrarla
            orden = Orden(medico_encontrado, Paciente)  # Asigna un ID adecuado
            orden.registrarOrden()
        else:
            print("Médico no encontrado. Verifique los datos ingresados.")

    elif option == 6:
        # Opción para registrar una entidad de salud
        id_entidad = input("Ingrese el ID de la entidad de salud, por favor: ")
        nit = input("Ingrese el NIT de la entidad de salud, por favor: ")
        telefono_entidad = input(
            "Ingrese el teléfono de la entidad de salud, por favor: "
        )
        celular_entidad = input(
            "Ingrese el celular de la entidad de salud, por favor: "
        )
        email_entidad = input("Ingrese el email de la entidad de salud, por favor: ")
        persona_disponible = input(
            "Ingrese el nombre de la persona disponible en la entidad de salud, por favor: "
        )
        celular_persona_disponible = input(
            "Ingrese el celular de la persona disponible, por favor: "
        )
        tipo_EntidadSalud = input("Ingrese el tipo de entidad de salud, por favor: ")

        # Crear una instancia de EntidadSalud y agregarla a la lista
        EntidadSalud = EntidadSalud(
            id_entidad,
            nit,
            telefono_entidad,
            celular_entidad,
            email_entidad,
            persona_disponible,
            celular_persona_disponible,
            tipo_EntidadSalud,
        )
        lista_entidades_salud.append(EntidadSalud)

        print("\nEntidad de salud registrada con éxito.")

    elif option == 7:
        # Opción para registrar un examen
        fecha_cita = input("Ingrese la fecha de la cita para el examen (YYYY-MM-DD): ")
        fecha_realizacion = input(
            "Ingrese la fecha de realización del examen (YYYY-MM-DD): "
        )
        observaciones = input("Ingrese las observaciones relacionadas con el examen: ")

        # Llama al método crear_examenes en la instancia de EncabezadoFactura
        EncabezadoFactura.crear_examenes(
            "Examenes medicos", "2023,09-09", "2023,09-09", "No tiene nada"
        )
    elif option == 8:
        # Opción para registrar un detalle de factura y asociar un examen
        id_detalle = input("Ingrese el ID del detalle de factura: ")

        # Solicita los datos para crear el examen
        tipo_examen = input("Ingrese el tipo de examen: ")
        fecha_cita = input("Ingrese la fecha de la cita para el examen (YYYY-MM-DD): ")
        fecha_realizacion = input(
            "Ingrese la fecha de realización del examen (YYYY-MM-DD): "
        )
        observaciones = input("Ingrese las observaciones relacionadas con el examen: ")

        # Crea un objeto DetalleFactura y llama al método crear_examen
        DetalleFactura = DetalleFactura(id_detalle, None)
        DetalleFactura.crear_examen(fecha_cita, fecha_realizacion, observaciones)

    else:
        switch = False

print("\nCerrando la aplicación...")
