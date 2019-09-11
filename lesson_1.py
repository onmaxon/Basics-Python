# coding: utf-8

print("\nУровень: easy")

print("\nЗадача 1")
name = input("Представьтесь пожалуйста: ")
print("Привет! ", name)

print("\nЗадача 2")
userInt = int(input("Введите число: "))
mySum = userInt + 2
print(name, "Я прибавил к твоему числу 2, вот что получилось: ", mySum)

print("\nЗадача 3")
userAge = int(input("Сколько вам лет?: "))
if userAge >= 18:
    print(name, "Доступ разрешен!")
else:
    print(name, "Извините, пользование данным ресурсом только с 18 лет")

print("\nУровень: normal")

print("\nЗадача 1")
while True:
    userInt = int(input("Введите число: "))
    if 0 < userInt < 10:
        exponent = userInt ** 2
        print("Я возвел ваше число в степень 2:", exponent)
        break
    if userInt <= 0:
        print("Введите число больше 0 но меньше 10")
    if userInt > 10:
        print("Введите число больше 0 но меньше 10")

print("\nЗадача 2")

firstInt = int(input("Введите 1-ое число: "))
secondInt = int(input("Введите 2-ое число: "))
#Можно сделать так.
# firstInt = firstInt + secondInt
# secondInt = firstInt - secondInt
# firstInt = firstInt - secondInt

#Но так проще
firstInt, secondInt = secondInt, firstInt
print("Первое число = ", firstInt)
print("Второе число = ", secondInt)

print("\nУровень: hard")
print("Медицинская анкета")
name = input("Ваше имя: ")
surname = input("Ваше фамилия: ")
age = int(input("Ваш возвраст: "))
weight = int(input("Ваш вес: "))
if age <= 30 and 50 <= weight <= 120:
    print('{0} {1}, {2} год, {3} кг - хорошее состояние!'.format(name, surname, age, weight))
if (age <= 40 and age >= 30) and (weight < 50 or weight > 120):
    print('{0} {1}, {2} год, {3} кг - пора начать правильный образ жизни!'.format(name, surname, age, weight))
if age > 40 and (weight < 50 or weight > 120):
    print('{0} {1}, {2} год, {3} кг - следует обратиться к врачу!'.format(name, surname, age, weight))
