class Player:
	def __init__(self,sc,nm,ps):
		self.score = sc
		self.gameScore = 0
		self.name = nm
		self.password = ps
		self.cards = []
	
	def getName(self):
		return self.name

	def getScore(self):
		return self.score

	def getPasscode(self):
		return self.password

	def addCards(self,card1,card2):
		self.cards.append(card1)
		self.cards.append(card2)

	def getCardsNumber(self):
		return len(self.cards)

	def addScore(self):
		self.score += self.getCardsNumber()

	def setScore(self,sc):
		self.score = sc

	def setGameScore(self):
		self.gameScore = self.getCardsNumber()

	def getGameScore(self):
		return self.gameScore

	def getCards(self):
		return self.cards

#class for a player, which stores the score, password hash, cards and name