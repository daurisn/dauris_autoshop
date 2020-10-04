services = {"Oil Change": 35, "Headlight Repair": 100, "Brake Repair": 300, "Wheel Alignment": 50, "Tire Rotation": 50,
            "Car Wash": 15, "Car Wax": 40}
total_cost = 0

print("""Dauris's Auto Shop Services:
Oil change -- $35
Tire rotation -- $50
Headlight Repair -- $100
Brake Repair -- $300
Wheel Alignment -- $50
Car Wash -- $15
Car Wax -- $40
""")

first = (input("What is the first service your car needs? :"))
second = (input("What is the second service your car needs? :"))

if first in services:
    print(first, "is $%s" % services[first])
    total_cost = services[first]
elif first == "None":
    print("No service selected.")
elif first not in services:
    print("We do not offer that service.")


if second in services and first in services:
    total_cost = services[first] + services[second]
    print(second, "is $%s" % services[second])
elif second in services and first not in services:
    print(second, "is $%s" % services[second])
    total_cost = services[second]
elif second == "None":
    print("No service selected.")
else:
    print("We do not offer that service.")

print("The total price is: $%s" % total_cost)
