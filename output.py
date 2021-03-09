from os import system
from time import sleep

class TerminalColors:
	lightGrey = '\033[37m'
	black = '\033[30m'
	red = '\033[31m'
	yellow = '\033[93m'
	cyanBack = '\033[46m'

textColor = TerminalColors.lightGrey

def clear():
	_ = system('clear')
	print(TerminalColors.cyanBack,textColor)

def printRules():
	rules = "In this game, each round consists of both players taking a card off the top of a shuffled deck.\nThere are a total of 30 cards and rounds continue until there are no cards left.\nEach card has a colour, red, yellow or black, and a number from 1 to 10.\nIf both cards are the same colour, the card with the highest number is the winner.\nIf the cards have different colours, the rules are as follows:\nRed beats black\nBlack beats yellow\nYellow beats red.\nThe winner is the player with the most cards at the end.\nAfter winning a round the player that wins the round keeps both cards."
	print(rules)

def setCardColor(card):
	if card.getInitial() == 'r':
		return TerminalColors.red
	elif card.getInitial() == 'b':
		return TerminalColors.black
	else:
		return TerminalColors.yellow

def printCard(card,color):
	cardEnd = "-------"
	cardMiddle = "|     |"
	cardNumber = "|  " + str(card.getNumber()) + "  |"
	if card.getNumber() == 10:
		cardNumber = "| " + str(card.getNumber()) + "  |"
	cardColor = "|  " + card.getInitial() + "  |"

	print(color + cardEnd)
	print(cardColor)
	print(cardMiddle)
	print(cardMiddle)
	print(cardNumber)
	print(cardEnd)
	print(textColor)

def printCards(card1,card2):
	color1 = setCardColor(card1)
	color2 = setCardColor(card2)

	input("Press enter to pick a card player 1: ")
	printCard(card1,color1)
	input("Press enter to pick a card player 2: ")
	printCard(card2,color2)

def printWinnerCards(winnerCards):
	for card in winnerCards:
		color = setCardColor(card)
		printCard(card,color)

def printWinners(lis):
	print("Top winners:")
	for i in lis:
		print(i.getName(),i.getScore())

def getWinner(player1,player2):
	if player1.getCardsNumber() > player2.getCardsNumber():
		print("Player 1 wins!")
		print("Player 1's cards: ")
		winner = player1
		nonWinner = player2
	else:
		print("Player 2 wins!")
		print("Player 2's cards: ")
		winner = player2
		nonWinner = player1
	printWinnerCards(winner.getCards())
	return winner,nonWinner

def printScore(player1,player2):
	player1.setGameScore()
	player2.setGameScore()
	player1.addScore()
	player2.addScore()

	print("Player 1's score this game: " + str(player1.getGameScore()))
	print("Player 2's score this game: " + str(player2.getGameScore()))
	print("Player 1's total score: " + str(player1.getScore()))
	print("Player 2's total score: " + str(player2.getScore()))
	sleep(1)

	return player1,player2

def isPreviousWinner(index):
	if index != -1:
		return True
	return False