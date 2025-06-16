# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de una cafetera eléctrica

class CoffeeMachine:
    def __init__(self, capacity=1000):
        """
        Constructor de la cafetera.
        :param capacity: Capacidad máxima del tanque de agua en mililitros (ml)
        """
        self.water_level = 0  # Nivel actual de agua (ml)
        self.capacity = capacity  # Capacidad total del tanque (ml)
        self.cups_served = 0  # Contador de tazas servidas

    def fill_water(self, amount):
        """
        Añade agua al tanque de la cafetera.
        :param amount: Cantidad de agua en ml.
        """
        if self.water_level + amount <= self.capacity:
            self.water_level += amount
            print(f"Se añadieron {amount} ml de agua.")
        else:
            self.water_level = self.capacity
            print("Tanque lleno. Se ha agregado hasta el límite máximo.")

    def serve_coffee(self, cup_size=200):
        """
        Sirve una taza de café si hay suficiente agua.
        :param cup_size: Tamaño de la taza en ml (por defecto 200 ml).
        """
        if self.water_level >= cup_size:
            self.water_level -= cup_size
            self.cups_served += 1
            print(f"Taza de {cup_size} ml servida.")
        else:
            print("No hay suficiente agua para servir una taza.")

    def status(self):
        """
        Muestra el estado actual de la cafetera.
        """
        print(f"Agua restante: {self.water_level} ml")
        print(f"Tazas servidas: {self.cups_served}")