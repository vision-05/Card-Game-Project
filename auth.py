import hashlib
import read as r
import exception as e
import write as w
import player as p

#make sure new users dont have space or symbols in name
def auth(loggedIn):
	try:
		allUsers = r.readAllUsers("hashTable.txt")
		hasAccount = input("Do you own an existing account: ")
		if hasAccount.lower() == "no":
			register(allUsers) #carry on with the log on process after registering

		allUsers = r.readAllUsers("hashTable.txt")
		name = input("Enter you name: ")
		playerLoggedIn(name,loggedIn)

		playerIndex = -1

		if isinstance(nameExists(allUsers,name), int):
			playerIndex = nameExists(allUsers,name)
			#make sure not to assign the index if there is no return type for the function, so there are no run time errors unhandled

			password = hashlib.sha256(input("Enter password: ").encode('utf-8'))
			isConfirmedPassword(password.hexdigest(),allUsers[playerIndex].getPasscode(),name)

			return allUsers[playerIndex]
	
	except e.FunctionFailed as ex:
		data = ex.getDiagnosticData()
		if data[0] == 1 and data[1] != -1:
			if ex.getInvalidChar() == ' ':
				raise e.RemoveAllSpaces(ex.getData(),"hashTable.txt")
			else: #check whether the invalid character needs to delete invalid data or whether the data can be corrected
				raise e.LinesToBeDeleted(ex.getData(),"hashTable.txt")
		else:
			print("Fatal error, function failed randomly, exiting...")
			exit(1)

	except e.UserNameNotFound as ex:
		print(ex.what())
		return 1
		

	except e.InvalidPassword as ex:
		print(ex.what())
		return 2

	except e.InvalidUserName as ex:
		print(ex.what())
		return 1

	except e.AlreadyLoggedIn as ex:
		print(ex.what())
		return 3

def isConfirmedPassword(pass1,pass2,name):
	if pass1 == pass2: #compare both hashed passwords
		print("Successful login!")	
	else:
		raise e.InvalidPassword(name)

def playerLoggedIn(name,loggedIn):
	if loggedIn != 0:
		if name == loggedIn.getName():
			raise e.AlreadyLoggedIn(name)

def register(users):
	name = input("Enter your name: ")
	try:
		isValidUserName(name)
		nameExists(users,name)
		raise e.InvalidUserName(name,"already exists!")
	except e.UserNameNotFound: #make sure the username is new
		password = input("Enter your password: ")
		pass2 = input("Verify your password: ")
	
		nameCorrectLength(name)
		if password == pass2:
			print("Account created!")
			passcode = hashlib.sha256(password.encode('utf8'))
			score = 0
			passcode = passcode.hexdigest()

			newPlayer = p.Player(score,name,passcode)
			w.appendNewUser("hashTable.txt",newPlayer)
			
	except e.InvalidUserName as ex:
		raise e.InvalidUserName(name,ex.getError())

def nameCorrectLength(username):
	if len(username) < 4:
		raise e.InvalidUserName(username,"must be 4 letters or longer!")

def isName(player,name):
	if player.getName() == name:
		return True
	return False

def nameExists(allUsers,name):
	for i in range(0,len(allUsers)):
		if isName(allUsers[i],name):
			return i
	raise e.UserNameNotFound(name)

def authorisePlayer(loggedIn):
	while True:
		unsuccessfulUsername = 0
		unsuccessfulPassword = 0
		authAttempt = auth(loggedIn)
		if authAttempt == 1:
			print("Invalid username")
			unsuccessfulUsername += 1
			if unsuccessfulUsername > 2:
				print("Too many attempts, exiting...")
				exit(1)
		elif authAttempt == 2:
			print("Invalid password")
			unsuccessfulPassword += 1
			if unsuccessfulPassword > 2:
				print("Too many attempts, exiting...")
				exit(1)
		elif authAttempt == 3:
			continue
		else:
			break
	
	return authAttempt

def isValidUserName(username):
	symbols = "!£$%^&*()[]{}:;,.=+\\|#~'@\"`¬ "
	for i in username:
		for j in symbols:
			if i == j:
				raise e.InvalidUserName(username,"includes a symbol or space, that is not an underscore!")

	return True