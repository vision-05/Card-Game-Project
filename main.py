from auth import authorisePlayer
import sort as s
import exception as e
import write as w
import read as r
import output as o
import gamePlay as g
import player as p
from time import sleep

background = o.TerminalColors.cyanBack
print(background)
print(o.textColor)
o.clear()

player1 = 0 #initialise both players before running code
player2 = 0

filename = "hashTable.txt"

while True:
	try:
		o.clear()
		print("Player 1 login:")
		player1 = authorisePlayer(0)
		break
	except e.LinesToBeDeleted as ex:
		w.rewriteData(r.removeLinesToDelete(ex.getCorruptDataSet(),filename),filename)
		w.rewriteData(r.removeSpaces(ex.getCorruptDataSet(),filename),filename)
	except e.RemoveAllSpaces as ex:
		w.rewriteData(r.removeSpaces(ex.getCorruptDataSet(),filename),filename)
		w.rewriteData(r.removeLinesToDelete(ex.getCorruptDataSet(),filename),filename)

sleep(1)
o.clear()

while True:
	try:
		o.clear()
		print("Player 2 login:")
		player2 = authorisePlayer(player1)
		break
	except e.LinesToBeDeleted as ex:
		w.rewriteData(r.removeLinesToDelete(ex.getCorruptDataSet(),filename),filename)
		w.rewriteData(r.removeSpaces(ex.getCorruptDataSet(),filename),filename)
	except e.RemoveAllSpaces as ex:
		w.rewriteData(r.removeSpaces(ex.getCorruptDataSet(),filename),filename)
		w.rewriteData(r.removeLinesToDelete(ex.getCorruptDataSet(),filename),filename)

sleep(1)
o.clear()

o.printRules()
sleep(10)
o.clear()


player1,player2 = g.gameLoop(g.initializeDeck(),player1,player2)
player1,player2 = o.printScore(player1,player2)

winner,nonWinner = o.getWinner(player1,player2)

filename = "winner.txt"

winners = []

while True:
	try:
		winners = r.getWinners()
		break
	except e.LinesToBeDeleted as ex:
		w.rewriteData(r.removeLinesToDelete(ex.getCorruptDataSet(),filename),filename)
		w.rewriteData(r.removeSpaces(ex.getCorruptDataSet(),filename),filename)
	except e.RemoveAllSpaces as ex:
		w.rewriteData(r.removeSpaces(ex.getCorruptDataSet(),filename),filename)
		w.rewriteData(r.removeLinesToDelete(ex.getCorruptDataSet(),filename),filename)

winners = g.formatWinners(winners,winner,nonWinner)
winners = s.sortWinners(s.getSortedScores(winners),winners)
winners.reverse()

o.printWinners(winners)

w.writeWinners("winner.txt",winners)
w.writeUserData("hashTable.txt",player1,player2,r.readAllUsers("hashTable.txt"))