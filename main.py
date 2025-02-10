import os
import time
import pygame

pygame.init()
diretorio = './sons_do_carro'


def efeito_carregando():
    print("Aguarde", end=' ')
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print()


class Motor:
    def __init__(self):
        self.nome = 'V8 5.0 biturbo'
        self.tipo = 'Esportivo'
        self.potencia = '1.176 cv'
        self.velocidade_maxima = 400
        self.velocidade_atual = 0
        self.ligando = False

    def ligando_motor(self, carro_nome):
        if not self.ligando:
            self.ligando = True
            pygame.mixer.music.load(os.path.join(diretorio, 'ligando_carro.MP3'))
            pygame.mixer.music.play()
            efeito_carregando()
            return f"O {carro_nome} está ligado."
        else:
            return f"O {carro_nome} já está ligado."
    
    def desligando_motor(self,carro_nome):
        if self.ligando:
            self.ligando = False
            efeito_carregando()
            return f'{carro_nome} desligado.'
        else:
            return f'{carro_nome} já está desligado.'


class Carro:
    def __init__(self, motor):
        self.nome = 'Tron'
        self.cor = 'Preto'
        self.ano = 2025
        self.fabricante = 'ByGui'
        self.motor = motor

    def ligar_carro(self):
        return print(self.motor.ligando_motor(self.nome))
    
    def desligar_carro(self):
        return print(self.motor.desligando_motor(self.nome))

    def acelerar(self):
        if self.motor.ligando:
            pygame.mixer.music.load(os.path.join(diretorio, "acelerando_carro.MP3"))
            pygame.mixer.music.play()
            if self.motor.velocidade_atual < self.motor.velocidade_maxima:
                self.motor.velocidade_atual += 10
                if self.motor.velocidade_atual > self.motor.velocidade_maxima:
                    self.motor.velocidade_atual = self.motor.velocidade_maxima
                return print(f'Acelerando... \nVelocidade atual: {self.motor.velocidade_atual} km/h')
            else:
                return print('Velocidade máxima atingida!')
        else:
            return print('Você precisa ligar o carro primeiro!')
    
    def frear(self):
        if self.motor.ligando:
            pygame.mixer.music.load(os.path.join(diretorio, 'frear_carro.MP3'))
            pygame.mixer.music.play()
            if self.motor.velocidade_atual > 0:
                self.motor.velocidade_atual -= 10
                if self.motor.velocidade_atual < 0:
                    self.motor.velocidade_atual = 0
                return print(f'Freando...\nVelocidade atual: {self.motor.velocidade_atual} km/h')
            else:
                return print('O carro já está parado.')
        else:
            return print('Você precisa ligar o carro primeiro!')
    
    def exibir_informacoes(self):
        print(f'Carro: {self.nome}')
        print(f'Ano: {self.ano}')
        print(f'Cor: {self.cor}')
        print(f'Velocidade Máxima: {self.motor.velocidade_maxima} km/h')
        print(f'Motor Ligado: {"Sim" if self.motor.ligando else "Não"}')
        print(f'Velocidade Atual: {self.motor.velocidade_atual} km/h')
motor = Motor()
carro = Carro(motor)

def mostrar_menu():
    os.system('cls')
    print("\033[1;35m" + "╔" + "═" * 58 + "╗")  
    print("\033[1;35m" + f"║\033[1;36m{' MENU DE CONTROLE DO CARRO ':^58}\033[1;35m║")  
    print("\033[1;35m" + "╠" + "═" * 58 + "╣")  
    print("\033[1;32m" + f"║ {'1. Ligar o carro 🚗':<27}{'4. Frear 🛑':<28}║")  
    print("\033[1;32m" + f"║ {'2. Desligar o carro ❌':<27} {'5. Exibir informações ':<29}║") 
    print("\033[1;32m" + f"║ {'3. Acelerar 🚀':<27}{'6. Sair 👋':<28}║")  
    print("\033[1;35m" + "╚" + "═" * 58 + "╝")  
    print("\033[0m")  

while True:
    mostrar_menu()
    try:
        escolha = int(input("Escolha uma opção: "))
    except:
        continue

    match escolha:
        case 1:
            carro.ligar_carro()
        case 2:
            carro.desligar_carro()
        case 3:
            carro.acelerar()
        case 4:
            carro.frear()
        case 5:
            print("Exibindo informações do carro...\n")
            carro.exibir_informacoes()
            input("\nPressione Enter para continuar...")
        case 6:
            print("👋 Saindo do programa... Até mais!")
            break
        case _:
            print("❌ Opção inválida! Por favor, escolha uma opção válida.")
    
    time.sleep(2)
