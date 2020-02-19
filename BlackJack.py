from random import shuffle

class Pachet:

	pachet = []

	def __init__(self,pachet) :

		self.pachet = pachet

	def creeaza_pachet(self):

		trefla = '\u2663' 
		neagra = '\u2660'
		romb   = '\u2666'
		rosie  = '\u2665'
		trefle  = []
		negre   = []
		romburi = []
		rosii   = []
		pachet = []

		for i in range(2,11) :

			trefle.append(str(i) + trefla)
			negre.append(str(i) + neagra)
			romburi.append(str(i) + romb)
			rosii.append(str(i) + rosie)

		for i in ['A','J','Q','K'] :

			trefle.append(i + trefla)
			negre.append(i + neagra)
			romburi.append(i + romb)
			rosii.append(i + rosie)

		self.pachet = trefle + negre + romburi + rosii

		return shuffle(self.pachet)

	def __str__(self) :

		return str(self.pachet)

	def __iter__(self) :

		return PachetIterator(self)

class PachetIterator :

	def __init__(self,_pachet) :

		self._pachet = _pachet
		self.index = 0

	def __next__(self) :

		if self.index < (len(self._pachet.pachet)) :

			result = self._pachet.pachet[self.index]

			self.index += 1
			return result

		raise StopIteration

class RaspunsGresit(Exception) :

	pass

class BustException(Exception) :

	pass

my_pachet = Pachet([])
my_pachet.creeaza_pachet()

iterator = iter(my_pachet)

deck = []

while True :

	try :

		deck.append(next(iterator))
		

	except StopIteration :

		break

#print(deck)

#Aici avem pachetul amestecat ---> deck !!!!

class UtilJoc(RaspunsGresit) :

	def __init__(self,deck) :

		self.deck = deck

	def imparte_primele_carti(self,player_cards=[],dealer_cards=[]):
		
		self.player_cards = player_cards
		self.dealer_cards = dealer_cards

		for i in range(0,4) :

			if i % 2 == 0 :

				self.player_cards.append(self.deck.pop())

			else :

				self.dealer_cards.append(self.deck.pop())

		return self.player_cards,self.dealer_cards

	#player_cards,dealer_cards = \
		#imparte_primele_carti(self,deck,player_cards=[],dealer_cards=[])

	#player-ul si dealer-ul au primit primul set de carti

	def draw_table(self,turn) :

		self.turn = turn

		if self.turn == 'p' :

			print (f"Dealer : ['{self.dealer_cards[0]}', ' ']\n")
			print (f'Player : {self.player_cards}')

		else :

			print (f'Dealer : {self.dealer_cards}\n')
			print (f'Player : {self.player_cards}')

	def hit_player(self) :

		self.decision = ''
		self.ok = 0

		print ('Doriti sa trageti o carte ?')

		while True :

			try :

				self.decision = input('Hit or Stand : ')

				if self.decision.lower() == 'hit' :

					self.player_cards.append(self.deck.pop())

					self.ok = 1

					break

				elif self.decision.lower() == 'stand' :

					break

				else :

					raise RaspunsGresit

			except RaspunsGresit :

				print ('Ai introdus un raspuns gresit !')

		return self.ok

	def check_aces(self) :

		aces = ['A\u2663','A\u2660','A\u2665','A\u2666']

		counter = 0

		for i in aces :

			for j in self.player_cards :

				if i == j :

					counter += 1

		return counter

	def delete_ace(self) :

		aces = ['A\u2663','A\u2660','A\u2665','A\2666']

		for i in aces :

			for j in self.player_cards :

				if i == j :

					self.player_cards.remove(i)
					break

def incepe_joc():

	print("Jocul a inceput !")

	test = UtilJoc(deck)
	#print(deck)
	player_cards,dealer_cards = \
		test.imparte_primele_carti(player_cards=[],dealer_cards=[])

	test.draw_table('p')

	while True :

		suma_player = 0
		
		try :

			for x in player_cards :

				if x[0][0].isdigit() :

					if x[0][0] == '1' :

						suma_player += 10

					else :

						suma_player += int(x[0][0])

				elif x[0][0] in ['J','Q','K'] :

					suma_player += 10

				else :

					suma_player += 11

			print('aces=',test.check_aces())

			if suma_player > 21 and test.check_aces() == 0:

				raise BustException

			elif suma_player < 21 :

				ok = 0
				ok = test.hit_player()

				if ok == 0 :
					
					break

				else :

					test.draw_table('p')

			elif suma_player > 21 and test.check_aces() != 0 :

				suma_player -= 10
				
				#test.delete_ace()
				

		except BustException :

			print ('Ai depasit 21 !')
			print ('Jocul s-a terminat ! Dealerul a castigat !')
			break

	print ('Ai ramas cu {}'.format(suma_player))

	print('You want to play this again ?')
	joaca_iar = input('Da sau Nu :')

	if joaca_iar.lower() == 'da' :

		print('\n\n')
		incepe_joc()


incepe_joc()



		













	




