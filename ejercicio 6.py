from abc import ABC, abstractmethod
class RecordatorioHogar(ABC):
    def __init__(self, titulo):
        self.titulo = titulo
        self._archivado = False

    def mostrar_nota(self):
        pass

class NotaPapel(RecordatorioHogar):
    def __init__(self, titulo, color_papel):
        super().__init__(titulo)
        self.color = color_papel

    def mostrar_nota(self):
        return f"Nota de Papel ({self.color}) pegada en el refrigerador: '{self.titulo}'"


class RecordatorioVoz(RecordatorioHogar):
    def __init__(self, titulo):
        super().__init__(titulo)

        self.__archivo_audio = f"audio_{titulo.lower().replace(' ', '_')}.mp3"

    def obtener_nombre_archivo(self):
        """Getter manual para revisar el nombre del archivo encapsulado si lo necesito."""
        return self.__archivo_audio

    def mostrar_nota(self):
        return f"Reproduciendo Recordatorio de Voz desde {self.__archivo_audio}: '¡Atención Eduardo! {self.titulo}'"


mi_pizarra = [
    NotaPapel("Comprar leche y huevos", "Amarillo"),
    RecordatorioVoz("Sacar la basura a las 8 PM")
]

print("Revisando las notas de mi casa ")
for nota in mi_pizarra:
    print(nota.mostrar_nota())
