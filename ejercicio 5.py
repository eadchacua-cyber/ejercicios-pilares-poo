class MisAudifonos:
    def __init__(self, marca_audifonos):
        self.marca = marca_audifonos
        self.__nivel_volumen = 10
    
    def get_volumen(self):
        """Mi método Getter: Retorna el volumen actual de forma interna."""
        return self.__nivel_volumen

    def set_volumen(self, nuevo_volumen):
        """Mi método Setter: Valido que el volumen no dañe mis oídos (máximo 30)."""
        if 0 <= nuevo_volumen <= 30:
            self.__nivel_volumen = nuevo_volumen
            print(f"Volumen de mis {self.marca} ajustado a: {self.__nivel_volumen}")
        else:
            print(f"¡Cuidado Eduardo! El nivel {nuevo_volumen} es peligroso para mi salud auditiva o es inválido.")

    volumen = property(get_volumen, set_volumen)

mis_cascos = MisAudifonos("Sony")

print(f"Volumen inicial en mi pantalla: {mis_cascos.volumen}")

mis_cascos.volumen = 22 
mis_cascos.volumen = 90