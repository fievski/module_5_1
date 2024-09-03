class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)



h1 = House('ЖК Пристройский', 18)
h2 = House('Сарай на даче', 2)
h1.go_to(5)
h2.go_to(10)


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#
#     def say_info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age}')
#
#     def birthday(self):
#         self.age += 1
#         print(f'У меня день рождения, мне теперь {self.age} ')
#
#
# sam = Human('Сёма', 25)
# ben = Human('Ваня', 20)
#
# sam.birthday()
#
# # print(sam.name, sam.age)
# # print(ben.name, ben.age)