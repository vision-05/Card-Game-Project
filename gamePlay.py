import card as c
from random import shuffle
from time import sleep
import output as o
import read as r
import sort as s
import exception as e

def player1Wins(card1,card2):
	redWin = card1.getColor() == "red" and card2.getColor() == "black"
	blackWin = card1.getColor() == "black" and card2.getColor() == "yellow"
	yellowWin = card1.getColor() == "yellow" and card2.getColor() == "red"
	if card1.getColor() == card2.getColor() and card1.getNumber() > card2.getNumber():
		return True
	elif redWin or blackWin or yellowWin:
		return True
	else:
		return False

def initializeDeck():
	colors = ["red","yellow","black"]
	cards = []

	for i in colors:
		for j in range(1,11):
			cards.append(c.Card(i,j))

	shuffle(cards)
	return cards

def gameLoop(cards,player1,player2):
	while len(cards) > 0:
		p1card = cards[-1] #pick last card
		cards.remove(p1card) #remove from deck
		p2card = cards[-1]
		cards.remove(p2card)

		o.printCards(p1card,p2card)

		if player1Wins(p1card,p2card):
			print("Player 1 wins the round!")
			player1.addCards(p1card,p2card)
		else:
			print("Player 2 wins the round!")
			player2.addCards(p1card,p2card)
		sleep(3)
		o.clear()

	return player1,player2

def isLessThanFiveWinners(winners,winner):
	if isinstance(winners, tuple): #this condition is if there are less than five winners
		index = r.findName(winners[0],winner.getName())
		if o.isPreviousWinner(index): #if the winner is already in the list of winners
			winners[0][index] = winner
			winners = winners[0]
		elif len(winners[0]) != 0:
			winners[0].append(winner)
			sortedWinners = s.sortWinners(s.getSortedScores(winners[0]),winners[0])
			sortedWinners.reverse()
			winners = sortedWinners
		else: #if there are no recorded winners
			winners[0].append(winner)
			winners = winners[0]

		raise e.NotEnoughData("",winners)

def isFiveOrMoreWinners(winners,winner):
		index = r.findName(winners,winner.getName())
		if o.isPreviousWinner(index):
			winners[index] = winner
		else: #if there are five winner already in the list
			sortedWinners = s.sortWinners(s.getSortedScores(winners),winners)
			#sort winner by score and put the new winner in the right place
			if sortedWinners[0].getScore < winner.getScore():
				for i in range(0,len(sortedWinners)):
					if winner.getScore() > sortedWinners[i].getScore():
						sortedWinners.insert(i,winner)
						sortedWinners.pop(0)

def formatWinners(winners,winner,nonWinner):
	if (isinstance(winners,tuple) and len(winners[0]) > 0):
		index = r.findName(winners[0],nonWinner.getName()) #update the non winners score in the winner list, the list will be resorted later
		winners[0][index] = nonWinner
	elif (isinstance(winners,list) and len(winners) > 0):
		index = r.findName(winners,nonWinner.getName()) #update the non winners score in the winner list, the list will be resorted later
		winners[index] = nonWinner
	try:
		isLessThanFiveWinners(winners,winner) #if there are less than five winners, an exception should be raised to skip the next line, so omission of control statement
		winners = isFiveOrMoreWinners(winners,winner) #this needs a return variable
		raise e.NotEnoughData("",winners) #bad use of the class, but used for succinct code, used to join back the branches of flow
	except e.NotEnoughData as ex:
		winners = ex.getWinners()
		return winners