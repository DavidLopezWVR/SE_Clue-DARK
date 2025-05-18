from motor_juego import iniciar_juego, mostrar_info_lugar, mostrar_info_personaje, mostrar_info_arma
from config import personajes, locaciones, armas

# 🎬 Finales especiales según la combinación exacta de crimen
finales_posibles = {
    ("Jonas", "Reloj de bolsillo alterado", "Búnker del 2052"): {
        "titulo": "El ciclo continúa",
        "descripcion": (
            "Has descubierto al culpable, el arma y el lugar… pero todo esto ya había ocurrido antes.\n"
            "En un rincón del búnker, encuentras un diario que describe con exactitud cada paso que tomaste.\n"
            "El asesino no actuó por voluntad, sino porque el tiempo así lo quiso.\n"
            "Cuando cierras los ojos, una nueva partida empieza… el ciclo no se ha roto."
        )
    },
    ("Noah", "Diario con secretos", "Iglesia abandonada"): {
        "titulo": "El origen del mal",
        "descripcion": (
            "Logras unir las piezas. El asesino era alguien que viajó entre épocas, influenciado por El Origen.\n"
            "Has eliminado la causa que dio inicio al bucle temporal en Winden.\n"
            "Por primera vez, todo está en calma. Pero un niño en 1953 observa el cielo, curioso…\n"
            "el ciclo puede empezar otra vez."
        )
    },
    ("Jugador", "Pistola oxidada", "Bosque de Winden"): {
        "titulo": "El impostor",
        "descripcion": (
            "Todo parece claro. El arma, el lugar, el culpable…\n"
            "Pero cuando confrontas al asesino, te das cuenta de algo terrible:\n"
            "¡Tú mismo eres el asesino! Has estado viajando en el tiempo intentando borrar tu culpa.\n"
            "No lo recuerdas… porque aún no lo has hecho."
        )
    },
    ("Claudia Tiedemann", "Máquina del tiempo rota", "Planta nuclear"): {
        "titulo": "El apocalipsis",
        "descripcion": (
            "Has encontrado al culpable, pero es demasiado tarde.\n"
            "El arma era parte de una máquina: un catalizador temporal.\n"
            "Cuando detonas el dispositivo, los relojes se detienen. Afuera, todo comienza a desintegrarse.\n"
            "Has resuelto el crimen, pero sellado el destino del mundo."
        )
    },
    ("Eva", "Fragmento de materia oscura", "Cuarto blanco"): {
        "titulo": "El mundo intermedio",
        "descripcion": (
            "Después de resolver el caso, una puerta se abre frente a ti.\n"
            "Entras, y ves todas las posibles realidades superpuestas.\n"
            "Tomas una decisión: borrar todos los mundos para evitar el sufrimiento.\n"
            "Nadie recuerda nada. Pero una voz susurra: 'Todo está conectado.'"
        )
    }
}

def mostrar_menu_lugares():
    print("\n🌍 Lugares disponibles para investigar:")
    for idx, lugar in enumerate(locaciones):
        print(f"{idx + 1}. {lugar['nombre']}")
    print("0. Hacer una acusación")

def hacer_acusacion(crimen_real):
    print("\n⚠️ ¡Estás a punto de hacer una acusación! ⚠️")

    # Elegir personaje
    print("\nSospechosos:")
    for i, p in enumerate(personajes):
        print(f"{i + 1}. {p['nombre']}")
    p_idx = int(input("¿Quién crees que fue el culpable? (número): ")) - 1

    # Elegir arma
    print("\nArmas:")
    for i, a in enumerate(armas):
        print(f"{i + 1}. {a['nombre']}")
    a_idx = int(input("¿Con qué arma se cometió el crimen? (número): ")) - 1

    # Elegir lugar
    print("\nLugares:")
    for i, l in enumerate(locaciones):
        print(f"{i + 1}. {l['nombre']}")
    l_idx = int(input("¿Dónde ocurrió el crimen? (número): ")) - 1

    # Verificación
    acierto = (
        personajes[p_idx]['nombre'] == crimen_real['culpable']['nombre'] and
        armas[a_idx]['nombre'] == crimen_real['arma']['nombre'] and
        locaciones[l_idx]['nombre'] == crimen_real['lugar']['nombre']
    )

    if acierto:
        clave_final = (
            personajes[p_idx]['nombre'],
            armas[a_idx]['nombre'],
            locaciones[l_idx]['nombre']
        )

        final = finales_posibles.get(clave_final)

        if final:
            print(f"\n🎬 Final desbloqueado: {final['titulo']}")
            print(final['descripcion'])
        else:
            print("\n🎉 ¡Felicidades! Has resuelto el caso correctamente.")
    else:
        print("\n❌ Fallaste en tu deducción.")
        print("\nEl crimen verdadero fue:")
        mostrar_info_personaje(crimen_real['culpable'])
        mostrar_info_arma(crimen_real['arma'])
        mostrar_info_lugar(crimen_real['lugar'])

def jugar():
    crimen_real = iniciar_juego()

    investigado = []

    while True:
        mostrar_menu_lugares()
        opcion = input("\nElige una opción: ")

        if opcion == "0":
            hacer_acusacion(crimen_real)
            break
        else:
            try:
                idx = int(opcion) - 1
                if 0 <= idx < len(locaciones):
                    lugar = locaciones[idx]
                    if lugar['nombre'] not in investigado:
                        print("\n🕵️ Investigando el lugar...")
                        mostrar_info_lugar(lugar)
                        investigado.append(lugar['nombre'])
                    else:
                        print("⚠️ Ya investigaste este lugar.")
                else:
                    print("❌ Opción inválida.")
            except ValueError:
                print("❌ Ingresa un número válido.")

if __name__ == "__main__":
    jugar()
