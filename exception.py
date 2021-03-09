#this file stores all of the exceptions needed to keep error from occuring
#and do message passing and event handling

#finds the line in a file that is not formatted properly
#need to add symbol detection and space detection to trigger this error
class InvalidUserDataLine(BaseException):
	def __init__(self,msg,ind,invalidChar):
		self.message = msg
		self.index = ind
		self.invalidChar = invalidChar

	def what(self):
		return self.message

	def getIndex(self):
		return self.index

	def getInvalidChar(self):
		return self.invalidChar

#says what function failed and what kind of function it is
class FunctionFailed(BaseException):
	def __init__(self,msg,functionsAffected,isWriteOperation,isReadOperation,lineIndexOfError,userData,invalidChar):
		self.message = msg
		self.functionsAffected = functionsAffected
		self.isReadOperation = isReadOperation
		self.isWriteOperation = isWriteOperation
		self.lineIndexOfError = lineIndexOfError
		self.data = userData
		self.invalidChar = invalidChar

	def what(self):
		return self.message

	def getFuncsAffected(self): #use this to diagnose problem and do automatic error correction
		return self.functionsAffected

	def getDiagnosticData(self):
		if self.isReadOperation:
			return (1,self.lineIndexOfError)
		elif self.isWriteOperation:
			return (2,-1)
		else:
			return (0,-1)

	def getData(self):
		return self.data

	def getInvalidChar(self):
		return self.invalidChar

#notifies if username is not found
class UserNameNotFound(BaseException):
	def __init__(self,name):
		self.message = "User: " + name + " does not exist"

	def what(self):
		return self.message

#notifies if invalid password is entered
class InvalidPassword(BaseException):
	def __init__(self,name):
		self.message = "Password is incorrect for user " + name

	def what(self):
		return self.message

#message passer for the lines that are incorrectly formatted
class LinesToBeDeleted(BaseException):
	def __init__(self,data,fi):
		self.data = data
		self.filename = fi

	def getFilename(self):
		return self.filename

	def getCorruptDataSet(self):
		return self.data

class RemoveAllSpaces(BaseException):
	def __init__(self,data,fi):
		self.data = data
		self.filename = fi

	def getCorruptDataSet(self):
		return self.data

	def getFilename(self):
		return self.filename

#notifies if user is already logged in for this instance of the game
class AlreadyLoggedIn(BaseException):
	def __init__(self,name):
		self.name = name

	def what(self):
		return self.name + "is already logged in!"

#used for case where the top five winner list is not full
class NotEnoughData(BaseException):
	def __init__(self,message,winners):
		self.message = message
		self.winners = winners
	
	def what(self):
		return self.message

	def getWinners(self):
		return self.winners

#used to notify if user tries to register an invalid username
class InvalidUserName(BaseException):
	def __init__(self,username,error):
		self.error = error
		self.username = username

	def what(self):
		return self.username + ' ' + self.error

	def getError(self):
		return self.error