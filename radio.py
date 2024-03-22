
estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}
class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estacoes = estacoes
        self.volume = None
        self.ligado = False
        self.estacao_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self):
        self.ligado = True
        self.volume = self.volume_min
        if self.antena_habilitada:
            primeira_freq = next(iter(self.estacoes))
            self.frequencia_atual = primeira_freq
            self.estacao_atual = self.estacoes[primeira_freq]

    def desligar(self):
        self.ligado = False
        self.volume = None
        self.frequencia_atual = None
        self.estacao_atual = None

    def aumentar_volume(self, incremento=1):
        if self.ligado and self.volume is not None:
            self.volume = min(self.volume + incremento, self.volume_max)

    def diminuir_volume(self, decremento=1):
        if self.ligado and self.volume is not None:
            self.volume = max(self.volume - decremento, self.volume_min)

    def mudar_frequencia(self, frequencia=0):
        if not self.ligado: return

        if frequencia:
            self.frequencia_atual = frequencia
            self.estacao_atual = self.estacoes.get(frequencia, 'estação inexistente')
        else:
            todas_freq = sorted(self.estacoes.keys())
            if self.frequencia_atual in todas_freq:
                indice_atual = todas_freq.index(self.frequencia_atual)
                proximo_indice = (indice_atual + 1) % len(todas_freq)
            else:
                proximo_indice = 0
            nova_freq = todas_freq[proximo_indice]
            self.frequencia_atual = nova_freq
            self.estacao_atual = self.estacoes[nova_freq]

    def habilitar_antena(self):
        self.antena_habilitada = True
        if self.ligado:
            self.ligar()

    def info_atual(self):
        if self.ligado:
            print(f"Ligado: {self.ligado}, Volume: {self.volume}, Frequência: {self.frequencia_atual}, Estação: {self.estacao_atual}")
        else:
            print("O rádio está desligado.")


radio1 = RadioFM(10, estacoes)
radio2 = RadioFM(15, estacoes)
radio3 = RadioFM(20, estacoes)


radio1.habilitar_antena()
radio1.ligar()
radio1.aumentar_volume(3)
radio1.info_atual()
radio1.mudar_frequencia()
radio1.info_atual()

radio2.habilitar_antena()
radio2.ligar()
radio2.aumentar_volume(5)
radio2.diminuir_volume(2)
radio2.mudar_frequencia(91.5)
radio2.info_atual()

radio3.habilitar_antena()
radio3.ligar()
radio3.aumentar_volume()
radio3.diminuir_volume()
radio3.mudar_frequencia(99.1)
radio3.info_atual()
radio3.desligar()
radio3.info_atual()