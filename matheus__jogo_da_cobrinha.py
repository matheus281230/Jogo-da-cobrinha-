import pygame
import random

largura_tela = 800
altura_tela = 500
lado_quadrado = 20
fps = 10

COR_FUNDO = "#121212"
COR_COBRA_CORPO = "#F39C12"
COR_COBRA_BORDA = "#D35400"
COR_COMIDA = "#9B59B6"

def gerar_comida():
    x = random.randrange(0, largura_tela, lado_quadrado)
    y = random.randrange(0, altura_tela, lado_quadrado)
    return x, y

def reiniciar():
    global xq, yq, move_x, move_y, corpo_cobra, tamanho_cobra, comida_x, comida_y
    xq = (largura_tela // 2 // lado_quadrado) * lado_quadrado
    yq = (altura_tela // 2 // lado_quadrado) * lado_quadrado
    move_x, move_y = 0, 0
    corpo_cobra = []
    tamanho_cobra = 1
    comida_x, comida_y = gerar_comida()

def desenhar_placar(tela, pontos):
    fonte = pygame.font.SysFont("Arial", 25, bold=True)
    texto = f"Pontos: {pontos - 1}"
    imagem_texto = fonte.render(texto, True, "#FFFFFF")
    tela.blit(imagem_texto, (10, 10))

pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("jogo da cobrinha - Matheus")
relogio = pygame.time.Clock()

rodando = True
reiniciar()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and move_y == 0:
                move_x, move_y = 0, -lado_quadrado
            elif evento.key == pygame.K_DOWN and move_y == 0:
                move_x, move_y = 0, lado_quadrado
            elif evento.key == pygame.K_LEFT and move_x == 0:
                move_x, move_y = -lado_quadrado, 0
            elif evento.key == pygame.K_RIGHT and move_x == 0:
                move_x, move_y = lado_quadrado, 0
            elif evento.key == pygame.K_ESCAPE:
                rodando = False

    if move_x != 0 or move_y != 0:
        xq += move_x
        yq += move_y

        if xq < 0 or xq >= largura_tela or yq < 0 or yq >= altura_tela:
            reiniciar()
        
        if xq == comida_x and yq == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        cabeca = [xq, yq]
        if cabeca in corpo_cobra:
            reiniciar()
        else:
            corpo_cobra.append(cabeca)
            if len(corpo_cobra) > tamanho_cobra:
                del corpo_cobra[0]

    tela.fill(COR_FUNDO)

    pygame.draw.rect(tela, COR_COMIDA, (comida_x, comida_y, lado_quadrado, lado_quadrado))

    for pedaco in corpo_cobra:
        pygame.draw.rect(tela, COR_COBRA_CORPO, (pedaco[0], pedaco[1], lado_quadrado, lado_quadrado))
        pygame.draw.rect(tela, COR_COBRA_BORDA, (pedaco[0], pedaco[1], lado_quadrado, lado_quadrado), 1)

    desenhar_placar(tela, tamanho_cobra)
    
    pygame.display.flip()
    relogio.tick(fps)

pygame.quit()
