import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib.widgets import Button
import math
import re
from collections import defaultdict

# Две функции для сравнения
def reference_function1(x):
    return np.cos(2 * x)

def reference_function2(x):
    return np.sin(np.abs(x)) + 1

# Глобальные переменные для хранения данных графиков
graphs_data = defaultdict(lambda: defaultdict(list))  # {номер: {буква: данные}}
current_page = 1   # Текущая страница
unique_numbers = [] # Уникальные номера для страниц

# Функция для переключения страниц
def switch_page(event):
    global current_page
    current_page = (current_page % len(unique_numbers)) + 1
    plot_graphs(current_page)

# Функция для отрисовки графиков
def plot_graphs(page_number):
    plt.clf()  # Очищаем текущий график

    # Получаем уникальный номер для текущей страницы
    current_number = unique_numbers[page_number - 1]
    
    # Сбираем данные для текущего номера
    current_data = {k: v for k, v in graphs_data[current_number].items() if v}

    if not current_data:
        plt.text(0.5, 0.5, f'Нет данных для номера {current_number}', 
                 horizontalalignment='center', verticalalignment='center')
    else:
        # Определяем количество столбцов и строк
        columns = len(current_data)  # Количество уникальных первых букв
        rows = max(len(v) for v in current_data.values())  # Максимальное количество файлов в группе

        # Создаем подграфики
        for col_idx, (first_letter, data_list) in enumerate(current_data.items()):
            for row_idx, data in enumerate(data_list):
                ax = plt.subplot(rows, columns, row_idx * columns + col_idx + 1)  # Один столбец на каждую букву
                
                # Отрисовка точек
                ax.scatter(data['x_points'], data['y_points'], label='Точки из файла')
                
                # Отрисовка функции
                x = np.linspace(min(data['x_points']), max(data['x_points']), 100)
                function = reference_function1 if current_number.endswith('1') else reference_function2
                y = function(x)
                ax.plot(x, y, 
                        color='blue' if current_number.endswith('1') else 'green', 
                        label=f'Функция {current_number}')
                
                ax.set_title(f'График {data["name"]}')
                ax.grid(True)
                ax.legend()

    plt.suptitle(f'Графики для номера {current_number}', fontsize=16)
    
    # Добавляем кнопку переключения
    if hasattr(plot_graphs, 'btn'):
        plot_graphs.btn.ax.set_visible(False)  # Скрываем старую кнопку
    btn_ax = plt.axes([0.4, 0.02, 0.2, 0.04])
    plot_graphs.btn = Button(btn_ax, 'Переключить страницу')
    plot_graphs.btn.on_clicked(switch_page)
    
    # Корректируем layout
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.1)
    
    plt.draw()

# Путь к директории с файлами
directory = "MB_Sem2_Lab2"
dir_path = os.path.join(os.getcwd(), directory)
files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]

# Читаем данные из всех файлов
for file_name in files:
    x_points = []
    y_points = []
    
    with open(os.path.join(dir_path, file_name), 'r') as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 2:
                try:
                    x = float(values[0])
                    y = float(values[1])
                    x_points.append(x)
                    y_points.append(y)
                except ValueError:
                    print(f"Пропущена строка в файле {file_name}: {line}")
    
    # Извлекаем номер и первую букву
    match = re.search(r'_(\d+)', file_name)
    if match:
        number = match.group(1)
        first_letter = file_name[0]
        
        # Сохраняем данные в соответствующий словарь
        data = {
            'name': file_name,
            'x_points': x_points,
            'y_points': y_points
        }
        
        graphs_data[number][first_letter].append(data)
        
        # Добавляем номер в уникальные номера, если его еще нет
        if number not in unique_numbers:
            unique_numbers.append(number)

# Создаем окно с графиком
fig = plt.figure(figsize=(15, 10))

# Отображаем первую страницу
plot_graphs(1)

# Показываем график
plt.show()