#importar a biblioteca do pygame após instalado
import pygame

#inicializar 
pygame.init()
tamanho_tela = (800,800)
#cria a tela do nosso jogo, mas para puxar ela na hora de desenhar, crie a variavel primeiro
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Brick Breaker")

tamanho_bola = 15 
#criando a bola em retangulo(baixo, cima, largura, altura) 
bola = pygame.Rect(100,500,tamanho_bola,tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0, 750, tamanho_jogador, 15)


#quantidade dos blocos
qtde_blocos_linha = 8
qtde_linhas_blocks = 5
qtd_total_blocos = qtde_blocos_linha * qtde_linhas_blocks

def criar_blocos(qtde_blocos_linha, qtde_linhas_blocks):
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    distancia_entre_blocos = 5
    largura_bloco = largura_tela / 8 - distancia_entre_blocos
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10

    blocos = []
    #criar blocos
    for j in range(qtde_linhas_blocks):
        for i in range(qtde_blocos_linha):
            #criar o bloco
            bloco = pygame.Rect( i * (largura_bloco + distancia_entre_blocos), j * distancia_entre_linhas, largura_bloco, altura_bloco) 
            #adicionar o bloco na lista de blocos
            blocos.append(bloco)
        
    return blocos

#cores rgb 
cores = {
    "branca": (255,255,255),
    "preta": (0,0,0),
    "azul": (0,0,255),
    "amarela": (255,255,0),
    "verde": (0,255,0)
}


fim_jogo = False
pontuacao = 0
#velocidade bola(x,y) - ta em list pq ela vai precisar ser editada, uma tupla é imutavel
movimento_bola = [1 , -1]


# criar as funções(movimentações) do jogo
def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            if jogador.x + tamanho_jogador < tamanho_tela[0]:#para não sair da tela
                jogador.x = jogador.x + 1
        if evento.key == pygame.K_LEFT:
            if jogador.x > 0:  
                jogador.x = jogador.x - 1
    

def movimentar_bola(bola):
    #movimentar a bola cru 
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]
    
    #alterar movimento bola 
    if bola.x <= 0: 
        movimento[0] = - movimento[0]#não deixar a bola sair
    if bola.y <= 0: 
        movimento[1] = - movimento[1]
    if bola.x + tamanho_bola >= tamanho_tela[0]: 
        movimento[0] = - movimento[0]
    if bola.y + tamanho_bola >= tamanho_tela[1]:
        movimento = None

    #colisão 
    if jogador.collidepoint(bola.x, bola.y):
        movimento[1] = - movimento[1]
    for bloco in blocos:
        if bloco.collidepoint(bola.x,bola.y):
            blocos.remove(bloco)
            movimento[1] = - movimento[1]
    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None, 30)#fonte none é a padrão
    texto = fonte.render(f"Pontuação: {pontuacao}", 1, cores["amarela"])#o numero é a grossura
    tela.blit(texto, (0,730))#escreve na tela
    if pontuacao >= qtd_total_blocos:
        return True
    else:
        return False

#criar todo o codigo da tela de fim de jogo junto aqui: 
def tela_fim_de_jogo(pontuacao):
    rodando_fim = True#controla o loop da tela final
    
    #fontes 
    fonte_titulo = pygame.font.Font(None, 80)
    fonte_texto = pygame.font.Font(None, 40)
    
    #criar botão (posicao x, y, largura, altura)
    botao = pygame.Rect(300,500,200,60)

    #loop da tela final
    while rodando_fim: 
        tela.fill(cores["preta"])#limpar tela

        #desenhar titulo
        titulo = fonte_titulo.render("FIM DE JOGO", True, cores["branca"])
        tela.blit(titulo, (200, 200))

        #desenhar pontuação final
        texto_pontos = fonte_texto.render(f"Pontos: {pontuacao}", True, cores["amarela"])
        tela.blit(texto_pontos, (300,350))
        #desenhar botão
        pygame.draw.rect(tela, cores["azul"], botao)

        #texto do botão
        texto_botao = fonte_texto.render("SAIR", True, cores["branca"])
        tela.blit(texto_botao, (350, 515))

        #eventos da tela final
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando_fim = False#fechar jogo

            if evento.type == pygame.MOUSEBUTTONDOWN:#clique do mouse
                if botao.collidepoint(evento.pos):#verifica se clicou no botão
                    rodando_fim = False#sair do jogo

        pygame.display.flip()#atualizar tela


# desenhar as coisas na tela
def desenhar_inicio_jogo():#função desenhar na tela
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branca"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela,cores["verde"], bloco)

#rodas as funções

blocos = criar_blocos(qtde_blocos_linha, qtde_linhas_blocks)

# criar um loop infinito para que o jogo funcione normalmente
while not fim_jogo: 
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    fim_jogo = atualizar_pontuacao(qtd_total_blocos - len(blocos))

    #eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
        
    movimentar_jogador(evento)

    movimento_bola = movimentar_bola(bola)# movimento da bola 

    if not movimento_bola:#contando como acaba o jogo
        fim_jogo = True

    pygame.time.wait(1)#para o jogo verificar a cada milissegundo e não ficar estatico
    pygame.display.flip()#atualizar tela

#tela final
tela_fim_de_jogo(qtd_total_blocos - len(blocos))

pygame.quit()#fechar tudo




