"""
Задача №1.
Тетяна кожен день лягає спати рівно опівночі і нещодавно дізналась, що оптимальний час для її сну становить t хвилин. Тетяна хоче поставити собі будильник так, щоб він продзвенів рівно через t хвилин після півночі, однак для цього необхідно вказати час сигналу у форматі години і хвилини. Допоможіть Тані визначити, на який час завести будильник. Години і хвилини у виведенні програми повинні розташовуватися на різних рядках.
Автор: Волочнюк Поліна іванівна
"""

t = int(input("Введіть оптимальний час для сну: "))  # Ввід оптимального часу для сну у хвилинах
hours = t // 60  # Отримання годин
minutes = t % 60  # Отримання хвилин

print(hours)  # Вивід годин
print(minutes)  # Вивід хвилин
