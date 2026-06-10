class MiSmartTV:
    def subir_volumen(self):
        return "SmartTV: Subiendo volumen en pantalla. Nivel [12]"

class MiEquipoAudio:
    def subir_volumen(self):
        return "Equipo de Audio: Subiendo potenciómetro físico y encendiendo luces LED."

class MisAudifonos:
    def subir_volumen(self):
        return "Audífonos: Emitiendo bip de confirmación en el oído. Volumen +1"

def presionar_subir_volumen(aparato):
    print(aparato.subir_volumen())

mis_aparatos = [MiSmartTV(), MiEquipoAudio(), MisAudifonos()]

print("Probando los controles de mi casa ")
for item in mis_aparatos:
    presionar_subir_volumen(item)