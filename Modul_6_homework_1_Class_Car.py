class Car:
    price = 1000000

    def horse_powers(self, horse_power):
        self.horse_power = horse_power
        return horse_power

class Nissan(Car):
    price = 20000

n = Nissan()
print('The price of my Nissan = ',n.price, ' dollars')
print('Engine power of my Nissan = ', n.horse_powers(80), ' horses')

class Kia(Car):
    price = 15000

d = Kia()
print('The price of my Kia = ',d.price, ' dollars')
print('Engine power of my Kia = ', d.horse_powers(90), ' horses')