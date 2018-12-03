
def addcandidates(voter,candidates,uni_candidates,Khan,Correy,Li,OTooley):
	for row in csvreader:
		voter.append(row[0])
		candidates.append(row[2])
		if row[2] == "Khan":
			Khan.append(row[0])
		elif row[2] == "Correy":
			Correy.append(row[0])
		elif row[2] == "Li":
			Li.append(row[0])
		elif row[2] == "O'Tooley":
			OTooley.append(row[0])

	for candidate in candidates:
		if candidate not in uni_candidates:
			uni_candidates.append(candidate)

def results(winner,voter,uni_candidates):
	totalvoters = len(voter)
	khanpercentage = winner.append(round(len(Khan)/totalvoters * 100))
	correypercentage = winner.append(round(len(Correy)/totalvoters * 100))
	lipercentage = winner.append(round(len(Li)/totalvoters * 100))
	otooleypercentage = winner.append(round(len(OTooley)/totalvoters * 100))

	print("Election Results")
	print("-------------------------")
	print("Total Votes: " + str(totalvoters))
	print("-------------------------")
	print("Khan: " + str(winner[0])+"%")
	print("Correy: " + str(winner[1])+"%")
	print("Li: " + str(winner[2])+"%")
	print("O'Tooley: " + str(winner[3])+"%")
	print("-------------------------")
	print("Winner: " + uni_candidates[winner.index(max(winner))])
	print("-------------------------")


import os
import csv 

pypolldata = os.path.join("..", "election_data.csv")
voter = []
candidates = []
uni_candidates = []
Khan = []
Correy = []
Li = []
OTooley = []
winner = []

with open(pypolldata, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader)

	addcandidates(voter,candidates,uni_candidates,Khan,Correy,Li,OTooley)
	results(winner,voter,uni_candidates)






