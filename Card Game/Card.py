class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        """ Возращает количество очков которое дает карта """

        if self.rank in "TJQK":
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)
