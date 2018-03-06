
import account
import evro
answer = input('"Вы хотите взять кредит в иностранной валюте? (y/n)')

if answer or answer[0].lower() != 'n':
        money = int(input("Введите сумму, которую вы хотите обменять: "))
        currency = int(input("Укажите код валюты (доллары - 400, евро - 401, болгарский лев - 402, венгерский форинт - 403): "))

        result = evro.currency_calc(money,currency)

        rate = int(input("Введите процентную ставку: "))
        money = int(input("Введите сумму: "))
        period = int(input("Введите период ведения счета в месяцах: "))
        result = account.calculate_income(rate, money, period)
        print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
              "Сумма на счете в конце периода: ", result)
else:
        rate = int(input("Введите процентную ставку: "))
        money = int(input("Введите сумму: "))
        period = int(input("Введите период ведения счета в месяцах: "))

result = account.calculate_income(rate, money, period)
print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: ", result)

