
# Design a class Vehicle that:
# Keeps a record of service charge rate common to all vehicles.
# Each vehicle has a model, kilometers_run, and service history.
# Has a function to calculate service charge based on km and rate.
# Provides a method to update the service rate for all vehicles.
# Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# 1.Creating vehicles with different km and models.
# 2.Updating the service rate.
# 3.Showing charges and eligibility checks.

class Vehicle:
    service_charge_rate=100
    def __init__(self,model, kilometers_run,service_history):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=service_history

    def service_charge(self):
        return self.kilometers_run * Vehicle.service_charge_rate
    @classmethod
    def update_rate(cls, new_rate):
        cls.service_charge_rate = new_rate
        (print("Service charge rate updated to:", cls.service_charge_rate))
    @staticmethod
    def eligible(years_old):
        return years_old <= 15
v1 = Vehicle("Honda City", 10, 2)
v2 = Vehicle("Swift", 20, 5)

vehicles = [v1, v2]

print("Before updating rate:")
for v in vehicles:
    print(v.model,
          "| Charge:", v.service_charge(),
          "| Eligible:", Vehicle.eligible(v.service_history))

# update rate
Vehicle.update_rate(150)

print("\nAfter updating rate:")
for v in vehicles:
    print(v.model,
          "| Charge:", v.service_charge(),
          "| Eligible:", Vehicle.eligible(v.service_history))