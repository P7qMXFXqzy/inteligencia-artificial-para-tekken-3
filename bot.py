import pyautogui
import time

#identificar se a luta começou
def esperarLuta():
    retorno = False
    localVida = pyautogui.locateOnScreen("imagens\\lifebarP1.png")
    if(localVida != None):
        print("Luta começou!")
        retorno = True
    return retorno

#identificar se a luta terminou
def identificarFinal():
    retorno = False
    localVida = pyautogui.locateOnScreen("imagens\\playerMorto.png")
    if(localVida != None):
        print("Luta acabou!")
        retorno = True
    return retorno

#método que executará os combos do personagem, cada "comandoEscolhido" é um combo diferente do personagem
def mover():
    from random import randrange
    cancel = 0
    while cancel < 3:
        comandoEscolhido = randrange(11)
        pyautogui.keyUp("j")
        if(comandoEscolhido == 0):
            pyautogui.keyDown("z")
            time.sleep(0.01)
            pyautogui.keyUp("z")
            time.sleep(0.01)
            pyautogui.keyDown("z")
            time.sleep(0.01)
            pyautogui.keyUp("z")
            time.sleep(0.01)
            pyautogui.keyDown("z")
            time.sleep(0.01)
            pyautogui.keyUp("z")
            time.sleep(0.01)
            pyautogui.keyDown("x")
            time.sleep(0.01)
            pyautogui.keyUp("x")
            time.sleep(0.01)
            pyautogui.keyDown("x")
            time.sleep(0.01)
            pyautogui.keyUp("x")
            time.sleep(0.8)
            rotas = randrange(6)
            if(rotas == 0):
                pyautogui.keyDown("s")
                time.sleep(0.01)
                pyautogui.keyUp("s")
            elif(rotas == 1):
                pyautogui.keyDown("j")
                pyautogui.keyDown("x")
                time.sleep(0.01)
                pyautogui.keyUp("j")
                pyautogui.keyUp("x")
                time.sleep(0.8)
                pyautogui.keyDown("s")
                time.sleep(0.01)
                pyautogui.keyUp("s")
            elif(rotas == 2):
                pyautogui.keyDown("z")
                time.sleep(0.01)
                pyautogui.keyUp("z")
                time.sleep(0.01)
                pyautogui.keyDown("z")
                time.sleep(0.01)
                pyautogui.keyUp("z")
            elif(rotas == 3):
                pyautogui.keyDown("l")
                pyautogui.keyDown("z")
                time.sleep(0.01)
                pyautogui.keyUp("l")
                pyautogui.keyUp("z")
                time.sleep(0.2)
                pyautogui.keyDown("x")
                time.sleep(0.01)
                pyautogui.keyUp("x")
            elif(rotas == 4):
                pyautogui.keyDown("x")
                time.sleep(0.01)
                pyautogui.keyUp("x")
                time.sleep(0.02)
                pyautogui.keyDown("x")
                time.sleep(0.01)
                pyautogui.keyUp("x")
            elif(rotas == 5):
                pyautogui.keyDown("l")
                pyautogui.keyDown("z")
                time.sleep(0.01)
                pyautogui.keyUp("l")
                pyautogui.keyUp("z")
                time.sleep(0.2)
                pyautogui.keyDown("v")
                time.sleep(0.01)
                pyautogui.keyUp("v")
                time.sleep(0.01)
                pyautogui.keyDown("v")
                time.sleep(0.01)
                pyautogui.keyUp("v")
                time.sleep(0.01)
                pyautogui.keyDown("z")
                time.sleep(0.3)
                pyautogui.keyDown("x")
                pyautogui.keyUp("z")
                time.sleep(0.01)
                pyautogui.keyUp("x")
                time.sleep(0.03)
                pyautogui.keyDown("z")
                time.sleep(0.01)
                pyautogui.keyUp("z")
                time.sleep(0.2)
                pyautogui.keyDown("x")
                time.sleep(0.01)
                pyautogui.keyUp("x")
                time.sleep(0.8)
                pyautogui.keyDown("x")
                time.sleep(0.01)
                pyautogui.keyUp("x")
                time.sleep(0.1)
                pyautogui.keyDown("x")
                time.sleep(0.01)
                pyautogui.keyUp("x")
                time.sleep(0.5)
                pyautogui.keyDown("x")
                time.sleep(0.01)
                pyautogui.keyUp("x")
        elif(comandoEscolhido == 1):
            pyautogui.keyDown("c")
            time.sleep(0.01)
            pyautogui.keyDown("v")
            pyautogui.keyUp("c")
            time.sleep(0.01)
            pyautogui.keyDown("z")
            pyautogui.keyUp("v")
            time.sleep(0.01)
            pyautogui.keyUp("z")
        elif(comandoEscolhido == 2):
            pyautogui.keyDown("z")
            time.sleep(0.001)
            pyautogui.keyUp("z")
            pyautogui.keyDown("z")
            time.sleep(0.001)
            pyautogui.keyUp("z")
            pyautogui.keyDown("z")
            time.sleep(0.001)
            pyautogui.keyUp("z")
            pyautogui.keyDown("z")
            time.sleep(0.001)
            pyautogui.keyUp("z")
        elif(comandoEscolhido == 3):
            pyautogui.keyDown("i")
            time.sleep(0.001)
            pyautogui.keyDown("x")
            pyautogui.keyUp("i")
            time.sleep(0.01)
            pyautogui.keyUp("x")
        elif(comandoEscolhido == 4):
            pyautogui.keyDown("i")
            time.sleep(0.001)
            pyautogui.keyDown("z")
            pyautogui.keyUp("i")
            time.sleep(0.01)
            pyautogui.keyUp("z")
        elif(comandoEscolhido == 5):
            pyautogui.keyDown("i")
            time.sleep(0.01)
            pyautogui.keyUp("i")
            time.sleep(0.2)
            pyautogui.keyDown("d")
            time.sleep(0.01)
            pyautogui.keyUp("d")
        elif(comandoEscolhido == 6):
            pyautogui.keyDown("k")
            time.sleep(0.01)
            pyautogui.keyUp("k")
            time.sleep(0.3)
            pyautogui.keyDown("f")
            time.sleep(0.01)
            pyautogui.keyUp("f")
        elif(comandoEscolhido == 7):
            pyautogui.keyDown("l")
            time.sleep(0.01)
            pyautogui.keyUp("l")
            time.sleep(0.01)
            pyautogui.keyDown("l")
            pyautogui.keyDown("z")
            time.sleep(0.01)
            pyautogui.keyUp("l")
            pyautogui.keyUp("z")
        elif(comandoEscolhido == 8):
            pyautogui.keyDown("l")
            time.sleep(0.01)
            pyautogui.keyUp("l")
            time.sleep(0.01)
            pyautogui.keyDown("l")
            pyautogui.keyDown("x")
            time.sleep(0.01)
            pyautogui.keyUp("l")
            pyautogui.keyUp("x")
        elif(comandoEscolhido == 9):
            pyautogui.keyDown("l")
            pyautogui.keyDown("i")
            pyautogui.keyDown("z")
            time.sleep(0.01)
            pyautogui.keyDown("x")
            pyautogui.keyUp("l")
            pyautogui.keyUp("i")
            pyautogui.keyUp("z")
            time.sleep(0.01)
            pyautogui.keyDown("z")
            pyautogui.keyUp("x")
            time.sleep(0.01)
            pyautogui.keyUp("z")
        elif(comandoEscolhido == 10):
            pyautogui.keyDown("k")
            pyautogui.keyDown("z")
            time.sleep(0.01)
            pyautogui.keyUp("k")
            pyautogui.keyUp("z")
        cancel = cancel + 1
        if cancel == 10:
            pyautogui.keyDown("j")

def loopPrincipal():
    lutaAcabou = False
    print("esperando luta...")
    while lutaAcabou == False:
        while esperarLuta() == False:
            time.sleep(0.1)
        pyautogui.keyDown("j")
        while identificarFinal() == False:
            pyautogui.keyUp("j")
            mover()
            pyautogui.keyDown("j")
        encerrar = input("Jogar mais uma vez? (s/n)")
        while(not(encerrar == "s") and not(encerrar == "n")):
            print(encerrar)
            print("escolha inválida!")
            encerrar = input("Jogar mais uma vez? (s/n)")
        if(encerrar == "n"):
            lutaAcabou = True
        pyautogui.keyUp("j")
loopPrincipal()