import doctest

class Car:
    def __init__(self, brand: str, max_speed: int):
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Марка автомобиля должна быть непустой строкой.")
        if not (isinstance(max_speed, int) and max_speed > 0):
            raise ValueError("Максимальная скорость должна быть положительным числом.")
        self.brand = brand
        self.max_speed = max_speed

    def drive(self, distance: float) -> None:

    def refuel(self, fuel_amount: float) -> None:


class Animal:
    def __init__(self, species: str, age: int):
        if not isinstance(species, str) or not species.strip():
            raise ValueError("Вид должен быть непустой строкой.")
        if not (isinstance(age, int) and age >= 0):
            raise ValueError("Возраст должен быть неотрицательным числом.")
        self.species = species
        self.age = age

    def eat(self, food: str) -> None:

    def make_sound(self) -> None:


class Book:

    def __init__(self, title: str, author: str):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название книги должно быть непустой строкой.")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Автор книги должен быть непустой строкой.")
        self.title = title
        self.author = author


    def read(self, page: int) -> None:

    def get_summary(self) -> str:

 if __name__ == "__main__":
    doctest.testmod()