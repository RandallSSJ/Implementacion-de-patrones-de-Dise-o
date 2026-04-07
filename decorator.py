class Producto:
    def descripcion(self):
        return "Producto básico"

class Decorador:
    def _init_(self, producto):
        self.producto = producto

class Fertilizante(Decorador):
    def descripcion(self):
        return self.producto.descripcion() + " + fertilizante"