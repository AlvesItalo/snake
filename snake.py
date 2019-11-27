import pygame
import random


# Macros
BLOCK = 10

X = 0
Y = 1
STARTY = 20
END = 400

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

GFPS = 10
FPS = 60


def menu():
    fonte = pygame.font.SysFont('Open sans', 32)
    texto1 = fonte.render('1 - Jogar', True, grey)
    texto2 = fonte.render('2 - Ranking', True, grey)
    texto3 = fonte.render('0 - Sair', True, grey)

    caixa_texto1 = texto1.get_rect()
    caixa_texto1.midtop = (180, 170)
    caixa_texto2 = texto1.get_rect()
    caixa_texto2.midtop = (180, 204)
    caixa_texto3 = texto1.get_rect()
    caixa_texto3.midtop = (180, 238)

    display.fill(white)

    display.blit(texto1, caixa_texto1)
    display.blit(texto2, caixa_texto2)
    display.blit(texto3, caixa_texto3)

    pygame.display.flip()
    
    while True:
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return 1
                elif evento.key == pygame.K_2:
                    return 2
                elif evento.key == pygame.K_0:
                    return 0

        fps_clock.tick(FPS)

def game():
    cobra = [[100, 50], [90, 50]]
    maca = nova_maca()
    pontuacao = 0
    velocidade = [10, 0]

    direcao = RIGHT

    while True:
        if (cobra[0][X] < 0 or cobra[0][X] >= 400) or (cobra[0][Y] < 50 or cobra[0][Y] >= 400) or cobra[0] in cobra[1:-1]:
            game_over(pontuacao)
            return pontuacao

        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT and direcao != LEFT:
                    direcao = RIGHT
                elif evento.key == pygame.K_LEFT and direcao != RIGHT:
                    direcao = LEFT
                elif evento.key == pygame.K_UP and direcao != DOWN:
                    direcao = UP
                elif evento.key == pygame.K_DOWN and direcao != UP:
                    direcao = DOWN
        
        if direcao == RIGHT:
            velocidade[X] = BLOCK
            velocidade[Y] = 0
        elif direcao == LEFT:
            velocidade[X] = -BLOCK
            velocidade[Y] = 0
        elif direcao == UP:
            velocidade[X] = 0
            velocidade[Y] = -BLOCK
        elif direcao == DOWN:
            velocidade[X] = 0
            velocidade[Y] = BLOCK
        
        cobra.insert(0, list((cobra[0][X] + velocidade[X], cobra[0][Y] + velocidade[Y])))
        if cobra[0] == maca:
            maca = nova_maca()
            pontuacao += 1
        else:
            cobra.pop()
        
        # Limpa a tela
        display.fill(white)
        desenhar_placar(pontuacao)
        
        for pos in cobra:
            pygame.draw.rect(display,
                             green,
			                 pygame.Rect(pos[X], pos[Y], BLOCK-2, BLOCK-2)
                             )

        pygame.draw.rect(display, brown,
		pygame.Rect(maca[X], maca[Y], BLOCK-2, BLOCK-2))

        pygame.display.flip()
        fps_clock.tick(GFPS)

def exibir_ranking():
    ranking = []
    caixas = []

    display.fill(grey)

    fonte = pygame.font.SysFont('Open sans', 32)

    arquivo = open('ranking.txt', 'r')
    
    i = 100
    for linha in arquivo:
        texto = fonte.render(linha.strip('\n'), True, green)
        caixa_texto = texto.get_rect()

        caixa_texto.midtop = (200, i)
        display.blit(texto, caixa_texto)

        i+= 40

        pygame.display.flip()

    arquivo.close()

    texto = fonte.render('1  - Voltar', True, white)
    caixa_texto = texto.get_rect()

    caixa_texto.midtop = (200, i)
    display.blit(texto, caixa_texto)
    
    pygame.display.flip()
    while True:
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return

        fps_clock.tick(FPS)

def gravar_ranking(nome, pontuacao):
    ranking = []
    nomes = []

    arquivo = open('ranking.txt', 'r')

    for i in range(5):
        linha = arquivo.readline()
        nome_r, pontuacao_r = linha.split()

        if int(pontuacao_r) < pontuacao:
            ranking.append(pontuacao)
            nomes.append(nome)
            ranking.append(pontuacao_r)
            nomes.append(nome_r)
        else:
            ranking.append(pontuacao_r)
            nomes.append(nome_r)
    
    arquivo.close()

    for i in range(5):
        ranking[i] = f'{nomes[i]} {ranking[i]}\n'

    arquivo = open('ranking.txt', 'w')
    for i in range(5):
        arquivo.write(ranking[i])

def nova_maca():
    return [random.randrange(1,40)*10, random.randrange(5,40)*10]

def game_over(pontuacao):
    nome = ''

    fonte = pygame.font.SysFont('Open sans', 32)
    texto = fonte.render('Digite seu nome', True, grey)
    caixa_texto = texto.get_rect()
    caixa_texto.midtop = (180, 170)

    while True:
        display.fill(white)
        display.blit(texto, caixa_texto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    print(nome)
                    gravar_ranking(nome, pontuacao)
                    return
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                else:
                    nome += evento.unicode
                    texto = fonte.render(nome, True, grey)

        pygame.display.flip()
        fps_clock.tick(FPS)

def desenhar_placar(pontuacao):
    pygame.draw.rect(display, grey, pygame.Rect(0,0, 400,50))

    fonte = pygame.font.SysFont('Open sans', 32)
    texto = fonte.render(f'Pontuação: {pontuacao}', True, white)
    caixa_texto = texto.get_rect()
    caixa_texto.midtop = (200, 15)

    display.blit(texto, caixa_texto)


# Color variables:
green = pygame.Color(0, 255, 0)   # Cor da cobra
white = pygame.Color(255, 255, 255)     # Cor de fundo
brown = pygame.Color(165, 42, 42) # Cor da maçã
grey = pygame.Color(50, 50, 50) # Cor do placar

# Display:
display = pygame.display.set_mode((400, 420))
pygame.display.set_caption('Snake')

fps_clock = pygame.time.Clock()

errors = pygame.init()
if(errors[1]):
    print(errors[0]+" errors.")
    sys.exit(-1)
else:
    print("No errors.")

while True:
    opt = menu()

    if opt == 1:
        pontuacao = game()
    elif opt == 2:
        exibir_ranking()
    elif opt == 0:
        quit()
