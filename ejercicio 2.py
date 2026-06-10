class Electrodomestico:
    def __init__(self, marca, voltaje):
        self.marca = marca
        self.voltaje = voltaje
        self.encendido = False

    def presionar_boton_encendido(self):
        self.encendido = not self.encendido
        estado = "Encendido" if self.encendido else "Apagado"
        return f"El aparato {self.marca} ahora está {estado}."

class Televisor(Electrodomestico):
    def __init__(self, marca, voltaje, pulgadas):
        super().__init__(marca, voltaje)
        self.pulgadas = pulgadas
        self.canal_actual = 1

    def cambiar_canal(self, nuevo_canal):
        if self.encendido:
            self.canal_actual = nuevo_canal
            return f"Cambiado al canal {self.canal_actual}."
        return "No se puede cambiar de canal, la TV está apagada."

mi_tele = Televisor("Samsung", 110, 55)
print(mi_tele.presionar_boton_encendido())
print(mi_tele.cambiar_canal(7))