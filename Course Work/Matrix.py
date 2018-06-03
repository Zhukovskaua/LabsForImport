# Реализация расчета матриц
import numpy as np

with open('1.txt', 'w') as f:
    pass
with open('2.txt', 'w') as f:
    pass


def read(num):
    ch1 = input('Не хотите ввести случайную матрицу? 1/0')
    if int(ch1) == 1:
        matrix = random()
        if num == 1:
            first_matrix = matrix
            return first_matrix
        if num == 2:
            second_matrix = matrix
            return second_matrix
    print('Введите вашу матрицу в файл 1.txt находящийся в папке с программой')
    print('Вторую соответственно в файл 2.txt')
    print('Все числа должны быть введены через запятую, кроме последнего элемента в строке')
    print('Пример')
    print('''1,2,3
4,5,6
7,8,9
            ''')
    ch = input('Отправьте единицу когда матрица будет введена')
    if int(ch) == 1:
        first_matrix = np.genfromtxt("1.txt", delimiter=",")
        second_matrix = np.genfromtxt("2.txt", delimiter=",")
        if num == 1:
            return first_matrix
        if num == 2:
            return second_matrix


def random():
        columns = input('Введите количество столбцов')
        rows = input('Введите количество строк')
        columns = int(columns)
        rows = int(rows)
        matrix = np.random.randint(0, 10, (rows, columns))
        print('Случайная матрица :\n', matrix)
        return matrix


def transpose(first_matrix):
    a = first_matrix.transpose()
    print('Транспонированная матрица \n', a)


def multiplication(first_matrix, second_matrix):
    ch = input('1 - Если нужно умножить первую матрицу на вторую, 2 - если наоборот')
    if int(ch) == 1:
        rez = first_matrix.dot(second_matrix)
        print(rez)
    elif int(ch) == 2:
        rez = second_matrix.dot(first_matrix)
        print(rez)


def division(first_matrix, second_matrix):
    ch = input('1 - Если нужно разделить первую матрицу на вторую, 2 - если наоборот')
    if int(ch) == 1:
        rez = first_matrix/second_matrix
        print(rez)
    elif int(ch) == 2:
        rez = second_matrix/first_matrix
        print(rez)


def rod(first_matrix, second_matrix):
    ch = input('1 - Если нужно разделить первую матрицу на вторую, 2 - если наоборот')
    if int(ch) == 1:
        rez = first_matrix % second_matrix
        print(rez)
    elif int(ch) == 2:
        rez = second_matrix % first_matrix
        print(rez)


def min_max(first_matrix, second_matrix):
    ch = input('1 - Если нужно найти максимальный элемент, 2 - если минимальный')
    ch1 = input('1 - Для первого массива, 2 - для второго')
    if int(ch) == 1:
        if int(ch1) == 1:
            rez = np.max(first_matrix)
            print('Максимальный элемент первого массива =', rez)
        elif int(ch1) == 2:
            rez = np.max(second_matrix)
            print('Максимальный элемент второго массива =', rez)
    elif int(ch) == 2:
        if int(ch1) == 1:
            rez = np.min(first_matrix)
            print('Минимальный элемент первого массива =', rez)
        elif int(ch1) == 2:
            rez = np.min(second_matrix)
            print('Минимальный элемент второго массива =', rez)


def exp(first_matrix, second_matrix):
    ch = input('1 - Если нужно возвести первую матрицу во вторую, 2 - если наоборот')
    if int(ch) == 1:
        rez = first_matrix ** second_matrix
        print(rez)
    elif int(ch) == 2:
        rez = second_matrix ** first_matrix
        print(rez)


def chol(first_matrix, second_matrix):
    ch = input('1 - Если нужно разложить первую матрицу, 2 - если вторую')
    if int(ch) == 1:
        rez = np.linalg.cholesky(first_matrix)
        print(rez)
    elif int(ch) == 2:
        rez = np.linalg.cholesky(second_matrix)
        print(rez)


def det(first_matrix, second_matrix):
    ch = input('1 - Если нужен определитель первой матрицы, 2 - если второй')
    if int(ch) == 1:
        rez = np.linalg.det(first_matrix)
        print('Определитель первой матрицы =', rez)
    elif int(ch) == 2:
        rez = np.linalg.det(second_matrix)
        print('Определитель второй матрицы =', rez)


def inv(first_matrix, second_matrix):
    ch = input('1 - Если нужена обратная первой матрица, 2 - если второй')
    if int(ch) == 1:
        rez = np.linalg.inv(first_matrix)
        print('Обратная первой матрица =\n', rez)
    elif int(ch) == 2:
        rez = np.linalg.inv(second_matrix)
        print('Обратная второй матрица =\n', rez)


def main():
    print('Какое действие вам необходимо совершить?')
    print('1 - Транспонировать матрицу; 2 - Умножение матриц; 3 - Деление; 4 - Остаток от деления;')
    print('5 - Поиск минимального или максимального значения; 6 - Возвести в степень; ')
    print('7 - Разложение Холецкого; 8 - Определитель; 9 - Обратная матрица;')
    action = input('Отправьте ноль для выхода')
    action = int(action)
    if action == 1:
        first_matrix = read(1)
        print('Исходная матрица\n', first_matrix)
        transpose(first_matrix)
        main()
    if action == 2:
        first_matrix = read(1)
        second_matrix = read(2)
        multiplication(first_matrix, second_matrix)
        main()
    if action == 3:
        first_matrix = read(1)
        second_matrix = read(2)
        division(first_matrix, second_matrix)
        main()
    if action == 4:
        first_matrix = read(1)
        second_matrix = read(2)
        rod(first_matrix, second_matrix)
        main()
    if action == 5:
        first_matrix = read(1)
        second_matrix = read(2)
        min_max(first_matrix, second_matrix)
        main()
    if action == 6:
        first_matrix = read(1)
        second_matrix = read(2)
        exp(first_matrix, second_matrix)
        main()
    if action == 7:
        first_matrix = read(1)
        second_matrix = read(2)
        chol(first_matrix, second_matrix)
        main()
    if action == 8:
        first_matrix = read(1)
        second_matrix = read(2)
        det(first_matrix, second_matrix)
        main()
    if action == 9:
        first_matrix = read(1)
        second_matrix = read(2)
        inv(first_matrix, second_matrix)
        main()
    if action == 0:
        exit('Выход')


if __name__ == "__main__":
    main()
