def appendNewUser(filename,user):
	openFile = open(filename, 'a')
	score = str(user.getScore())
	name = user.getName()
	passcode = user.getPasscode()

	openFile.write(score + ',' + name + ',' + passcode + '\n')
	openFile.close()

def rewriteData(playerData,filename):
	openFile = open(filename,"wt")
	for i in playerData:
		openFile.write(i + '\n')
	openFile.close()

def userToString(user):
	score = str(user.getScore())
	name = user.getName()
	passcode = user.getPasscode()

	return score + ',' + name + ',' + passcode + '\n'
	

def writeWinners(filename,users):
	openFile = open(filename,"wt")

	for user in users:
		data = userToString(user)

		openFile.write(data)
	openFile.close()

def writeUserData(filename,user,user1,data):
	for i in data:
		if user.getName() == i.getName():
			i.setScore(user.getScore())
		elif user1.getName() == i.getName():
			i.setScore(user1.getScore())

	openFile = open(filename,"wt")
	for userN in data:
		string = userToString(userN)
		openFile.write(string)
	openFile.close()