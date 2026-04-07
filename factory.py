class Planta:
    def descripcion(self):
        return "Planta"

class Maceta:
    def descripcion(self):
        return "Maceta"

def crear_producto(tipo):
    if tipo == "planta":
        return Planta()
    elif tipo == "maceta":
        return Maceta()