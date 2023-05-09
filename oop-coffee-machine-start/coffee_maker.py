class CoffeeMaker:
    """Modela a máquina que faz o café"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Imprime um relatório de todos os recursos."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Retorna True quando o pedido pode ser feito, False se os ingredientes são insuficientes."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f" Desculpe, ingredientes insuficiente{item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deduz os ingredientes necessários dos recursos."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Aqui está o seu {order.name} ☕️. ")
