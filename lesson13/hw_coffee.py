class Furgon:
    def __init__(self):
        self.cuzov = []

    def add_coffeeBox(self, coffeeBox):
        self.cuzov.append(coffeeBox)

    def profit(self):
        total_profit = 0
        for coffeeBox in self.cuzov:
            total_profit += coffeeBox.profit()
        return total_profit

class CoffeeBox:
    def __init__(self,weight,coffee):
        self.coffeeList = []
        self.weight = weight
        self.coffee = coffee

# calculate coffee*weight

    def get_weight(self):
        return self.weight

    def add_coffee(self, coffee):
        self.coffeeList.append(coffee)

class Coffee:
    def __init__(self,sort, price):
        self.sort = sort
        self.price = price

    def get_price(self):
        return self.price

def main():
    furgon = Furgon()
    coffee1 = Coffee("Arabica",120)
    coffee2 = Coffee("Rabusta",100)

    coffeeBox1 = CoffeeBox()
    coffeeBox1.get_weight(10)
    coffeeBox2 = CoffeeBox()
    coffeeBox2.get_weight(20)
    coffeeBox1.add_coffee

    furgon.add_coffeeBox()
    print(furgon.profit())

main()