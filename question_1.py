class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

vehicle1 = Vehicle(55, "Nissan", "Jeffrey")
vehicle2 = Vehicle(24, "Toyota", "Jim")

print(vehicle1.owner)
print(vehicle2.owner)

vehicle1.update_owner(new_owner="Joe")
vehicle2.update_owner(new_owner="Timothy")

print(vehicle1.owner)
print(vehicle2.owner)

