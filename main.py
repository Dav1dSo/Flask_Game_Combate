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
        return f"Nome: {self.__nome} \n Vida: {self.__vida} \n Nível: {self.__nivel}"


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return f"{self.__habilidade}"

    def exibe_detalhes(self):
        return f"{super().exibe_detalhes()} \n Habilidade: {self.__habilidade}"


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return f"{self.__tipo}"

    def exibe_detalhes(self):
        return f"{super().exibe_detalhes()} \nTipo: {self.__tipo}"


class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi("Galonilda", 1200, 43, "Atirar ovo")
        self.inimigo = Inimigo("Bob_Esponjo", 4500, 100, "potente")

    def iniciar_jogo(self):
        print(
            "************************************* \n Jogo iniciado! \n************************************* \n"
        )

        print(self.heroi.exibe_detalhes())
        print(self.inimigo.exibe_detalhes())

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print(" \n Escolha uma opção:")
            escolha = input(" 1 - Ataque normal\n 2 - Ataque Potente ")


play = Jogo()
play.iniciar_jogo()
