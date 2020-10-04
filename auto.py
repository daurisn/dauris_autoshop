# dictionary with services available and their cost
services = {"Oil Change": 35, "Headlight Repair": 100, "Brake Repair": 300, "Wheel Alignment": 50, "Tire Rotation": 50,
            "Car Wash": 15, "Car Wax": 40}

# set variable for total cost of services to be used later in the program
total_cost = 0

# displays the services available to the customer
print("""Davy's Auto Shop Services:
Oil change -- $35
Tire rotation -- $50
Headlight Repair -- $100
Brake Repair -- $300
Wheel Alignment -- $50
Car Wash -- $15
Car Wax -- $40
""")

# asks the customer which two services they need done
first = (input("What is the first service your car needs? :"))
second = (input("What is the second service your car needs? :"))

# finds if the chose a service and what service the customer chose
if first in services:
    print(first, "is $%s" % services[first])
    total_cost = services[first]
elif first == "None":
    print("No service selected.")
elif first not in services:  # in case customer inputs characters that don't match services available
    print("We do not offer that service.")

# finds if customer chose a second service and if so which one
if second in services and first in services:
    total_cost = services[first] + services[second]  # adds cost of services selected and assigns them to total_cost
    print(second, "is $%s" % services[second])
elif second in services and first not in services:
    print(second, "is $%s" % services[second])
    total_cost = services[second]
elif second == "None":
    print("No service selected.")
else:
    print("We do not offer that service.")

print("The total price is: $%s" % total_cost)