linii = {'h':'_ _ _ _ _ _ _ _ _ _',
	'v':'      |      |       '}

class WrongSymbolError(Exception):

	pass

def white_spaces(n) :

	return (n * ' ')

def draw_board(board) :

	for i in range(0,19) :

		if i % 2 == 0 and i not in [6,12,4,10,16] :

			print(white_spaces(22))

		elif i == 6 or i == 12 :

			print (linii['h'])

		elif i == 4 :

			print(white_spaces(2) + board[6] + white_spaces(6) + board[7] 
				+ white_spaces(6) + board[8] + white_spaces(5) )

		elif i == 10 :

			print(white_spaces(2) + board[3] + white_spaces(6) + board[4] 
				+ white_spaces(6) + board[5] + white_spaces(5) )

		elif i == 16 :

			print(white_spaces(2) + board[0] + white_spaces(6) + board[1] 
				+ white_spaces(6) + board[2] + white_spaces(5) )

		else :

			print (linii['v'])

def play_again():

	print('Doriti sa mai jucati ?')
	b = input('Da sau Nu : ')
	
	if b == 'Da' or b == 'da' or b == 'DA' :

		play()

def pick():

	while True :

		try :

			k = int(input('Introduceti valoarea corespunzatoare casutei: '))

		except ValueError :

			print ('Nu ai ales o valoare corecta!')

		else :

			return k
			break

def play() :

	print ('Jocul a inceput!')

	while True :

		try :

			a = input('Alege cu ce vei juca : X sau 0 ? ')

			if a != 'X' and a != 'x' and a != '0' :

				raise WrongSymbolError

		except WrongSymbolError :

			print('Ati introdus o valoare straina!')
	
		else :

			break

	board = ['','','','','','','','','']

	rand = 'X'
	
	ok = 0
	nu_rand = ''

	while ok == 0 :

		if board != ['','','','','','','','',''] :
			
			if board[0] == board[1] and board[1] == board[2] and \
			board[0] != '' or \
			board[3] == board[4] and board[4] == board[5] and \
			board[3] != '' or \
			board[6] == board[7] and board[7] == board[8] and \
			board[6] != '' or \
			board[6] == board[3] and board[3] == board[0] and \
			board[6] != '' or \
			board[7] == board[4] and board[4] == board[1] and \
			board [7] != '' or \
			board[8] == board[5] and board[5] == board[2] and \
			board [8] != '' or \
			board[6] == board[4] and board[4] == board[2] and \
			board [6] != '' or \
			board[8] == board[4] and board[4] == board[0] and \
			board [8] != '':

				print ('Jocul s-a terminat !')
				if rand == 'X' :

					nu_rand = '0'

				else :

					nu_rand = 'X'
				
				print ("Castigatorul este : %s " % nu_rand)
	
				ok = 1

		if ok == 1 :

			play_again()
			break

		if '' not in board :

			print ("Jocul s-a terminat!")
			
			print ("Nimeni nu a castigat acest joc!")

			ok = 1

		if ok == 1 :

			play_again()
			break

		p = pick()
		
		board[p-1] = rand

		if rand == 'X' :

			rand = '0'

		else :

			rand = 'X'

		
		draw_board(board)

play()







