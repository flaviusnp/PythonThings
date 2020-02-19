from random import shuffle


class Pachet:
    pachet = []

    def __init__(self, pachet):

        self.pachet = pachet

    def creeaza_pachet(self):

        trefla = '\u2663'
        neagra = '\u2660'
        romb = '\u2666'
        rosie = '\u2665'
        trefle = []
        negre = []
        romburi = []
        rosii = []

        for i in range(2, 11):
            trefle.append(str(i) + trefla)
            negre.append(str(i) + neagra)
            romburi.append(str(i) + romb)
            rosii.append(str(i) + rosie)

        for i in ['A', 'J', 'Q', 'K']:
            trefle.append(i + trefla)
            negre.append(i + neagra)
            romburi.append(i + romb)
            rosii.append(i + rosie)

        self.pachet = trefle + negre + romburi + rosii

        return shuffle(self.pachet)

    def __str__(self):

        return str(self.pachet)

    def __iter__(self):

        return PachetIterator(self)


class PachetIterator:

    def __init__(self, _pachet):
        self._pachet = _pachet
        self.index = 0

    def __next__(self):
        if self.index < (len(self._pachet.pachet)):
            result = self._pachet.pachet[self.index]

            self.index += 1
            return result

        raise StopIteration


class RaspunsGresit(Exception):
    pass

class NotEnoughFoundsException(Exception):

    pass


class BustException(Exception):
    pass


my_pachet = Pachet([])
my_pachet.creeaza_pachet()

iterator = iter(my_pachet)

deck = []

while True:

    try:

        deck.append(next(iterator))

    except StopIteration:

        break

# print(deck)

# Aici avem pachetul amestecat ---> deck !!!!


class UtilJoc(RaspunsGresit):

    def __init__(self, deck, founds):

        self.deck = deck
        self.founds = founds

    def imparte_primele_carti(self, player_cards=[], dealer_cards=[]):

        self.player_cards = player_cards
        self.dealer_cards = dealer_cards

        for i in range(0, 4):

            if i % 2 == 0:

                self.player_cards.append(self.deck.pop())

            else:

                self.dealer_cards.append(self.deck.pop())

        return self.player_cards, self.dealer_cards

    # player-ul si dealer-ul au primit primul set de carti

    def draw_table(self, turn):

        self.turn = turn

        if self.turn == 'p':

            print(f"Dealer : ['{self.dealer_cards[0]}', ' ']\n")
            print(f'Player : {self.player_cards}')

        else:

            print(f'Dealer : {self.dealer_cards}\n')
            print(f'Player : {self.player_cards}')

    def hit_player(self):

        self.decision = ''
        self.ok = 0

        print('Doriti sa trageti o carte ?')

        while True:

            try:

                self.decision = input('Hit or Stand : ')

                if self.decision.lower() == 'hit':

                    self.player_cards.append(self.deck.pop())

                    self.ok = 1

                    break

                elif self.decision.lower() == 'stand':

                    break

                else:

                    raise RaspunsGresit

            except RaspunsGresit:

                print('Ai introdus un raspuns gresit !')

        return self.ok

    def hit_dealer(self):

        self.dealer_cards.append(self.deck.pop())

    def check_aces(self, jucator):

        self.jucator_cards = jucator

        aces = ['A\u2663', 'A\u2660', 'A\u2665', 'A\u2666']

        counter = 0

        for i in aces:

            for j in self.jucator_cards:

                if i == j:
                    counter += 1

        return counter

    def delete_ace(self,jucator_cards):

        aces = ['A' + '\u2663', 'A' + '\u2660', 'A' + '\u2665', 'A' + '\u2666']

        for i in aces:

            ok = 0

            for j in self.jucator_cards:

                if i == j:
                    self.jucator_cards.remove(i)
                    self.jucator_cards.append(1)
                    ok = 1
                    break

            if ok == 1:
                break

    def place_bet(self):

        #min bet is 100

        if self.founds < 100 :

            raise NotEnoughFoundsException

        while True :

            try :

                suma = int(input('Pariaza o suma: '))

                if suma > self.founds :

                    raise NotEnoughFoundsException

                else :

                    print('Ai pariat {}$'.format(suma))
                    break

            except NotEnoughFoundsException :

                print('Nu ai bani suficienti !')

        return suma

    def payment(self,suma,winner):

        if winner == 'd':

            self.founds -= suma

        elif winner == 'p':

            self.founds += suma

        return self.founds

def incepe_joc(founds):

    print("Jocul a inceput !")

    test = UtilJoc(deck, founds)
    # print(deck)

    suma_pariata = test.place_bet()

    player_cards, dealer_cards = \
        test.imparte_primele_carti(player_cards=[], dealer_cards=[])

    # FOR TESTING ONLY !
    # player_cards = ['A\u2660', '4\u2660', 1, '2\u2660', '10\u2660'] BUG !

    test.draw_table('p')

    blackjack_player = 0
    blackjack_dealer = 0
    winner = ''

    if player_cards[0][0] == 'A' and player_cards[1][0] in ['10', 'J', 'Q', 'K'] or\
        player_cards[1][0] == 'A' and player_cards[0][0] in ['10', 'J', 'Q', 'K']:

        print('BlackJack !')

        blackjack_player = 1

    if dealer_cards[0][0] == 'A' and dealer_cards[1][0] in ['10', 'J', 'Q', 'K']:

        print('Dealer-ul are BlackJack !')

        blackjack_dealer = 1

    if blackjack_player == 1 and blackjack_dealer == 1:

        print('Runda s-a terminat la egalitate !')

    elif blackjack_dealer == 1 and blackjack_player == 0:

        print('Dealer-ul a castigat!')
        founds = test.payment(suma_pariata,'d')

    elif blackjack_player == 1 and blackjack_dealer == 0:

        print('Ai castigat !')
        founds = test.payment(suma_pariata,'p')

    suma1 = 0

    while blackjack_player == 0 and blackjack_dealer == 0:

        suma_player = 0

        try:

            for x in player_cards:

                if isinstance(x, int):

                    suma_player += 1

                elif x[0][0].isdigit():

                    if x[0][0] == '1':

                        suma_player += 10

                    else:

                        suma_player += int(x[0][0])

                elif x[0][0] in ['J', 'Q', 'K']:

                    suma_player += 10

                else:

                    suma_player += 11

            if suma_player > 21 and test.check_aces(player_cards) == 0:

                raise BustException

            elif suma_player < 21:

                ok = 0
                ok = test.hit_player()

                if ok == 0:

                    suma1 = suma_player

                    print('Ai ramas cu {}'.format(suma_player))

                    break

                else:

                    test.draw_table('p')

            elif suma_player == 21:

                suma1 = suma_player
                break

            elif suma_player > 21 and test.check_aces(player_cards) != 0:

                test.delete_ace(player_cards)

        except BustException:

            print('Ai ramas cu {}'.format(suma_player))

            print('Ai depasit 21 !')

            print('Jocul s-a terminat ! Dealerul a castigat !')

            founds = test.payment(suma_pariata, 'd')

            break

    suma2 = 0
    print('\n')
    test.draw_table('d')

    while blackjack_dealer == 0 and suma1 <= 21 and suma1 != 0:

        suma_dealer = 0

        try:

            for x in dealer_cards:

                if isinstance(x, int):

                    suma_dealer += 1

                elif x[0][0].isdigit():

                    if x[0][0] == '1':

                        suma_dealer += 10

                    else:

                        suma_dealer += int(x[0][0])

                elif x[0][0] in ['J', 'Q', 'K']:

                    suma_dealer += 10

                else:

                    suma_dealer += 11

            if suma_dealer > 21 and test.check_aces(dealer_cards) == 0:

                raise BustException

            elif suma_dealer < 17:

                test.hit_dealer()
                print('\n')
                test.draw_table('d')

            elif suma_dealer >= 17 and test.check_aces(dealer_cards) == 0:

                suma2 = suma_dealer
                print('Dealer-ul a ramas cu {} '.format(suma_dealer))
                break

            elif suma_dealer == 21:

                print('\n')
                test.draw_table('d')
                suma2 = suma_dealer
                print('Dealer-ul are 21 !')
                break

            elif suma_dealer >= 17 and test.check_aces(dealer_cards) != 0:

                test.delete_ace(dealer_cards)

        except BustException:

            print('Dealer-ul are {}'.format(suma_dealer))

            break

    if suma1 != 0:

        if suma1 > suma2:

            print('Ai castigat !')
            founds = test.payment(suma_pariata, 'p')

        elif suma2 > suma1:

            print('Dealer-ul a castigat !')
            founds = test.payment(suma_pariata, 'd')

        else:

            print('Remiza')

    print('Ai {}$ in cont'.format(founds))

    print('You want to play this again ?')

    joaca_iar = input('Da sau Nu :')

    if joaca_iar.lower() == 'da':

        print('\n\n')

        incepe_joc(founds)


founds = 10000

while True:

    try:

        incepe_joc(founds)

    except NotEnoughFoundsException:

        print('Nu ai suficienti bani in cont !')

        break
