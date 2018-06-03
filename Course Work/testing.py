from tkinter import *
import numpy as np
from time import sleep

clicks_yes = 0
clicks_no = 0


class UI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.set_ui()

    def set_ui(self):

        def click_yes():
            global clicks_yes
            clicks_yes += 1

        def click_no():
            global clicks_no
            clicks_no += 1
        self.parent.title("Операции с матрицами")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.result = Text(self, width=50, height=25, wrap=WORD)
        self.result.grid(row=2, column=0, columnspan=5, padx=5, sticky=W)
        self.yes = Button(self, text="Да", width=10,height=5, command=lambda: click_yes())
        self.yes.grid(row=2, column=4, padx=5, sticky=E+W)
        self.no = Button(self, text="Нет", width=10,height=5, command=lambda: click_no())
        self.no.grid(row=2, column=5, padx=5, sticky=E+W)

        transpose_btn = Button(self, text="Транспонировать матрицу", width=21, command=lambda: transpose())
        transpose_btn.grid(row=0, column=1)

        multiplication_btn = Button(self, text="Умножение матриц", width=21, command=lambda: multiplication())
        multiplication_btn.grid(row=0, column=2)

        division_btn = Button(self, text="Деление", width=21, command=lambda: division())
        division_btn.grid(row=0, column=3)

        rod_btn = Button(self, text="Остаток от деления", width=21, command=lambda: rod())
        rod_btn.grid(row=0, column=4)

        min_max_btn = Button(self, text="Поиск мин/макс значения", width=21, command=lambda: min_max())
        min_max_btn.grid(row=1, column=1)

        exp_btn = Button(self, text="Возвести в степень", width=21, command=lambda: exp())
        exp_btn.grid(row=1, column=2)

        chol_btn = Button(self, text="Разложение Холецкого", width=21, command=lambda: chol())
        chol_btn.grid(row=1, column=3)

        det_btn = Button(self, text="Определитель", width=21, command=lambda: det())
        det_btn.grid(row=1, column=4)

        inv_btn = Button(self, text="Обратная матрица", width=21, command=lambda: inv())
        inv_btn.grid(row=1, column=5)

        def clear():
            self.result.delete(0.0, 'end')

        def Schitivanie(event):
            # глобальные переменные, которые функция меняет, должны быть объявлены как глобальные,
            # иначе функция просто создаст локальную переменную с тем же именем
            # и ее значение останется внутри функции
            global number_of_string
            text_from_entry_0 = entry_0.get()
            number_of_string = int(text_from_entry_0)

        def read(num):
            self.result.insert(0.0, chars='Не хотите ввести случайную матрицу? Да\Нет')
            ch1 = checker()
            if int(ch1) == 1:
                matrix = random()
                print(matrix)
                if num == 1:
                    first_matrix = matrix
                    return first_matrix
                if num == 2:
                    second_matrix = matrix
                    return second_matrix
            self.result.insert(0.0, chars='Введите вашу матрицу в файл 1.txt находящийся в папке с программой')
            print('Вторую соответственно в файл 2.txt')
            print('Все числа должны быть введены через запятую, кроме последнего элемента в строке')
            print('Пример')
            print('''1,2,3
        4,5,6
        7,8,9
                    ''')
            ch = input('Нажмите ДА когда матрица будет введена')
            if int(ch) == 1:
                first_matrix = np.genfromtxt("1.txt", delimiter=",")
                second_matrix = np.genfromtxt("2.txt", delimiter=",")
                if num == 1:
                    return first_matrix
                if num == 2:
                    return second_matrix

        def random():
            matrix = np.random.randint(0, 10, (5, 5))
            print('Случайная матрица 5x5:\n', matrix)
            return matrix

        def transpose():
            first_matrix = read(1)
            a = first_matrix.transpose()
            print('Транспонированная матрица \n', a)

        def multiplication():
            first_matrix = read(1)
            second_matrix = read(2)
            ch = input('Да - Если нужно умножить первую матрицу на второую, Нет - если наоборот')
            if int(ch) == 1:
                rez = first_matrix.dot(second_matrix)
                print(rez)
            elif int(ch) == 2:
                rez = second_matrix.dot(first_matrix)
                print(rez)

        def division():
            first_matrix = read(1)
            second_matrix = read(2)
            ch = input('Да - Если нужно разделить первую матрицу на второую, Нет - если наоборот')
            if int(ch) == 1:
                rez = first_matrix / second_matrix
                print(rez)
            elif int(ch) == 2:
                rez = second_matrix / first_matrix
                print(rez)

        def rod():
            first_matrix = read(1)
            second_matrix = read(2)
            ch = input('Да - Если нужно разделить первую матрицу на второую, Да - если наоборот')
            if int(ch) == 1:
                rez = first_matrix % second_matrix
                print(rez)
            elif int(ch) == 2:
                rez = second_matrix % first_matrix
                print(rez)

        def min_max():
            first_matrix = read(1)
            second_matrix = read(2)
            ch = input('Да - Если нужно найти максимальный элемент, Да - если минимальный')
            ch1 = input('Да - Для первого массива, Да - для второго')
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

        def exp():
            first_matrix = read(1)
            second_matrix = read(2)
            ch = input('Да - Если нужно возвести первую матрицу во вторую, Нет - если наоборот')
            if int(ch) == 1:
                rez = first_matrix ** second_matrix
                print(rez)
            elif int(ch) == 2:
                rez = second_matrix ** first_matrix
                print(rez)

        def chol():
            first_matrix = read(1)
            second_matrix = read(2)
            ch = input('Да - Если нужно разложить первую матрицу, Нет - если вторую')
            if int(ch) == 1:
                rez = np.linalg.cholesky(first_matrix)
                print(rez)
            elif int(ch) == 2:
                rez = np.linalg.cholesky(second_matrix)
                print(rez)

        def det():
            first_matrix = read(1)
            second_matrix = read(2)
            ch = input('Да - Если нужен определитель первой матрицы, Нет - если второй')
            if int(ch) == 1:
                rez = np.linalg.det(first_matrix)
                print('Определитель первой матрицы =', rez)
            elif int(ch) == 2:
                rez = np.linalg.det(second_matrix)
                print('Определитель второй матрицы =', rez)

        def inv():
            first_matrix = read(1)
            second_matrix = read(2)
            ch = input('Да - Если нужена обратная первой матрица, Нет - если второй')
            if int(ch) == 1:
                rez = np.linalg.inv(first_matrix)
                print('Определитель первой матрицы =\n', rez)
            elif int(ch) == 2:
                rez = np.linalg.inv(second_matrix)
                print('Определитель второй матрицы =\n', rez)

def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = UI(root)
    root.mainloop()


main()
