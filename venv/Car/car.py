#!/usr/bin/python
# -*- coding: utf-8 -*-

'''一个可用于表示汽车的类'''
class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        lone_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return lone_name

    def read_odometer(self):
        print 'This ca has ' + str(self.odometer_reading) + ' miles on it.'

    def updata_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print "You can't roll back an odometer!"

    def increment_odometer(self, miles):
        self.odometer_reading += miles


'''组用于表示燃油汽车和电动汽车的类'''
class Battery(object):
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print "This car has a " + str(self.battery_size) + '-kWh battery.'

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += ' miles on a full charge.'
        print message



class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()
