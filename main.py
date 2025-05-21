# main.py

from interfaz import pantalla_inicio, pantalla_mision, pantalla_acusacion
from motor_juego import iniciar_juego

if __name__ == "__main__":
    while True:
        accion = pantalla_inicio()
        if accion == "iniciar":
            crimen = iniciar_juego()
            accion_mision = pantalla_mision(crimen)
            if accion_mision == "acusar":
                pantalla_acusacion(crimen)
            # Al terminar, el bucle regresa a la pantalla de inicio para un nuevo caso
        else:
            # Si el usuario pulsa “Salir” en la pantalla de inicio, salimos del juego
            break
