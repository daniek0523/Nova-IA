import os
import subprocess
import webbrowser
import cv2
import time

# --- Protección de librerías locales de Windows para la nube ---
try:
    import pyautogui
except ImportError:
    pyautogui = None

try:
    import winsound
except ImportError:
    winsound = None


def sonar_alerta(tipo):
    """Genera sonidos de interfaz robótica (solo disponible en Windows local)"""
    if not winsound:
        return
    if tipo == "ok":
        winsound.Beep(2000, 100)
        winsound.Beep(2500, 120)
    elif tipo == "error":
        winsound.Beep(600, 300)
    elif tipo == "escaneo":
        for frec in range(1500, 2500, 200):
            winsound.Beep(frec, 60)


def tomar_foto_nova():
    sonar_alerta("escaneo")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        sonar_alerta("error")
        return "Error: No se pudo acceder a los sensores ópticos, jefe."
    ret, frame = cap.read()
    if ret:
        nombre_archivo = "captura_nova.jpg"
        cv2.imwrite(nombre_archivo, frame)
        cap.release()
        sonar_alerta("ok")
        return f"Captura de cámara realizada. Archivo guardado como '{nombre_archivo}'."
    cap.release()
    sonar_alerta("error")
    return "No se pudo tomar la captura de la cámara."


def escanear_escritorio():
    if not pyautogui:
        return "Acción no disponible en el entorno en la nube."
    sonar_alerta("escaneo")
    nombre_pantalla = "screenshot_nova.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(nombre_pantalla)
    if hasattr(os, "startfile"):
        os.startfile(nombre_pantalla)
    sonar_alerta("ok")
    return f"Escritorio escaneado. Desplegando archivo '{nombre_pantalla}'."


def activar_modo_panico():
    """Oculta todo el laboratorio y pone música para disimular"""
    sonar_alerta("escaneo")
    if pyautogui:
        pyautogui.hotkey("win", "d")
        time.sleep(0.5)

    webbrowser.open("https://open.spotify.com/search/Grupo%20Frontera")
    sonar_alerta("ok")
    return "Modo Pánico activado. Todo oculto y frecuencias musicales de Grupo Frontera desplegadas, jefe."


def activar_modo_tetris():
    """Abre un simulador de Tetris"""
    sonar_alerta("ok")
    webbrowser.open("https://tetris.com/play-tetris")

    try:
        subprocess.Popen(
            [
                "start",
                "cmd",
                "/k",
                "echo === MODO TETRIS TERMINAL === && echo Cargando interfaz...",
            ],
            shell=True,
        )
    except Exception:
        pass

    return "Protocolo Tetris iniciado, jefe. Diviértase en el simulador."


def ejecutar_comando_sistema(texto_comando):
    if not pyautogui:
        return "Comandos de automatización gráfica no disponibles en la nube."

    if "escribe" in texto_comando:
        texto_a_escribir = texto_comando.split("escribe ", 1)[1]
        sonar_alerta("ok")
        time.sleep(2.0)
        pyautogui.write(texto_a_escribir, interval=0.08)
        return "Texto introducido en el sistema."

    elif (
        "cierra la ventana" in texto_comando
        or "cerrar programa" in texto_comando
    ):
        sonar_alerta("escaneo")
        pyautogui.hotkey("alt", "f4")
        return "Ventana activa clausurada, jefe."

    elif (
        "minimizar todo" in texto_comando
        or "pantalla principal" in texto_comando
    ):
        sonar_alerta("ok")
        pyautogui.hotkey("win", "d")
        return "Minimizando todas las ventanas, jefe."

    return None


def execute_action(command_text):
    command_text = command_text.lower()

    # --- Macros Especiales ---
    if (
        "modo panico" in command_text
        or "modo pánico" in command_text
        or "viene mi mamá" in command_text
    ):
        return activar_modo_panico()

    elif (
        "activa el tetris" in command_text or "modo tetris" in command_text
    ):
        return activar_modo_tetris()

    # --- Comandos visuales ---
    elif (
        "activa la visión" in command_text or "toma una foto" in command_text
    ):
        return tomar_foto_nova()
    elif (
        "escanea el escritorio" in command_text
        or "mira mi pantalla" in command_text
    ):
        return escanear_escritorio()

    # --- Control total y macros ---
    elif (
        "escribe" in command_text
        or "minimizar todo" in command_text
        or "cierra la ventana" in command_text
    ):
        return ejecutar_comando_sistema(command_text)

    # --- Programas ---
    elif "abrir spotify" in command_text:
        try:
            subprocess.Popen(["start", "spotify"], shell=True)
        except Exception:
            webbrowser.open("https://open.spotify.com")
        sonar_alerta("ok")
        return "Abriendo Spotify, jefe."
    elif (
        "abrir navegador" in command_text or "buscar en google" in command_text
    ):
        webbrowser.open("https://www.google.com")
        sonar_alerta("ok")
        return "Navegador desplegado."
    elif "abrir youtube" in command_text:
        webbrowser.open("https://www.youtube.com")
        sonar_alerta("ok")
        return "Abriendo YouTube."

    return None