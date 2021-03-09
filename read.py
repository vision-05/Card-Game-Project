import exception as e
import player as p

#create functions to find symbols
#create function to get rid of spaces and check again for invalid formatting

def findName(ls,name):
	if len(ls) == 0:
		return -1
	for i in range(0,len(ls)):
		if ls[i].getName() == name:
			return i
	return -1

def findChars(line,index,character):
	chars = addChars(line,character)
	return chars

def addChars(line,character):
	characters = []
	for i in range(0,len(line)):
		if line[i] == character:
			characters.append(i)
	return characters

def hasSymbol(name):
	symbols = "!£$%^&*()#~'@\\|\"`¬<>?/.:;-+=[]{}"
	for i in name:
		for j in symbols:
			if i == j:
				return True,j
	return False,0

def readLineToPlayer(line,index):
	try:
		commas = findChars(line,index,',')
		if len(commas) < 2:
			raise e.InvalidUserDataLine("Invalid user data entry",index,',')
		spaces = findChars(line,index,' ')
		if len(spaces) > 0:
			raise e.InvalidUserDataLine("Invalid user data entry",index,' ')
		symbol = hasSymbol(line)
		if symbol[0] == True:
			raise e.InvalidUserDataLine("Invalid user data entry",index,symbol[1])
		score = int(line[0:commas[0]]) #first string is the score
		name = line[commas[0] + 1:commas[1]] #then the name
		passcode = line[commas[1] + 1:].rstrip('\n') #then the hashed passcode

		newPlayer = p.Player(score,name,passcode) #use the formatted data and skip the comma
		return newPlayer

	except e.InvalidUserDataLine as ex:
		print(ex.what())
		raise e.InvalidUserDataLine(ex.what(),ex.getIndex(),ex.getInvalidChar()) #acknowledge the error and pass on to find the line
	


def readAllUsers(filename):
	try:
		playerList = []
		#store lines in buffer, not read straight from file
		openFile = open(filename,'r')
		lines = getLines(openFile)
		
		for i in range(0,len(lines)):
			newPlayer = readLineToPlayer(lines[i],i)
			playerList.append(newPlayer)
		openFile.close()
		return playerList

	except e.InvalidUserDataLine as ex:
		funcsAffected = ["readAllUsers","readLineToPlayer","findChars"]
		raise e.FunctionFailed(ex.what(),funcsAffected,False,True,ex.getIndex(),lines,ex.getInvalidChar())

def getLines(file):
	lines = []
	for i in file:
		lines.append(i.rstrip('\n'))
	return lines

def findErrorLinesSymbols(filename):
	openFile = open(filename,'r')
	lines = getLines(openFile)
	linesToDelete = []
	for i in range(0,len(lines)):
		symbol = hasSymbol(lines[i])
		if symbol[0] == True:
			linesToDelete.append(i)
	return linesToDelete

def findErrorLinesCommas(filename):
	openFile = open(filename,'r')
	lines = getLines(openFile)
	linesToDelete = []
	#find the lines with invalidly formatted data
	for i in range(0,len(lines)):
		commas = addChars(lines[i],',')
		length = len(commas)
		if length < 2:
			linesToDelete.append(i)
	#return the index of these lines
	return linesToDelete

def removeLinesToDelete(userData,filename):
	linesToDelete = findErrorLinesCommas(filename)
	linesToDeleteSymbols = findErrorLinesSymbols(filename)

	if len(linesToDelete) < 1 and len(linesToDeleteSymbols) < 1:
		return userData
	
	if len(linesToDelete) > 0:
		for i in linesToDelete:
			userData.pop(i)
	else:
		for i in linesToDeleteSymbols:
			userData.pop(i)

	return userData

def findErrorLinesSpaces(filename):
	openFile = open(filename,'r')
	lines = getLines(openFile)
	linesToEdit = []

	for i in range(0,len(lines)):
		spaces = addChars(lines[i],' ')
		length = len(spaces)
		if length > 0:
			linesToEdit.append(i)

	return linesToEdit

def removeSpaces(userData,filename):
	linesToEdit = findErrorLinesSpaces(filename)

	if len(linesToEdit) < 1:
		return userData

	for i in linesToEdit:
		userData[i] = userData[i].replace(" ","")

	return userData

def readWinnerData(filename):
	openFile = open(filename,'r')
	lines = getLines(openFile)
	winnerList = []

	try:
		if len(lines) < 5:
			for i in range(0,len(lines)):
				newPlayer = readLineToPlayer(lines[i],i)
				winnerList.append(newPlayer)
			openFile.close()
			raise e.NotEnoughData("Less than five winners recorded!",winnerList)
		for i in range(0,len(lines)):
			newPlayer = readLineToPlayer(lines[i],i)
			winnerList.append(newPlayer)
		openFile.close()
		return winnerList

	except e.InvalidUserDataLine as ex:
		funcsAffected = ["readWinnerData","readLineToPlayer","findChars"]
		raise e.FunctionFailed(ex.what(),funcsAffected,False,True,ex.getIndex(),lines,ex.getInvalidChar())

def getWinners():
	try:
		winners = readWinnerData("winner.txt")
		return winners
	except e.NotEnoughData as ex:
		return (ex.getWinners(),5)
	except e.FunctionFailed as ex:
		data = ex.getDiagnosticData()
		if data[0] == 1 and data[1] != -1:
			if ex.getInvalidChar() == ' ':
				raise e.RemoveAllSpaces(ex.getData(),"winner.txt")
			else:
				raise e.LinesToBeDeleted(ex.getData(),"winner.txt")
		else:
			print("Fatal error, function failed randomly, exiting...")
			exit(1)