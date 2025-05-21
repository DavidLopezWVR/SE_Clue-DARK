# interfaz.py

import pygame
import sys
from config import personajes, armas, locaciones
from motor_juego import iniciar_juego, investigar_lugar, verificar_acusacion

# ----------------------------
# 1) Diccionario de finales
# ----------------------------
finales_posibles = {
    ("Jonas", "Revólver", "La cueva"): {
        "titulo": "El ciclo continúa",
        "descripcion": (
            "Has descubierto al culpable, el arma y el lugar… pero todo esto ya había ocurrido antes.\n"
            "En un rincón del búnker, encuentras un diario que describe con exactitud cada paso que tomaste.\n"
            "El asesino no actuó por voluntad, sino porque el tiempo así lo quiso.\n"
            "Cuando cierras los ojos, una nueva partida empieza… el ciclo no se ha roto."
        )
    },
    ("Martha", "Cuerda", "El búnker"): {
        "titulo": "El origen del mal",
        "descripcion": (
            "Logras unir las piezas. El asesino era alguien que viajó entre épocas, influenciado por El Origen.\n"
            "Has eliminado la causa que dio inicio al bucle temporal en Winden.\n"
            "Por primera vez, todo está en calma. Pero un niño en 1953 observa el cielo, curioso…\n"
            "el ciclo puede empezar otra vez."
        )
    },
    ("Claudia", "Estatuilla", "La planta nuclear"): {
        "titulo": "El impostor",
        "descripcion": (
            "Todo parece claro. El arma, el lugar, el culpable…\n"
            "Pero cuando confrontas al asesino, te das cuenta de algo terrible:\n"
            "¡Tú mismo eres el asesino! Has estado viajando en el tiempo intentando borrar tu culpa.\n"
            "No lo recuerdas… porque aún no lo has hecho."
        )
    },
    ("Noah", "Tijeras", "Casa de los Doppler"): {
        "titulo": "El apocalipsis",
        "descripcion": (
            "Has encontrado al culpable, pero es demasiado tarde.\n"
            "El arma era parte de una máquina: un catalizador temporal.\n"
            "Cuando detonas el dispositivo, los relojes se detienen. Afuera, todo comienza a desintegrarse.\n"
            "Has resuelto el crimen, pero sellado el destino del mundo."
        )
    },
    ("Ulrich", "Jeringa con veneno", "La iglesia"): {
        "titulo": "El mundo intermedio",
        "descripcion": (
            "Después de resolver el caso, una puerta se abre frente a ti.\n"
            "Entras, y ves todas las posibles realidades superpuestas.\n"
            "Tomas una decisión: borrar todos los mundos para evitar el sufrimiento.\n"
            "Nadie recuerda nada. Pero una voz susurra: 'Todo está conectado.'"
        )
    }
}

# ----------------------------
# 2) Inicializar Pygame
# ----------------------------
pygame.init()
ANCHO, ALTO = 800, 1000                                    # ← Tamaño de la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("CLUE: DARK - Winden")

# Colores
BLANCO       = (255, 255, 255)
NEGRO        = (  0,   0,   0)
GRIS_OSCURO  = ( 30,  30,  30)
AZUL         = ( 70, 130, 180)
AZUL_CLARO   = (135, 206, 250)
ROJO         = (180,  50,  50)
ROJO_CLARO   = (210,  80,  80)

# Fuentes
fuente_titulo = pygame.font.SysFont("arial", 52, bold=True)  # ← Tamaño del texto de título
fuente_sub    = pygame.font.SysFont("arial", 24)            # ← Tamaño del texto secundario
fuente_btn    = pygame.font.SysFont("impact", 30)            # ← Tamaño del texto en botones
fuente_texto  = pygame.font.SysFont("arial", 24)            # ← Tamaño del texto de pistas

# ----------------------------
# 3) Función de botón
# ----------------------------
def boton(texto, rect, col_norm, col_hover, mouse, clic, fuente=fuente_btn):
    x, y, w, h = rect
    # rect = (x, y, w, h): Defines posición y tamaño del botón
    over = pygame.Rect(rect).collidepoint(mouse)
    color = col_hover if over else col_norm
    pygame.draw.rect(ventana, color, rect, border_radius=12)
    surf = fuente.render(texto, True, BLANCO)
    ventana.blit(surf, surf.get_rect(center=(x + w//2, y + h//2)))  # ← Centrado dentro del rect
    return over and clic[0]

# ----------------------------
# 4) Pantalla de Inicio
# ----------------------------
def pantalla_inicio():
    bg = pygame.image.load("Multi/Fondo_1.jpg").convert()
    bg = pygame.transform.scale(bg, (ANCHO, ALTO))  # ← Escalar fondo al tamaño de ventana

    clock = pygame.time.Clock()
    while True:
        mouse = pygame.mouse.get_pos()
        clic  = pygame.mouse.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        ventana.blit(bg, (0, 0))  # ← Posición (0,0) para cubrir toda la ventana
        tit = fuente_titulo.render("🌀 CLUE: DARK - Winden", True, BLANCO)
        #ventana.blit(tit, (ANCHO//2 - tit.get_width()//2, 100))  # ← Centrar horizontal, y=100

        # Botones con rect = (x, y, ancho, alto)
        if boton("Iniciar Juego", (ANCHO//2 - 150, 300, 300, 60), AZUL, AZUL_CLARO, mouse, clic):
            return "iniciar"
        if boton("Salir",           (ANCHO//2 - 150, 400, 300, 60), ROJO, ROJO_CLARO, mouse, clic):
            pygame.quit(); sys.exit()

        pygame.display.flip()
        clock.tick(60)

# ----------------------------
# 5) Pantalla de Misión
# ----------------------------
def pantalla_mision(crimen_real):
    # Cargar y escalar fondo
    bg = pygame.image.load("Multi/Fondo_2.jpg").convert()
    bg = pygame.transform.scale(bg, (ANCHO, ALTO))

    clock = pygame.time.Clock()
    intro  = crimen_real["intro"]
    mision = "Tu misión: descubrir culpable, arma y lugar correcto."

    # Botones de locaciones (no cambian)
    botones = []
    margen_y, sep = 300, 80
    for i, loc in enumerate(locaciones[:3]):
        botones.append((loc["nombre"], (50, margen_y + i*sep, 350, 60)))
    for i, loc in enumerate(locaciones[3:]):
        botones.append((loc["nombre"], (ANCHO - 400, margen_y + i*sep, 350, 60)))

    # Botón “Investigar” y “Salir del juego”
    rect_investigar = (ANCHO//2 - 100, ALTO - 160, 200, 50)
    rect_salir     = (ANCHO//2 - 150, ALTO - 100,  300, 60)

    pista = ""
    while True:
        mouse = pygame.mouse.get_pos()
        clic  = pygame.mouse.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        ventana.blit(bg, (0, 0))

        # Títulos y descripción
        ventana.blit(fuente_titulo.render("Misión en Winden", True, BLANCO),
                     (ANCHO//2 - 200, 5))
        ventana.blit(fuente_sub.render(intro, True, BLANCO),
                     (50, 160))
        ventana.blit(fuente_sub.render(mision, True, BLANCO),
                     (50, 190))

        # Botones de locaciones
        for nombre, rect in botones:
            if boton(nombre, rect, AZUL, AZUL_CLARO, mouse, clic):
                pista = investigar_lugar(nombre)

        # Botón Investigar
        if boton("Acusar", rect_investigar, AZUL, AZUL_CLARO, mouse, clic):
            return "acusar"


        # Botón Salir del juego
        if boton("Salir del juego", rect_salir, ROJO, ROJO_CLARO, mouse, clic):
            pygame.quit(); sys.exit()

        # Mostrar pista
        if pista:
            for idx, line in enumerate(pista.split("\n")):
                ventana.blit(fuente_texto.render(line, True, BLANCO),
                             (50, ALTO - 350 + idx*30))

        pygame.display.flip()
        clock.tick(60)

# ----------------------------
# 6) Selección genérica (Sospechoso / Arma / Lugar)
# ----------------------------
def pantalla_seleccionar(items, title):
    clock = pygame.time.Clock()
    botones = []
    mx, my = 50, 120                                       # ← margen inicial para selección
    for idx, item in enumerate(items):
        x = mx + (idx % 2)*370                             # ← dos columnas
        y = my + (idx//2)*100                              # ← separación vertical
        botones.append((item["nombre"], (x, y, 340, 60)))  # ← tamaño de botón

    while True:
        mouse = pygame.mouse.get_pos()
        clic  = pygame.mouse.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        ventana.fill(GRIS_OSCURO)
        header = fuente_titulo.render(title, True, BLANCO)
        ventana.blit(header, (ANCHO//2 - header.get_width()//2, 20))  # ← header centrado

        for nombre, rect in botones:
            if boton(nombre, rect, AZUL, AZUL_CLARO, mouse, clic):
                return nombre

        pygame.display.flip()
        clock.tick(60)

# ----------------------------
# 7) Pantalla de Acusación y Resultado
# ----------------------------
def pantalla_acusacion(crimen_real):
    # 1) Selección de sospechoso
    culp = pantalla_seleccionar(personajes, "Selecciona Sospechoso")
    
    # 2) Selección de arma
    arma = pantalla_seleccionar(armas, "Selecciona Arma")
    
    # 3) Selección de lugar
    lugar = pantalla_seleccionar(locaciones, "Selecciona Lugar")

    # 4) Validación de las tres elecciones
    correcto = verificar_acusacion(
        crimen_real,
        {"asesino": culp, "arma": arma, "lugar": lugar}
    )
        
    ventana.fill(GRIS_OSCURO)
    if correcto:
        clave = (culp, arma, lugar)
        final = finales_posibles.get(clave)
        if final:
            # Final especial
            titulo = fuente_titulo.render(final["titulo"], True, AZUL_CLARO)
            ventana.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 200))
            for i, line in enumerate(final["descripcion"].split("\n")):
                ventana.blit(
                    fuente_texto.render(line, True, BLANCO),
                    (50, 280 + i*30)
                )
        else:
            # Final genérico de victoria
            msg = fuente_titulo.render("🎉 ¡Has resuelto el caso!", True, AZUL_CLARO)
            ventana.blit(msg, (ANCHO//2 - msg.get_width()//2, ALTO//2 - 20))
    else:
        # Error en la acusación
        msg = fuente_titulo.render("❌ Acusación incorrecta...", True, ROJO_CLARO)
        ventana.blit(msg, (ANCHO//2 - msg.get_width()//2, ALTO//2 - 20))
        # Mostrar la combinación real
        real = crimen_real
        detalle = (
            f"Real: {real['culpable']['nombre']}  /  "
            f"{real['arma']['nombre']}  /  "
            f"{real['lugar']['nombre']}"
        )
        ventana.blit(
            fuente_sub.render(detalle, True, BLANCO),
            (ANCHO//2 - fuente_sub.size(detalle)[0]//2, ALTO//2 + 40)
        )
    
    pygame.display.flip()
    pygame.time.wait(4000)

# ----------------------------
# 8) Flujo principal
# ----------------------------
if __name__ == "__main__":
    while True:
        accion = pantalla_inicio()
        if accion == "iniciar":
            crimen = iniciar_juego()
            pantalla_mision(crimen)
            pantalla_acusacion(crimen)
        else:
            break