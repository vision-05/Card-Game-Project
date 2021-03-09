class Card:
	def __init__(self,col,num):
		self.color = col
		self.number = num
		self.colInitial = self.color[0]

	def getColor(self):
		return self.color

	def getNumber(self):
		return self.number

	def getInitial(self):
		return self.colInitial

#class for card, which stores the colour and number