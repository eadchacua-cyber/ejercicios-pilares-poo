from abc import ABC, abstractmethod
class Instrumento(ABC):
    def __init__(self, apodo):
        self.apodo = apodo

    @abstractmethod
    def producir_musica(self):
        pass

class MiGuitarra(Instrumento):
    def producir_musica(self):
        return f"Tocando mi {self.apodo}: Rasgueo de cuerdas.Sonando Acorde Sol"

class MiPiano(Instrumento):
    def producir_musica(self):
        return f"Tocando mi {self.apodo}: Presionando teclas.Sonando Melodía Base Clásica "

mi_lira = MiGuitarra("Guitarra Acústica")
mi_teclado = MiPiano("Teclado Casio")

print(mi_lira.producir_musica())
print(mi_teclado.producir_musica())