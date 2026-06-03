import os
import sys
import time
import climage
from nava import play, stop

# Resolve caminho dos assets mesmo dentro do .exe 
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

def mostrar_imagem(caminho_imagem):
    try:
        path = resource_path(caminho_imagem)
        print(climage.convert(path, is_unicode=True))
    except:
        pass

def digitar(texto, velocidade=0.04, cor="\033[0;37m"):
    sys.stdout.write(cor)
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)
    sys.stdout.write("\033[0m\n")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu(opcoes):
    for i, opcao in enumerate(opcoes, 1):
        print(f"\033[1;35m[{i}]\033[0m {opcao}")
    
    while True:
        escolha = input("\n\033[1;35m>\033[0m Escolha: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return int(escolha)
        digitar("Opcao invalida. Tente de novo.", 0.02, "\033[1;31m")

def menu_inicial():
    while True:
        limpar_tela()
        print(r"""
  _____ _ _                      _____  _ _ _
 / ____(_) |                    |  __ \(_) | |
| (___  _| | ___ _ __   ___ ___ | |__) |_| | |
 \___ \| | |/ _ \ '_ \ / __/ _ \|  _  /| | | |
 ____) | | |  __/ | | | (_|  __/| | \ \| | | |
|_____/|_|_|\___|_| |_|\___\___||_|  \_\_|_|_|
""")
        print("\033[0;37mSilence Rill é um lugar que existe entre a memória e o arrependimento.")
        print("Alguns entram por acidente. Outros nunca conseguem sair.\033[0m\n")
        print("\033[1;35m[1]\033[0m Jogar")
        print("\033[1;35m[2]\033[0m Sair\n")
        
        escolha = input("\033[1;35m>\033[0m ").strip()
        
        match escolha:
            case "1":
                introducao()
                break
            case "2":
                limpar_tela()
                digitar("Jogo fechado.", 0.05, "\033[1;35m")
                break

def introducao():
    limpar_tela()
    digitar("Você desperta lentamente, com uma sensação estranha no peito. O ar está frio e pesado. O quarto parece familiar, mas algo está errado.", cor="\033[0;37m")
    time.sleep(1)
    digitar("Sua cabeça dói como se tivesse esquecido algo importante. A porta está trancada e um espelho antigo ocupa a parede à sua frente.", cor="\033[0;37m")
    time.sleep(1)
    
    opcoes = ["Olhar o espelho", "Gritar", "Olhar debaixo da cama"]
    escolha = mostrar_menu(opcoes)
    
    match escolha:
        case 1:
            cena_espelho()
        case 2:
            cena_grito()
        case 3:
            cena_cama()

def cena_espelho():
    limpar_tela()
    mostrar_imagem(resource_path("espelho.avif"))
    digitar("Você se aproxima do espelho coberto por poeira. Cada passo faz o assoalho ranger suavemente.", cor="\033[0;37m")
    time.sleep(1)
    digitar("Por um breve instante, você tem a impressão de que o reflexo se moveu antes de você.\nO seu reflexo está sorrindo, mas você não está.", cor="\033[1;31m")
    time.sleep(1)
    
    opcoes = ["Quebrar o espelho", "Fechar os olhos", "Tocar no vidro"]
    escolha = mostrar_menu(opcoes)
    
    match escolha:
        case 1:
            fim_insanidade()
        case 2:
            cena_quarto_escuro()
        case 3:
            cena_atravessar_espelho()

def cena_atravessar_espelho():
    limpar_tela()
    digitar("Seus dedos afundam no espelho como se fosse água fria.", cor="\033[1;35m")
    time.sleep(1.5)
    digitar("O reflexo puxa seu braço com força extrema.", cor="\033[1;31m")
    time.sleep(1)
    digitar("Você é arrastado para dentro do mundo invertido.", cor="\033[1;31m")
    time.sleep(1.5)
    
    opcoes = ["Explorar o lado invertido", "Tentar voltar imediatamente"]
    escolha = mostrar_menu(opcoes)
    
    match escolha:
        case 1:
            cena_lado_invertido()
        case 2:
            fim_preso_no_reflexo()

def cena_lado_invertido():
    limpar_tela()
    digitar("O outro lado do espelho parece uma versão distorcida da realidade. Tudo é cinza, silencioso e imóvel. O teto parece infinitamente alto.", cor="\033[0;37m")
    time.sleep(1)
    digitar("No centro do cômodo vazio, há uma cadeira com correntes.", cor="\033[0;37m")
    time.sleep(1)
    
    opcoes = ["Sentar na cadeira", "Procurar uma saída nas paredes"]
    escolha = mostrar_menu(opcoes)
    
    match escolha:
        case 1:
            fim_aceitacao()
        case 2:
            cena_porta_secreta()

def cena_porta_secreta():
    limpar_tela()
    digitar("Você tateia as paredes frias e encontra uma maçaneta oculta.", cor="\033[1;32m")
    time.sleep(1)
    digitar("Ao girá-la, uma luz branca intensa cega seus olhos.", cor="\033[1;32m")
    time.sleep(1.5)
    fim_despertar()

def cena_quarto_escuro():
    limpar_tela()
    digitar("Você fecha os olhos e ouve passos.", cor="\033[1;31m")
    time.sleep(1)
    digitar("Quando abre os olhos, a porta está aberta.", cor="\033[1;32m")
    time.sleep(1)
    digitar("Você conseguiu sair do quarto.", cor="\033[1;32m")
    print("\n\033[1;32m--- FIM: A FUGA ---\033[0m")

def cena_grito():
    limpar_tela()
    digitar("Você tenta gritar com todas as suas forças...", cor="\033[0;37m")
    time.sleep(1)
    digitar("Mas o som parece morrer na sua garganta. Nenhum ruído sai.", cor="\033[1;31m")
    time.sleep(1)
    digitar("Do canto escuro do quarto, você ouve um estalo vindo do armário.", cor="\033[1;35m")
    time.sleep(1.5)
    
    opcoes = ["Abrir o armário", "Investigar debaixo da cama"]
    escolha = mostrar_menu(opcoes)
    
    match escolha:
        case 1:
            fim_capturado()
        case 2:
            cena_cama()

def cena_cama():
    limpar_tela()
    digitar("Você se ajoelha e afasta a poeira acumulada sob a cama. O espaço parece mais profundo do que deveria.", cor="\033[0;37m")
    time.sleep(1)
    digitar("Enquanto tateia na escuridão, seus dedos encontram um objeto metálico e gelado. É uma chave antiga de ferro.", cor="\033[1;32m")
    time.sleep(1)
    digitar("Ao lado da chave há um diário empoeirado, com várias páginas desgastadas pelo tempo.", cor="\033[0;37m")
    time.sleep(1.5)
    
    opcoes = ["Usar a chave na porta", "Ler o diario"]
    escolha = mostrar_menu(opcoes)
    
    match escolha:
        case 1:
            cena_porta()
        case 2:
            fim_verdade()

def cena_porta():
    limpar_tela()
    digitar("Você caminha até a porta de madeira pesada.", cor="\033[0;37m")
    time.sleep(1)
    digitar("Insere a chave na fechadura e ela gira com um estalo satisfatório.", cor="\033[1;32m")
    time.sleep(1)
    digitar("Você puxa a porta, mas atrás dela...", cor="\033[1;31m")
    time.sleep(1.5)
    digitar("Existe apenas uma parede de tijolos maciços. Não há saída.", cor="\033[1;31m")
    time.sleep(1.5)
    print("\n\033[1;31m--- FIM: SEM SAÍDA ---\033[0m")


def fim_insanidade():
    limpar_tela()
    digitar("Você quebra o espelho e corta as mãos.", cor="\033[1;31m")
    time.sleep(1)
    print("\n\033[1;31m--- FIM: VOCÊ ENLOQUECEU ---\033[0m")
    stop(musica_jogo)

def fim_capturado():
    limpar_tela()
    digitar("Você abre o armário. Algo te puxa para a escuridão.", cor="\033[1;35m")
    time.sleep(1)
    print("\n\033[1;31m--- FIM: VOCÊ FOI PEGO ---\033[0m")
    stop(musica_jogo)


def fim_verdade():
    limpar_tela()
    digitar("Você abre o diário e reconhece imediatamente a caligrafia. O diário é seu.", cor="\033[1;32m")
    time.sleep(1)
    digitar("As páginas descrevem medo, arrependimento e uma decisão desesperada. No final, está escrito que você se trancou ali de propósito.", cor="\033[1;31m")
    time.sleep(1)
    print("\n\033[1;32m--- FIM: VOCÊ DESCOBRIU A VERDADE ---\033[0m")
    stop(musica_jogo)


def fim_preso_no_reflexo():
    limpar_tela()
    digitar("Você tenta lutar, mas o vidro se solidifica instantaneamente.", cor="\033[1;31m")
    time.sleep(1)
    digitar("Agora você assiste, de dentro do espelho, o seu reflexo controlando o seu corpo real.", cor="\033[1;31m")
    time.sleep(1.5)
    print("\n\033[1;31m--- FIM: TORNANDO-SE O REFLEXO ---\033[0m")
    stop(musica_jogo)

def fim_aceitacao():
    limpar_tela()
    digitar("Você se senta na cadeira. As correntes se prendem sozinhas.", cor="\033[1;35m")
    time.sleep(1)
    digitar("A escuridão te abraça confortavelmente. Você finalmente aceitou seu destino.", cor="\033[1;35m")
    time.sleep(1.5)
    print("\n\033[1;35m--- FIM: ETERNO COMPLACENTE ---\033[0m")
    stop(musica_jogo)

def fim_despertar():
    limpar_tela()
    digitar("Você acorda assustado em sua cama real, suando frio.", cor="\033[1;32m")
    time.sleep(1)
    digitar("Olha ao redor e vê seu quarto normal. Foi tudo um pesadelo.", cor="\033[1;32m")
    time.sleep(1)
    digitar("Mas ao olhar para o lado, a chave brilhante está em cima do criado-mudo.", cor="\033[1;31m")
    time.sleep(2)
    print("\n\033[1;32m--- FIM: ACORDADO? ---\033[0m")
    stop(musica_jogo)
                           

if __name__ == "__main__":
    musica_jogo = play(resource_path("musica.wav"), async_mode=True, loop=True)
    menu_inicial()
