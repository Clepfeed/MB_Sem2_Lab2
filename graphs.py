import matplotlib.pyplot as plt
import os
import numpy as np

# Функция, с которой мы будем сравнивать точки
def reference_function(x):
    return np.sin(np.abs(x)) + 1  # Пример функции f(x) = x^2

# Получаем список всех txt файлов в текущей директории
files = [f for f in os.listdir('.') if f.endswith('.txt')]

# Для каждого файла создаем отдельный график
for file_name in files:
    # Чтение данных из файла
    x_points = []
    y_points = []
    
    with open(file_name, 'r') as file:
        for line in file:
            # Разбиваем строку на два числа
            values = line.strip().split()
            if len(values) == 2:
                try:
                    x = float(values[0])
                    y = float(values[1])
                    x_points.append(x)
                    y_points.append(y)
                except ValueError:
                    print(f"Пропущена строка в файле {file_name}: {line}")
    
    # Создаем новый график
    plt.figure(figsize=(10, 6))
    
    # Построение точек из файла
    plt.scatter(x_points, y_points, color='red', label='Точки из файла')
    
    # Построение графика функции
    # Создаем массив x-значений для плавного графика
    x = np.linspace(min(x_points), max(x_points), 100)
    y = reference_function(x)
    plt.plot(x, y, color='blue', label='Заданная функция')
    
    # Настройка графика
    plt.title(f'График для файла {file_name}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()

# Показываем все графики
plt.show()


# Можешь пожалуйста добавить чтобы программа проверяла названия файлов и, если название оканчивается на 1, график по данным из файла рисовался поверх графика функции 1 (указанной внутри программы), а если название оканчивалось на 2, график по данным из файла рисовался поверх графика функции 2 (указанной внутри программы)