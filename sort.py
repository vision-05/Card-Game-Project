def sortWinners(scores,winners):
	sortedWinners = []
	for j in range(0,len(scores)):
		for i in range(0,len(winners)):
			if winners[i].getScore() == scores[j]:
				sortedWinners.append(winners[i])

	return sortedWinners

def getSortedScores(winners):
	scores = []
	for i in winners:
		scores.append(i.getScore())

	scores.sort()

	return scores