class Car():
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
    self.fuel = 0

  def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.model + ' ' + self.make
    return long_name.title()

  def read_odometer(self):
    print("This car has " + str(self.odometer_reading))

  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage

    else:
      print("You can't roll back an odometer")
      
  def increament_odometer(self, miles):
    self.odometer_reading += miles

  def fill_gas_tank(self, liter):
    self.fuel += liter

class Battery():
  def __init__(self, battery_size = 70):
    self.battery_size = battery_size

  def describe_battery(self):
    print('this car has a' + str(self.battery_size) + ' kWh battery')
    
  def upgrade_battery(self):
    if self.battery_size != 85:
      self.battery_size = 85
      
  def get_range(self):
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270

    message = "This car can go approximately " + str(range) + " miles on a full charge."
    print(message)

class ElectricCar(Car):  #Inheritance ElectricCar is the child/base class of Car the parent/super class
  def __init__(self, make, model, year):
    super().__init__(make, model, year)  #super():make connections between the parent and child class
    self.color = 'Red'
    self.battery = Battery() #attribute of ElectricCar is the instance of Battery class
    
  def describe_color(self):
    print(f"The model {self.model} is of {self.color}")

  def fill_gas_tank(self):  #Overriding the fill_gas_tank method in Car(parent class)
    print('This car doesnt need a gas tank!')

my_car = ElectricCar('Ford','model', 2000)
print(my_car.get_descriptive_name())  #function of parent class called through the instance of child class
my_car.battery.describe_battery()  #function of another class used by current class's instance due to instance is an attribute of current class
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()
