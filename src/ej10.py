def master_chef():
    
    rounds = [
        {
            'theme': 'Entrada' ,
             'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 8, 'judge_2': 8,'judge_3': 8},
            }
    },
        {

            'theme': 'Plato principal',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            }
    },
        {

            'theme': 'Postre',
            'scores': {
                'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            }
    },
        {

            'theme': 'Cocina internacional',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
                'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
            }
    },
        {

            'theme': 'Final libre',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
                'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
            }
        }
    ]

    acumulado = {}
    rondas_ganadas = {}
    mejores = {}

    for i,ronda in enumerate(rounds, start=1):
        tema = ronda['theme']
        scores = ronda['scores']
        puntajes_ronda = {}
    
        for nombre,jueces in scores.items():
            total = sum(jueces.values())
            puntajes_ronda[nombre] = total

            if nombre in acumulado:
                acumulado[nombre] += total
            else:
                acumulado[nombre] = total

            if nombre not in mejores or total > mejores[nombre]:
                mejores[nombre] = total 

        ganador = max(puntajes_ronda, key=lambda x:puntajes_ronda[x])
        if ganador not in rondas_ganadas:
            rondas_ganadas[ganador] = 1
        else:
            rondas_ganadas[ganador] += 1

         
        ranking = sorted(acumulado.items(), key=lambda x:x[1], reverse = True) 
                 
        print(f'Ronda {i} - {tema}: ')
        print(f' Ganador: {ganador} ({puntajes_ronda[ganador]} pts.)')
        print()
        print(f'Tabla parcial: ')
        print(f'Cocinero          Puntaje  Rondas Ganadas  Mejor Ronda  Promedio')
        print('-----------------------------------------------------------------')

        for nombre, total in ranking:
            ganadas = rondas_ganadas.get(nombre,0)
            mejor = mejores[nombre]
            promedio = total / i

            print(f"{nombre:<18} {total:<8} {ganadas:<15} {mejor:<13} {promedio:.1f}")

        print('-----------------------------------------------------------------')
        print()
        
    
    resultado = []

    for nombre in acumulado:
        total = acumulado[nombre]
        ganadas = rondas_ganadas.get(nombre,0)
        mejor = mejores[nombre]
        promedio = total / len(rounds)

        resultado.append({
            'nombre': nombre,
            'total': total,
            'ganadas': ganadas,
            'mejor': mejor,
            'promedio': promedio
        })

    resultado.sort(key=lambda x: x['total'], reverse = True)
    
    print('Tabla de posiciones final: ')
    print(f'Cocinero          Puntaje  Rondas Ganadas  Mejor Ronda  Promedio')
    print('-----------------------------------------------------------------')    
    for r in resultado:
        print(f"{r['nombre']:<18} {r['total']:<8} {r['ganadas']:<15} {r['mejor']:<13} {r['promedio']:.1f}")
    print('------------------------------------------------------------------')