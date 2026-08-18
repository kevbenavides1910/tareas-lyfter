class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has boarded the bus.")
        else:
            print("The bus is full. Cannot add more passengers.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} has left the bus.")
        else:
            print(f"{person.name} is not on the bus.")


def find_passenger(passengers, name):
    return next((p for p in passengers if p.name.lower() == name.lower()), None)


max_passengers = int(input("Enter the bus capacity: "))
bus = Bus(max_passengers)

while True:
    print(f"\nPassengers on bus: {len(bus.passengers)}/{bus.max_passengers}")
    print("1. Add passenger")
    print("2. Remove passenger")
    print("3. Exit")
    option = input("Select an option: ").strip()

    if option == "1":
        name = input("Passenger name: ").strip()
        age = int(input("Passenger age: "))
        bus.add_passenger(Person(name, age))

    elif option == "2":
        name = input("Passenger name to remove: ").strip()
        person = find_passenger(bus.passengers, name)
        if person:
            bus.remove_passenger(person)
        else:
            print(f"{name} is not on the bus.")

    elif option == "3":
        break
