'''
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
'''
time_in_seconds = int(input('Введите время в секундах: '))
time_in_minutes = round(float(time_in_seconds/60), 1)
time_in_horse = round(float(time_in_minutes/60), 1)
print(f'Время в формате ч:м:с - {time_in_horse} : {time_in_minutes} : {time_in_seconds}')