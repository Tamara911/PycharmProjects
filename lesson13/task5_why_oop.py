# oop reduces time of creation code
# object oriented modelling

class Aircompany:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def profit(self):
        total_profit = 0
        for flight in self.flights:
            total_profit += flight.profit()
        return total_profit

class Flight:
    def __init__(self,airplane, direction):
        self.tickets = []
        self.employees = []
        self.airplane = airplane
        self.direction = direction

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def add_employee(self,employee):
        self.employees.append(employee)

    def profit(self):
        total_profit = 0
        for ticket in self.tickets:
            total_profit += ticket.get_price()
        for employee in self.employees:
            total_profit -= employee.get_salary()
        total_profit -= self.airplane.get_gas_usege()*self.direction.get_lenght()*30 # 30 per one litr
        return total_profit

class Ticket:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

class Employee:
    def __init__(self, employee_type, salary):
        self.employee_type = employee_type
        self.salary = salary

    def get_salary(self):
        return self.salary

class Airplane:
    def __init__(self, airplane_type, gas_usege):
        self.airplane_type = airplane_type
        self.gas_usege = gas_usege

    def get_gas_usege(self):
        return self.gas_usege

class Diraction:
    def __init__(self, from_city, to_city, lenght):
        self.from_city = from_city
        self.to_city = to_city
        self.lenght = lenght

    def get_lenght(self):
        return self.lenght

def main():
    aircompany = Aircompany()
    airplane = Airplane('A320', 50)
    direction = Diraction("Kyiv", "Paris", 600)
    flight = Flight(airplane, direction)
    pilot1 = Employee("pilot", 200)
    pilot2 = Employee("pilot", 300)
    stuard1 = Employee("stuard", 100)
    stuard2 = Employee("stuard", 150)
    flight.add_employee(pilot1)
    flight.add_employee(pilot2)
    flight.add_employee(stuard1)
    flight.add_employee(stuard2)
    ticket1 = Ticket(50)
    ticket2 = Ticket(150)
    flight.add_ticket(ticket1)
    flight.add_ticket(ticket2)
    aircompany.add_flight(flight)

    print(aircompany.profit())

main()




