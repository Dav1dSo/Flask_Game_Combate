class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return f"{self.__nome}"

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return f"{self.__nivel}"

    def exibe_detalhes(self):
        return f"\nNome: {self.__nome} \n Vida: {self.__vida} \n Nível: {self.__nivel} \n"
    
    def recebeAtaque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0 
    
    def ataque(self, alvo):
        dano = self.__nivel * 2
        alvo.recebeAtaque(dano)
        print(f"\n {self.__nome} atacou {alvo.get_nome()} e causou {dano} de dano!")
        
    def ataqueEspecial(self, alvo):
        dano = self.__nivel * 5
        alvo.recebeAtaque(dano) 
        print(f"{self.get_nome()} soltou o especial em {alvo.get_nome()} e causou {dano} de dano!")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return f"{self.__habilidade}"

    def exibe_detalhes(self):
        return f"{super().exibe_detalhes()} Habilidade: {self.__habilidade}"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return f"{self.__tipo}"

    def exibe_detalhes(self):
        print(f"{super().exibe_detalhes()} Tipo: {self.__tipo}")


class Jogo:

    def __init__(self) -> None:
        self.heroi = Heroi("Galonilda", 100, 1,  "Atirar ovo")
        self.inimigo = Inimigo("Bob_Esponjo", 100, 10, "potente")
    print('teste')
    def iniciar_jogo(self):
        print("********* Jogo iniciado! ********* \n")


        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print(self.heroi.exibe_detalhes())
            print(self.inimigo.exibe_detalhes())
            print("\n Escolha uma opção:")
            escolha = input(str(" 1 - Ataque normal\n 2 - Ataque Potente\n"))
            
            if escolha == "1":
                self.heroi.ataque(self.inimigo)
            elif escolha == "2":
                self.heroi.ataqueEspecial(self.inimigo)
            else:
                print("Escolha inválida! Escolha novamente! \n")
                
            if self.inimigo.get_vida() > 0:
                self.inimigo.ataque(self.heroi)
                
        print(f"\nParabéns! Você venceu o {self.inimigo.get_nome()}!")

play = Jogo()
play.iniciar_jogo()
