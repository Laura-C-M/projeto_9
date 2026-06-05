import cv2

# carregar imagem
img = cv2.imread("imagem.png")

# função que captura o clique
def mostrar_coordenadas(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Coordenadas:", x, y)

# criar janela
cv2.imshow("Imagem", img)

# associar função ao rato
cv2.setMouseCallback("Imagem", mostrar_coordenadas)

cv2.waitKey(0)
cv2.destroyAllWindows()