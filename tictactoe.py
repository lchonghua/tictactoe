# For using the same code in either python 2 or 3
## Note: for python 2, use raw_input() to get player input; 
# for python 3, use input()
from __future__ import print_function
import os

board = [0]*9
markers = {0: 'A', 1:'B'}
current_player = 0

def clear():
	os.system('cls')

def display_board():
	clear()
	print('It\'s player-'+ markers[current_player]+ '\'s turn:')
	hLine = '- - - - - - - - - -'
	for i in [0, 3, 6]:
		print(hLine)
		print('| ', board[i],' | ', board[i+1], ' | ', board[i+2], ' |')
	print(hLine)

def player_input():
	loc = int(raw_input('player-' + markers[current_player] + ' input (1-9):'))
	while (loc not in range(1,10)) or (not isPositionAvailable(board, loc-1)):
		loc = int(raw_input('player-' + markers[current_player] + ' input (1-9):'))
	return loc-1		
	
def isPositionAvailable(board, pos):
	return board[pos] == 0

def place_marker(board, position):
	global current_player
	board[position] = markers[current_player]
	
	return board

def switch_player():
	return (current_player-1)**2

def isWin():
	marker = markers[current_player]
	return ((board[0] == marker and board[1] == marker and board[2] == marker) or 
		(board[3] == marker and board[4] == marker and board[5] == marker) or
		(board[6] == marker and board[7] == marker and board[8] == marker) or 
		(board[0] == marker and board[3] == marker and board[6] == marker) or
		(board[1] == marker and board[4] == marker and board[7] == marker) or
		(board[2] == marker and board[5] == marker and board[8] == marker) or
		(board[0] == marker and board[4] == marker and board[8] == marker) or
		(board[2] == marker and board[4] == marker and board[6] == marker))
	

def isBoardFull():
	return 0 not in board


while True:
	display_board()
	loc = player_input()
	board = place_marker(board, loc)
	
	if(isWin()):
		display_board()
		print('**** player -', markers[current_player], ' won! ****')
		break
	elif(isBoardFull()):
		print('**** TIE ****')
		break
	else:
		current_player = switch_player()
		print('Switch player...')

	




