class Cafetera:
    def __init__(self, marca):
        self.marca = marca
        
        self.__temperatura_agua = 20  
        self.__nivel_agua = 100       

    def encender(self):
        print("Buen dia Eduardo cafetera encendida. iniciando proceso")
        self.__calentar_agua()
        self.__filtrar_cafe()
        print("Es un buen dia para iniciar tomando cafe")

    def __calentar_agua(self):
        self.__temperatura_agua = 90
        print(f"Calentando agua..Temperatura interna: {self.__temperatura_agua}°C")

    def __filtrar_cafe(self):
        self.__nivel_agua -= 20
        print("Pasando el agua caliente por el filtro de café.")

mi_cafetera = Cafetera("Oster")
mi_cafetera.encender()