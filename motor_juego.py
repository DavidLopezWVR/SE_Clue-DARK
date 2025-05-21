# motor_juego.py

from config import personajes, armas, locaciones

# ———————————————————————————————
# 1) Lista de casos predeterminados (5 crímenes)
#    Cada caso usa exactamente los nombres de config.py
#—————————————————————————————————
CRIMENES_PRED = [
    {
        "culpable": next(p for p in personajes if p["nombre"] == "Jonas"),
        "arma":      next(a for a in armas       if a["nombre"] == "Revólver"),
        "lugar":     next(l for l in locaciones  if l["nombre"] == "La cueva"),
        "victima":   next(p for p in personajes if p["nombre"] == "Ulrich"),
        "intro":     "Jonas encontró a Ulrich sin vida en la cueva. Nadie entiende cómo…"
    },
    {
        "culpable": next(p for p in personajes if p["nombre"] == "Martha"),
        "arma":      next(a for a in armas       if a["nombre"] == "Cuerda"),
        "lugar":     next(l for l in locaciones  if l["nombre"] == "El búnker"),
        "victima":   next(p for p in personajes if p["nombre"] == "Noah"),
        "intro":     "Un grito en el búnker alertó a todos: Martha había acabado con Noah."
    },
    {
        "culpable": next(p for p in personajes if p["nombre"] == "Claudia"),
        "arma":      next(a for a in armas       if a["nombre"] == "Estatuilla"),
        "lugar":     next(l for l in locaciones  if l["nombre"] == "La planta nuclear"),
        "victima":   next(p for p in personajes if p["nombre"] == "Martha"),
        "intro":     "Claudia descubrió a Martha muerta junto a una estatuilla en la planta nuclear."
    },
    {
        "culpable": next(p for p in personajes if p["nombre"] == "Noah"),
        "arma":      next(a for a in armas       if a["nombre"] == "Tijeras"),
        "lugar":     next(l for l in locaciones  if l["nombre"] == "Casa de los Doppler"),
        "victima":   next(p for p in personajes if p["nombre"] == "Claudia"),
        "intro":     "Noah atacó a Claudia en la casa de los Doppler con unas tijeras."
    },
    {
        "culpable": next(p for p in personajes if p["nombre"] == "Ulrich"),
        "arma":      next(a for a in armas       if a["nombre"] == "Jeringa con veneno"),
        "lugar":     next(l for l in locaciones  if l["nombre"] == "La iglesia"),
        "victima":   next(p for p in personajes if p["nombre"] == "Jonas"),
        "intro":     "Ulrich envenenó a Jonas en la iglesia. La traición más inesperada."
    },
]

# ———————————————————————————————
# 2) Índice interno para iterar los casos
#—————————————————————————————————
_indice_crimen = 0

# ———————————————————————————————
# 3) Variable global que guarda el caso activo
#—————————————————————————————————
crimen_real = {}

# ———————————————————————————————
def iniciar_juego():
    """
    Selecciona el siguiente caso predeterminado de CRIMENES_PRED,
    actualiza la variable global crimen_real e incluye 'intro'.
    Devuelve el dict crimen_real para usarlo en la interfaz.
    """
    global _indice_crimen, crimen_real

    caso = CRIMENES_PRED[_indice_crimen]
    _indice_crimen = (_indice_crimen + 1) % len(CRIMENES_PRED)

    crimen_real = {
        "culpable": caso["culpable"],
        "arma":      caso["arma"],
        "lugar":     caso["lugar"],
        "victima":   caso["victima"],
        "intro":     caso["intro"]
    }

    return crimen_real

# ———————————————————————————————
def investigar_lugar(nombre_lugar):
    """
    Devuelve la pista (string) al investigar una locación.
    Si coincide con el lugar del crimen actual, muestra evidencia clara.
    Si no, devuelve la pista estática de esa locación.
    """
    loc = next((l for l in locaciones if l["nombre"] == nombre_lugar), None)
    if not loc:
        return f"❌ Lugar '{nombre_lugar}' no encontrado."

    # Si es el lugar del crimen
    if loc["nombre"] == crimen_real["lugar"]["nombre"]:
        return (
            f"EVIDENCIA: ¡El arma '{crimen_real['arma']['nombre']}' fue hallada aquí!\n"
            f"Sospechoso probable: {crimen_real['culpable']['nombre']}"
        )

    # Pista estática
    return loc.get("pista_estatica", "No se encontró nada relevante.")

# ———————————————————————————————
def verificar_acusacion(crimen, acusacion):
    """
    Recibe:
      crimen: dict retornado por iniciar_juego()
      acusacion: {"asesino": str, "arma": str, "lugar": str}
    Devuelve True si todos los elementos coinciden con crimen_real.
    """
    return (
        acusacion.get("asesino") == crimen["culpable"]["nombre"] and
        acusacion.get("arma")    == crimen["arma"]["nombre"]    and
        acusacion.get("lugar")   == crimen["lugar"]["nombre"]
    )
