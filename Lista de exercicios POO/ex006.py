# Classe TV

# Nesse programa eu considerei que os canais vão de 0 a 200 e o volume de 0 a 100

class TV:
    def __init__(self, canal=0, volume=0):
        if 0 < canal < 200:
            self.canal = canal
        if 0 < volume < 100:
            self.volume = volume

    def trocar_canal(self, novo_canal):
        if 0 < novo_canal < 200:
            self.canal = novo_canal

    def aumentar_volume(self, novo_volume):
        if novo_volume > self.volume and 0 < novo_volume < 100:
            self.volume = novo_volume

    def diminuir_volume(self, novo_volume):
        if novo_volume < self.volume and 0 < novo_volume < 100:
            self.volume = novo_volume

