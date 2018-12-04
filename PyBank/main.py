
def revenuetotals():

	for row in csvreader:
		date.append(row[0])
		revenue.append(int(row[1]))

def revenuechange(revenue):

	for i in range(1,len(revenue)):
		change = revenue[i] - revenue[i - 1]
		changerev.append(change)


def printresults(date,revenue,changerev):

	print()
	print("Financial Analysis")
	print("----------------------------")
	print("Total Months: " + str(len(date)))
	print("Total: " + "$" + str(sum(revenue)))
	print("Average Change:" + "$" + str(round((sum(changerev)/len(revenue)))))
	print("Greatest Increase in Profits: "+ str(date[changerev.index(max(changerev))]) + " (" + str(max(changerev)) + ")")
	print("Greatest Decrease in Profits: " + str(date[changerev.index(min(changerev))]) + " (" + str(min(changerev)) + ")")

def exportresults(date,revenue,changerev):

	output.write("Financial Analysis"+"\n")
	output.write("----------------------------"+"\n")
	output.write("Total Months: " + str(len(date))+"\n")
	output.write("Total: " + "$" + str(sum(revenue))+"\n")
	output.write("Average Change:" + "$" + str(round((sum(changerev)/len(revenue))))+"\n")
	output.write("Greatest Increase in Profits: "+ str(date[changerev.index(max(changerev))]) + " (" + str(max(changerev)) + ")"+"\n")
	output.write("Greatest Decrease in Profits: " + str(date[changerev.index(min(changerev))]) + " (" + str(min(changerev)) + ")"+"\n")


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
	printresults(date,revenue,changerev)

output_path = os.path.join("..", "PyBank_output.text")

with open(output_path, 'a') as output: 

	exportresults(date,revenue,changerev)
