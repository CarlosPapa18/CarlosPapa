class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            print(f"{self.nombre} ha muerto.")
        else:
            print(f"{self.nombre} tiene {self.vida} de vida.")

    def atacar(self, enemigo):
        pass  # Método que será redefinido por cada subclase


class Guerrero(Personaje):
    def atacar(self, enemigo):
        daño = 10
        print(f"{self.nombre} ataca con espada causando {daño} de daño.")
        enemigo.recibir_daño(daño)


class Mago(Personaje):
    def atacar(self, enemigo):
        daño = 12
        print(f"{self.nombre} lanza un hechizo causando {daño} de daño.")
        enemigo.recibir_daño(daño)


# Simulación de combate simple
g = Guerrero("Arthas", 30)
m = Mago("Merlín", 25)

g.atacar(m)
m.atacar(g)
