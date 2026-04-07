class Cliente:
    def actualizar(self, mensaje):
        print("Cliente:", mensaje)

class Venta:
    def _init_(self):
        self.observadores = []

    def agregar(self, obs):
        self.observadores.append(obs)

    def notificar(self, mensaje):
        for o in self.observadores:
            o.actualizar(mensaje)