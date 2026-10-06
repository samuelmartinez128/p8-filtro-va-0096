#Samuel Martinez NC 0096 NL=39
#PROBLEMA 2
import cv2

# Cargar imagen
imagen = cv2.imread("imagenes/condorr.jpg")

# Comprobar imagen
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a imagen binaria mediante umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Detectar contornos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar los contornos
resultado = imagen.copy()

cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),
    2
)

# Mostrar resultados
cv2.imshow("condorr0096_original.jpg", imagen)
cv2.imshow("condorr0096_binaria.jpg", binaria)
cv2.imshow(" condorr.jpg Contornos detectados 0096", resultado)

# Guardar resultado
cv2.imwrite(
    "resultado/ejemplo2_condor0096.jpg",
    resultado
)

print("Cantidad de contornos encontrados:", len(contornos))
print("Resultado guardado en resultado/ejemplo2_condor0096.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("+-+-+EJEMPLO 3+-+-+")
#PROBLEMA 3
import cv2

# Cargar imagen
imagen = cv2.imread("imagenes/condorr.jpg")

# Comprobar imagen
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Encontrar contornos externos
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Crear copia
resultado = imagen.copy()

# Contador
cantidad = 0

# Analizar cada contorno
for contorno in contornos:

    # Calcular área
    area = cv2.contourArea(contorno)

    # Ignorar objetos demasiado pequeños
    if area > 500:

        cantidad += 1

        # Dibujar contorno
        cv2.drawContours(
            resultado,
            [contorno],
            -1,
            (0, 255, 0),
            2
        )

        # Obtener rectángulo
        x, y, ancho, alto = cv2.boundingRect(contorno)

        # Dibujar rectángulo
        cv2.rectangle(
            resultado,
            (x, y),
            (x + ancho, y + alto),
            (255, 0, 0),
            2
        )

        # Mostrar número del objeto
        cv2.putText(
            resultado,
            f"Objeto {cantidad}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

# Mostrar resultado
cv2.imshow("Objetos identificados 0096", resultado)

# Guardar
cv2.imwrite(
    "resultado/ejemplo3_objetos_condor0096.jpg",
    resultado
)

print("Objetos identificados:", cantidad)
print("Resultado guardado en resultado/ejemplo3_objetos_condor0096.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar
cv2.destroyAllWindows()
print("Samuel Martinez NC=0096 NL=39")