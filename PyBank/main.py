
def revenuetotals():

	for row in csvreader:
		date.append(row[0])
		revenue.append(int(row[1]))

def revenuechange(revenue):

	for i in range(1,len(revenue)):
		change = revenue[i] - revenue[i - 1]
		changerev.append(change)


def answers(date,revenue,changerev):

	maximum = max(changerev)
	minimum = min(changerev)

	print()
	print("Financial Analysis")
	print("----------------------------")

	print("Total Months: " + str(len(date)))
	print("Total: " + "$" + str(sum(revenue)))

	print("Average Change:" + "$" + str(round((sum(changerev)/len(revenue)))))

	print("Greatest Increase in Profits: "+ str(date[changerev.index(maximum)]) + " (" + str(maximum) + ")")
	print("Greatest Decrease in Profits: " + str(date[changerev.index(minimum)]) + " (" + str(minimum) + ")")


import os
import csv


pybankdata = os.path.join('..','PyBank_data.csv')


with open(pybankdata, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader)
	date = []
	revenue = []
	changerev = []

	revenuetotals()
	revenuechange(revenue)
	answers(date,revenue,changerev)

output_path = os.path.join("..", "output.text")

#with open(output_path, 'a') as output: 
#	 answeroutput = answers(date,revenue,changerev)
#	 output.write(



