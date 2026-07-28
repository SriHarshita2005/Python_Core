#7. Create: • An Engine class with private state like temperature • A Car class that uses an Engine but should:
# o Not allow users to manipulate engine temperature
# o Only expose methods like start_car() or cool_engine()
# Demonstrate why giving direct engine access is dangerous.

class Engine:
    def __init__(self,temperature):
        self.__temperature=temperature

class Car(Engine):
