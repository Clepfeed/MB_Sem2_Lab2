import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def read_data_file(filename):
    """Чтение данных из файла формата 'x f(x)'"""
    x_values = []
    y_values = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    try:
                        x = float(parts[0])
                        y = float(parts[1])
                        x_values.append(x)
                        y_values.append(y)
                    except ValueError:
                        print(f"Ошибка в преобразовании строки '{line}' в файле {filename}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    
    return np.array(x_values), np.array(y_values)

def plot_all_data(filenames, function=None, function_name=None, x_range=(-5, 5), num_points=1000):
    """Построение графиков данных из файлов и заданной функции"""
    plt.figure(figsize=(10, 6))
    
    # Цвета для графиков из файлов
    colors = ['blue', 'green', 'red']
    
    # Построение графиков из файлов
    for i, filename in enumerate(filenames):
        x_data, y_data = read_data_file(filename)
        if len(x_data) > 0:
            plt.scatter(x_data, y_data, color=colors[i], s=30, alpha=0.7, 
                        label=f'Данные из {filename}')
            plt.plot(x_data, y_data, color=colors[i], linestyle='-', alpha=0.5)
    
    # Построение графика заданной функции
    if function is not None:
        x_func = np.linspace(x_range[0], x_range[1], num_points)
        y_func = function(x_func)
        plt.plot(x_func, y_func, color='purple', linestyle='--', linewidth=2, 
                 label=function_name if function_name else 'Заданная функция')
    
    # Настройка графика
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Графики данных из файлов и заданной функции')
    plt.legend()
    
    # Настройка делений осей
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
    
    plt.tight_layout()
    plt.show()

# Пример использования программы
if __name__ == "__main__":
    # Список файлов с данными
    filenames = ['P1.txt', 'P2.txt', 'P3.txt']
    
    # Определение заданной функции
    def custom_function(x):
        return np.cos(2*x)
    
    # Построение всех графиков
    plot_all_data(filenames, function=custom_function, function_name='cos(2x)')