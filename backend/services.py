def calcular_compatibilidad(programador, oferta):
    # TECNOLOGIAS (60%)
    tecs_oferta = set(oferta.tecnologias)
    tecs_programador = set(programador.tecnologias)
    coincidencias = tecs_oferta & tecs_programador

    if len (tecs_oferta)>0:
        puntos_tecs = (len(coincidencias) / len(tecs_oferta)) * 60
    else:
        puntos_tecs = 60 # si la oferta no requiere tecnologías, puntuación completa

    # EXPERIENCIA (25%)
    minim_exp = oferta.experiencia_minima or 0
    experiencia_cumple = programador.experiencia >= minim_exp
    if minim_exp == 0 or experiencia_cumple:
        puntos_exp = 25
    else:
        puntos_exp = (programador.experiencia/minim_exp) * 25

    # UBICACION (15%)
    ciudad_cumple = programador.ciudad.lower() == oferta.ciudad.lower()
    pais_cumple = programador.pais.lower() == oferta.pais.lower()

    if ciudad_cumple:
        puntos_ciudad = 15
    elif pais_cumple:
        puntos_ciudad = 7
    else:
        puntos_ciudad = 0

    total = round(puntos_tecs + puntos_exp + puntos_ciudad)

    return {
        "porcentaje": total,
        "desglose": {
            "tecnologias_coincidentes": list(coincidencias),
            "tecnologias_faltantes": list(tecs_oferta - tecs_programador),
            "experiencia_cumple": experiencia_cumple,
            "ciudad_cumple": ciudad_cumple,
            "pais_cumple": pais_cumple
        }
    } 