usd = 57
euro = 60
bgn = 35
huf = 22

money = int(input("Введите сумму, которую вы хотите обменять: "))
currency = int(input("Укажите код валюты (доллары - 400, евро - 401, болгарский лев - 402, венгерский форинт - 403): "))

if currency == 400:
    cache = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 401:
    cache = round(money / euro, 2)
    print("Валюта: евро")
elif currency == 402:
    cache = round(money / bgn, 2)
    print("Валюта: болгарский лев")
elif currency == 403:
    cache = round(money / huf, 2)
    print("Валюта: венгерский форинт")
else:
    cache = 0
    print("Неизвестная валюта")

print("К получению:", cache)