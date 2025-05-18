import random
from config import personajes, locaciones, armas

# Posibles escenas del crimen (puedes agregar más)
introducciones_crimen = [
    "El cuerpo de {victima} fue encontrado en {lugar}, completamente desfigurado.",
    "Una extraña desaparición terminó con el hallazgo del cadáver de {victima} en {lugar}.",
    "{victima} fue hallado sin vida en {lugar}, junto a un misterioso objeto ensangrentado.",
    "Nadie sabe cómo, pero {victima} apareció muerto en {lugar}, sin señales de lucha.",
    "En {lugar} se escuchó un grito… después, {victima} fue hallado muerto sin explicación alguna.",
]


def seleccionar_crimen():
    personaje = random.choice(personajes)
    arma = random.choice(armas)
    lugar = random.choice(locaciones)
    return {
        "culpable": personaje,
        "arma": arma,
        "lugar": lugar
    }

def mostrar_info_personaje(personaje):
    print(f"🔍 Sospechoso: {personaje['nombre']} ({personaje['profesion']})")
    print(f"📅 Edad: {personaje['edad']} | Línea temporal: {personaje['linea_temporal']}")
    print(f"🧬 Afiliación: {personaje['afiliacion']} | Estado: {personaje['estado']}")
    print("-" * 40)

def mostrar_info_lugar(lugar):
    print(f"📍 Lugar: {lugar['nombre']}")
    print(f"🗺️ Descripción: {lugar['descripcion']}")
    print(f"🕵️ Pista encontrada: {lugar['pista']}")
    print("-" * 40)

def mostrar_info_arma(arma):
    print(f"🔪 Arma: {arma['nombre']}")
    print(f"📜 Descripción: {arma['descripcion']}")
    print(f"🕰️ Disponible en: {arma['tiempo']}")
    print("-" * 40)

def iniciar_juego():
    print("\n🌀 BIENVENIDO A 'CLUE: Winden' 🕯️")
    print("El tiempo es confuso. El crimen, aún más...\n")

    # Escoger víctima aleatoria distinta de culpable
    victima = random.choice(personajes)['nombre']
    lugar = random.choice(locaciones)['nombre']
    intro = random.choice(introducciones_crimen).format(victima=victima, lugar=lugar)

    print("🧩 Crimen en Winden:")
    print(intro)
    print("Tu misión: descubrir al asesino, el arma utilizada y el lugar real del crimen.")
    print("-" * 40)

    # Elegimos el crimen real
    culpable = random.choice(personajes)
    arma = random.choice(armas)
    lugar_real = random.choice(locaciones)

    return {
        "culpable": culpable,
        "arma": arma,
        "lugar": lugar_real
    }


# Solo se ejecuta si ejecutas este archivo directamente
if __name__ == "__main__":
    crimen_real = iniciar_juego()
