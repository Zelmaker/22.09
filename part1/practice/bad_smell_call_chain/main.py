# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, rum_num, city_popylation):
        self.run_num = rum_num
        self.city_population = city_popylation

    def get_person_room(self):
        return self.run_num

    def get_city_population(self):
        return self.city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person(42, 100500)
print(person.get_person_room())
print(person.get_city_population())

# ИЛИ
room = Room()
city = City()

person = Person(room.get_name(), city.population())
print(person.get_person_room())
print(person.get_city_population())
