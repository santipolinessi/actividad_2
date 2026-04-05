def alumnos():
    
    students_limpios = []
    mejores = {}
    
    students = [
        {"name": "  Ana García ", "grade": "8", "status": "aprobado"},
        {"name": "pedro lópez", "grade": "4", "status": "DESAPROBADO"},
        {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status": "Aprobado"},
        {"name": "ana garcía", "grade": "9", "status": "aprobado"},
        {"name": None, "grade": "7", "status": "aprobado"},
        {"name": "Luis Martínez  ", "grade": None, "status": "aprobado"},
        {"name": " carlos RUIZ", "grade": "6", "status": "aprobado"},
        {"name": "PEDRO LÓPEZ ", "grade": "3", "status": "desaprobado"},
        {"name": "  ", "grade": "5", "status": "aprobado"},
        {"name": "María Fernández", "grade": "7", "status": "APROBADO"},
        {"name": "Sofía Torres", "grade": "9", "status": "Aprobado"},
        {"name": "  sofía torres ", "grade": "8", "status": "aprobado"},
        {"name": "Carlos Ruiz", "grade": "6", "status": "APROBADO"},
        {"name": "Roberto Díaz", "grade": "absent", "status": "ausente"},
        {"name": "roberto díaz", "grade": "", "status": "Ausente"},
        {"name": None, "grade": None, "status": None},
        {"name": "Laura Méndez", "grade": "7", "status": "aprobado"},
        {"name": "  laura méndez", "grade": "8", "status": "Aprobado"},
        {"name": "GABRIELA RÍOS", "grade": "5", "status": "aprobado"},
        {"name": "gabriela ríos ", "grade": "4", "status": "Desaprobado"},
    ]

    for estudiante in students:
        nombre = estudiante['name']
        nota = estudiante['grade']
        estado = estudiante['status']
        
        if nombre is None or nombre.strip() == '':  #el strip le saca espacios y el != ve que no sea vacio
            continue

        if nota is None or not nota.isdigit() or nota == '':
            continue

        nombre = nombre.strip().title()
        estado = estado.strip().title()
        nota = int(nota)

        students_limpios.append({
            'name':nombre,
            'grade':nota,
            'status':estado
        })

    for alumno in students_limpios:
        nombre = alumno['name']
        nota = alumno['grade']

        if nombre not in mejores or nota > mejores[nombre]['grade']:
            mejores[nombre] = alumno

    resultado = list(mejores.values())
    resultado_ordenado = sorted(resultado, key=lambda x: x['name'])
        
    print('Registros limpios de alumnos:')
    print('Nombre               Nota       Estado')
    print('--------------------------------------')
    contador = 0
    for a in resultado_ordenado:
        contador += 1
        print(f'{a['name']:<20} {a['grade']:<5} {a['status']}')
        
    print()
    print('Total de alumnos validos: ',contador)