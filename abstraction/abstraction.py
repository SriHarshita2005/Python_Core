#11. Using abc module:
# • Create an abstract class Shape with area(), perimeter()
# • Implement Circle, Rectangle, Triangle
# Demonstrate: • why base class should NOT contain calculation logic
# • what happens if a subclass fails to implement one of the methods

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def area(self,r):
        return 3.14*r*r
    def perimeter(self,r):
        return 2*3.14*r
class Rectangle(Shape):
    def area(self,a,b):
        return a*b
    def perimeter(self,a,b):
        return 2*(a+b)
class Triangle(Shape):
    def area(self,b,h):
        return 0.5*b*h
    def perimeter(self,a,b,c):
        return a+b+c
# c = Circle()
# print("Circle Area =", c.area(5))
# print("Circle Perimeter =", c.perimeter(5))
# r = Rectangle()
# print("Rectangle Area =", r.area(4, 6))
# print("Rectangle Perimeter =", r.perimeter(4, 6))
# t = Triangle()
# print("Triangle Area =", t.area(10, 5))
# print("Triangle Perimeter =", t.perimeter(3, 4, 5))

#12. Design an abstract class PaymentGateway with:
# • authenticate() • pay(amount) • refund(amount)
# Implement subclasses: • UPIPayment • CardPayment • NetBankingPayment
# Show how abstraction helps your main program call payment methods without caring about the payment type.

from abc import ABC,abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
class UPIPayment(PaymentGateway):
    def authenticate(self):
        pin=int(input("Enter pin"))
        if pin==1234:
            print("Authentication is successful")
        else:
            print("Invalid Pin")
    def pay(self,amount):
        return f"Paid {amount} using UPI"
    def refund(self,amount):
        return f"Refunded {amount} using UPI"
class CardPayment(PaymentGateway):
    def authenticate(self):
        pin=int(input("Enter pin"))
        if pin=="1234":
            print("Authentication is successful")
        else:
            print("Invalid Pin")
    def pay(self,amount):
        return f"Paid {amount} using card"
    def refund(self,amount):
        return f"Refunded {amount} using card"
class NetBankingPayment(PaymentGateway):
    def authenticate(self):
        pin=int(input("Enter pin"))
        if pin=="1234":
            print("Authentication is successful")
        else:
            print("Invalid Pin")
    def pay(self,amount):
        return f"Paid {amount} using net banking"
    def refund(self,amount):
        return f"Refunded {amount} using net banking"
# u=UPIPayment()
# c=CardPayment()
# n=NetBankingPayment()
# u.authenticate()
# print(u.pay(100))
# print(u.refund(500))
# print(c.authenticate())
# print(c.pay(200))
# print(c.refund(500))
# print(n.authenticate())
# print(n.pay(200))
# print(n.refund(500))

#13. Create: • Abstract class VehicleControl with methods accelerate(), brake(), steer()
# • Implement CarControl, BikeControl, TruckControl Demonstrate calling each through a single interface.

from abc import ABC , abstractmethod
class VehicleControl(ABC):
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def steer(self):
        pass
class CarControl(VehicleControl):
    def accelerate(self):
        print("Car is accelerating")
    def brake(self):
        print("Car is brakeing")
    def steer(self):
        print("Car is steering")
class BikeControl(VehicleControl):
    def accelerate(self):
        print("Bike is accelerating")
    def brake(self):
        print("Bike is brakeing")
    def steer(self):
        print("Bike is steering")
class TruckControl(VehicleControl):
    def accelerate(self):
        print("Truck is accelerating")
    def brake(self):
        print("Truck is brakeing")
    def steer(self):
        print("Truck is steering")
def operate_vehicle(vehicle):
    vehicle.accelerate()
    vehicle.brake()
    vehicle.steer()
    print()
# car = CarControl()
# bike = BikeControl()
# truck = TruckControl()
# operate_vehicle(car)
# operate_vehicle(bike)
# operate_vehicle(truck)

 #Create an abstract class DatabaseDriver with: • connect() • execute(query) • close()
# Implement concrete drivers: • MySQLDriver • PostgresDriver • SQLiteDriver
# Show how abstraction helps switch databases without rewriting main code.

from abc import ABC, abstractmethod
class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def execute(self, query):
        pass
    @abstractmethod
    def close(self):
        pass
class MySQLDriver(DatabaseDriver):
    def connect(self):
        print("Connected to MySQL Database")
    def execute(self, query):
        print("MySQL Executing:", query)
    def close(self):
        print("MySQL Connection Closed")
class PostgresDriver(DatabaseDriver):
    def connect(self):
        print("Connected to PostgreSQL Database")
    def execute(self, query):
        print("PostgreSQL Executing:", query)
    def close(self):
        print("PostgreSQL Connection Closed")
class SQLiteDriver(DatabaseDriver):
    def connect(self):
        print("Connected to SQLite Database")
    def execute(self, query):
        print("SQLite Executing:", query)
    def close(self):
        print("SQLite Connection Closed")
def run_database(driver):
    driver.connect()
    driver.execute("SELECT * FROM STUDENTS")
    driver.close()
    print()
# mysql = MySQLDriver()
# postgres = PostgresDriver()
# sqlite = SQLiteDriver()
# run_database(mysql)
# run_database(postgres)
# run_database(sqlite)

#15. Design a class ReportGenerator (abstract) with: • load_data() • process() • export() Implement: • PDFReport • ExcelReport
from abc import ABC , abstractmethod
class ReportGenerator(ABC):
    def load_data(self):
        pass
    def process(self):
        pass
    def export(self):
        pass
class PDFReport(ReportGenerator):
    def load_data(self):
        print("Loading data for Pdf")
    def process(self):
        print("Processing data for pdf")
    def export(self):
        print("Exporting data for pfd")
class ExcelReport(ReportGenerator):
    def load_data(self):
        print("Loading data for excel")
    def process(self):
        print("Processing data for excel")
    def export(self):
        print("Exporting data for excel")
# pdf = PDFReport()
# pdf.load_data()
# pdf.process()
# pdf.export()
# print()
# excel = ExcelReport()
# excel.load_data()
# excel.process()
# excel.export()

#16. Create an abstract class RobotCommand with: • execute() • undo()
# Implement: • PickCommand • PlaceCommand • MoveCommand
# Demonstrate how abstraction cleanly represents commands without revealing details.

from abc import ABC , abstractmethod
class RobotCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass
class PickCommand(RobotCommand):
    def execute(self):
        print("Robot picked obj")
    def undo(self):
        print("Robot placed the obj")
class PlacedCommand(RobotCommand):
    def execute(self):
        print("Robot placed the object")
    def undo(self):
        print("Robot picked up the object again")
class MovedCommand(RobotCommand):
    def execute(self):
        print("Robot moved forward")
    def undo(self):
        print("Robot moved backward")
def run_command(command):
    command.execute()
    command.undo()
# run_command(PickCommand())
# run_command(PlacedCommand())
# run_command((MovedCommand()))

#17. Create an abstract class MLModel with: • train(data) • predict(x) • evaluate(test_set)
# Implement models: • LinearRegressionModel- some different logic • DecisionTreeModel – some logic
# Show how a generic training loop works for any model without caring about details.

from abc import ABC , abstractmethod
class MLModel(ABC):
    @abstractmethod
    def train(self,data):
        pass
    @abstractmethod
    def predict(self,x):
        pass
    @abstractmethod
    def evaluate(self,test_set):
        pass
class LinearRegressionModel(MLModel):
    def train(self, data):
        print("Training Linear Regression using gradient descent")
    def predict(self, x):
        print("Predicting using equation y = mx + c")
    def evaluate(self, test_set):
        print("Evaluating Linear Regression using MSE")
class DecisionTreeModel(MLModel):
    def train(self, data):
        print("Training Decision Tree by splitting nodes")
    def predict(self, x):
        print("Predicting using tree traversal")
    def evaluate(self, test_set):
        print("Evaluating Decision Tree using accuracy")
def train_model(model):
    model.train("Training data")
    model.predict(10)
    model.evaluate("Test data")
    print()
# l=LinearRegressionModel()
# d=DecisionTreeModel()
# train_model(l)
# train_model(d)

#18. Design a system without abstraction first: • Write separate functions for EmailSender, SMSSender, PushSender
# Show how the main program becomes a mess with constant if/else. Then: • Redesign using an abstract base class Notifier.
# def EmailSender(message):
#     print("Sending Email:",message)
# def SMSSender(message):
#     print("Senfing SMS:",message)
# def PushSender(message):
#     print("Sending Push notification:",message)
# choice=input("Enter your choice")
# if choice == "email":
#     EmailSender("Hello")
# elif choice == "sms":
#     SMSSender("HI")
# elif choice == "push":
#     PushSender("How are you")

from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailSender(Notifier):
    def send(self, message):
        print("Sending Email:", message)
class SMSSender(Notifier):
    def send(self, message):
        print("Sending SMS:", message)
class PushSender(Notifier):
    def send(self, message):
        print("Sending Push Notification:", message)
def notify_user(notifier, message):
    notifier.send(message)
# notify_user(EmailSender(), "Hello User")
# notify_user(SMSSender(), "Hello User")
# notify_user(PushSender(), "Hello User")

#19. Create an abstract MediaPlayer with: • load() • play() • stop()
# Implement: • MP3Player • WAVPlayer • AACPlayer
# Demonstrate calling each via a unified interface.

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MP3Player(MediaPlayer):
    def load(self):
        print("Loading MP3 file")

    def play(self):
        print("Playing MP3 file")

    def stop(self):
        print("Stopping MP3 file")

class WAVPlayer(MediaPlayer):
    def load(self):
        print("Loading WAV file")

    def play(self):
        print("Playing WAV file")

    def stop(self):
        print("Stopping WAV file")

class AACPlayer(MediaPlayer):
    def load(self):
        print("Loading AAC file")

    def play(self):
        print("Playing AAC file")

    def stop(self):
        print("Stopping AAC file")

def play_media(player):
    player.load()
    player.play()
    player.stop()

# play_media(MP3Player())
# play_media(WAVPlayer())
# play_media(AACPlayer())

#20. Design: • Abstract base class Sensor with functions read_value() and calibrate() •
# Subclasses: TemperatureSensor, PressureSensor, HumiditySensor
# Encapsulate: • internal raw sensor readings • calibration factor H
# ide all raw operations and allow only a public, clean get_reading() method.

from abc import ABC , abstractmethod
class Sensor(ABC):
    def __init__(self):
        self.__raw_readings = 100
        self.__calibration_factor = 1.0
    @abstractmethod
    def read_value(self):
        pass
    @abstractmethod
    def calibrate(self):
        pass
    def get_reading(self):
        return self.read_value()
class TemperatureSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.__raw_reading = 30
        self.__calibration_factor = 1.05
    def read_value(self):
        return self.__raw_reading*self.__calibration_factor
    def calibrate(self):
        self.__calibration_factor = 1.1
class PressureSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.__raw_reading = 1000
        self.__calibration_factor = 0.98
    def read_value(self):
        return self.__raw_reading * self.__calibration_factor
    def calibrate(self):
        self.__calibration_factor = 1.0
class HumiditySensor(Sensor):
    def __init__(self):
        super().__init__()
        self.__raw_reading = 60
        self.__calibration_factor = 1.02
    def read_value(self):
        return self.__raw_reading * self.__calibration_factor
    def calibrate(self):
        self.__calibration_factor = 1.05
# t = TemperatureSensor()
# p = PressureSensor()
# h = HumiditySensor()
#
# print("Temperature:", t.get_reading())
# print("Pressure:", p.get_reading())
# print("Humidity:", h.get_reading())

