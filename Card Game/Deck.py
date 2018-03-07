import Card


class Deck:
    def __init__(self):  # метод __init__ используется для автоматического присвоения аттрибутов при вызове класса
        import random
        ranks = "23456789TJQKA"
        suits = "DCHS"
        self.cards = [Card(r, s) for r in ranks for s in suits] # генератор списков создающий колоду из 52 карт
        random.shuffle(self.cards)  # перетасовываем колоду в стек

    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()