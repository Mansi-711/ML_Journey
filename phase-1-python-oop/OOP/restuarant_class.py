class Restaurant():
    def __init__(self,name,cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    def describe_restuarant(self):
        print(f'The name of the restaurant is {self.name} and it has {self.cuisine} cuisine.')

    def open_restaurant(self):
        print(f'{self.name} is now open')

    def set_customer_served(self,num):
        self.number_served = num
        print(f'{self.name} has served {self.number_served} customers')
        
    def increment_customer_served(self,increment):
        self.number_served += increment
        print(f'{self.name} has served {self.number_served} customers')

r1 = Restaurant('Taj Mahal', 'Indian')
r1.describe_restuarant()
r1.open_restaurant()
r1.set_customer_served(300)
r1.increment_customer_served(400)

r2 = Restaurant('Osteria','Italian')
r2.describe_restuarant()
r2.open_restaurant()
r2.set_customer_served(400)
r2.increment_customer_served(500)

