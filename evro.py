def currency_calc(money,currency):
    usd = 57
    euro = 60
    bgn = 35
    huf = 22
    if currency == 400:
        money = round(money / usd, 2)
        print("Валюта: доллары США")
    elif currency == 401:
        money = round(money / euro, 2)
        print("Валюта: евро")
    elif currency == 402:
        money = round(money / bgn, 2)
        print("Валюта: болгарский лев")
    elif currency == 403:
        money = round(money / huf, 2)
        print("Валюта: венгерский форинт")
    else:
        money = 0
        print("Неизвестная валюта")
    return money

def main():
    money = 100
    currency = 401

    result = currency_calc(money,currency)
    print("курс:", result)


if __name__ == "__main__":
    main()

