import picamera

# Inicializar la cámara
camera = picamera.PiCamera()

try:
    # Capturar una imagen
    camera.capture('./imagen.jpg')
    print("Imagen capturada con éxito")
finally:
    # Cerrar la cámara
    camera.close()

