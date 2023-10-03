from paciente import Paciente

switch = True
menu = "\n***** Laboratorio clínico Konoha SAS *****\n\
1. Realizar examen\n\
2. Consultar factura\n\
3. Médico tratante que más pacientes remitió\n\
4. Consultar paciente por número de documento\n\
5. Cerrar la aplicación\n\n"


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
            pacient = Paciente(tipo_documento, numero_documento, nombres, apellidos, telefono, celular, direccion, fecha_nacimiento, email, nombre_pariente, contacto_pariente)
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
        
    else:
        switch = False

print("\nCerrando la aplicación...")
