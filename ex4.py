import cv2

# Carrega a imagem do disco
# Certifique-se de que 'imagem.png' está no mesmo diretório ou forneça o caminho completo
img = cv2.imread("imagem.png")

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho do ficheiro.")
else:
    # Desenha um retângulo na imagem
    # Argumentos: imagem, canto superior esquerdo (x1, y1), canto inferior direito (x2, y2),
    # cor (BGR - Azul, Verde, Vermelho), espessura da linha
    cv2.rectangle(img, (544, 369), (1011, 681), (0, 255, 0), 3)

    # Exibe a imagem com o retângulo desenhado
    cv2.imshow("Retangulo", img)

    # Espera indefinidamente por uma tecla ser pressionada
    cv2.waitKey(0)

    # Destrói todas as janelas criadas pelo OpenCV
    cv2.destroyAllWindows()