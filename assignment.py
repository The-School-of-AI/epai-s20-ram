from datetime import datetime
import math


class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.birth_year = birth_year
        self.first_name = first_name
        self.last_name = last_name
        self.bonus = 0.1
        self.base_salary = 50000

    def __str__(self):
        return f"Person(age={self.age}, first_name={self.first_name}, last_name={self.last_name})"

    @property
    def age(self):
        return datetime.now().year - self.birth_year

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        if isinstance(value, int):
            self._birth_year = value
        else:
            raise ValueError("Birth year must be an integer")

    def set_birth_year(self, value):
        self.birth_year = value

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        self.first_name, self.last_name = value.split()

    @property
    def salary(self):
        return self.bonus * self.base_salary + self.base_salary

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if isinstance(value, (int, float)):
            self._bonus = value
        else:
            raise ValueError("Bonus must be a real number")

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value):
        if isinstance(value, (int, float)):
            self._base_salary = value
        else:
            raise ValueError("Base salary must be a real number")

    @property
    def current_year(self):
        return datetime.now().year


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._radius = value
            self._area = math.pi * self.radius**2
            self._diameter = 2 * self.radius
        else:
            raise ValueError("Radius must be a positive real number")

    def set_radius(self, value):
        self.radius = value

    @property
    def area(self):
        return self._area

    @property
    def diameter(self):
        return self._diameter


class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count

    @staticmethod
    def classify_vehicle(vehicle_type):
        return f"This is a {vehicle_type}"


class ElectricVehicle(Vehicle):
    @staticmethod
    def classify_vehicle(vehicle_type):
        return f"This is an electric {vehicle_type}"


class DynamicClass:
    static_value = 0

    def __init__(self):
        self._dynamic_attr = {}

    def dynamic_attr(self, name, value):
        self._dynamic_attr[name] = value

    def __getattr__(self, name):
        if name in self._dynamic_attr:
            return self._dynamic_attr[name]
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )


class ValidatedAttribute:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int) or not value > 0:
            raise ValueError(f"{value} must be a positive integer")
        self._value = value
